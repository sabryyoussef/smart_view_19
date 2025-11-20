# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
import logging
import re

_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # WhatsApp Integration
    whatsapp_sent = fields.Boolean(
        string='WhatsApp Sent',
        default=False,
        copy=False,
        help="Indicates if quotation was sent via WhatsApp"
    )
    whatsapp_sent_date = fields.Datetime(
        string='WhatsApp Sent Date',
        copy=False,
        help="Date and time when quotation was sent via WhatsApp"
    )
    whatsapp_message_count = fields.Integer(
        string='WhatsApp Messages',
        compute='_compute_whatsapp_message_count',
        help="Number of WhatsApp messages sent for this order"
    )
    partner_whatsapp = fields.Char(
        string='Customer WhatsApp',
        related='partner_id.phone',
        help="Customer's WhatsApp number (uses phone field)"
    )
    can_send_whatsapp = fields.Boolean(
        string='Can Send WhatsApp',
        compute='_compute_can_send_whatsapp',
        help="Check if quotation can be sent via WhatsApp"
    )

    @api.depends('partner_id.phone')
    def _compute_can_send_whatsapp(self):
        """Check if customer has valid WhatsApp number"""
        for order in self:
            can_send = False
            if order.partner_id and order.partner_id.phone:
                # Basic validation - has phone number
                mobile = order.partner_id.phone
                # Remove spaces and special chars
                clean_mobile = re.sub(r'[^\d+]', '', mobile)
                # Check if it looks like a phone number (at least 8 digits)
                if len(re.sub(r'[^\d]', '', clean_mobile)) >= 8:
                    can_send = True
            order.can_send_whatsapp = can_send

    @api.depends('partner_id')
    def _compute_whatsapp_message_count(self):
        """Count WhatsApp messages sent for this SO"""
        for order in self:
            # Query pragtech_whatsapp_base messages
            messages = self.env['whatsapp.messages'].search([
                '|',
                ('message', 'ilike', order.name),
                ('message', 'ilike', 'SO%s' % order.id),
            ])
            order.whatsapp_message_count = len(messages)

    def action_send_whatsapp(self):
        """
        REQ-00027 Task 27: Send quotation via WhatsApp
        Opens wizard to send quotation
        """
        self.ensure_one()
        
        # Validate customer has WhatsApp
        if not self.partner_id:
            raise UserError(_("Please select a customer first."))
        
        if not self.partner_id.phone:
            raise UserError(_(
                "Customer %s does not have a phone number.\n\n"
                "Please add a phone number in the customer's contact information."
            ) % self.partner_id.name)
        
        # Validate WhatsApp instance exists
        whatsapp_instance = self.env['whatsapp.instance'].search([
            ('status', '=', 'enable')
        ], limit=1)
        
        if not whatsapp_instance:
            raise UserError(_(
                "No active WhatsApp instance found.\n\n"
                "Please configure WhatsApp in Settings > Technical > WhatsApp > WhatsApp Instance."
            ))
        
        # Open send wizard
        return {
            'name': _('Send Quotation via WhatsApp'),
            'type': 'ir.actions.act_window',
            'res_model': 'send.whatsapp.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_sale_order_id': self.id,
                'default_partner_id': self.partner_id.id,
                'default_mobile': self.partner_id.phone,
            }
        }

    def _send_whatsapp_notification(self, template_name, additional_context=None):
        """
        Helper method to send WhatsApp notification using pragtech_whatsapp_base
        
        Args:
            template_name: Name of WhatsApp template to use
            additional_context: Additional context for template rendering
        
        Returns:
            bool: True if sent successfully, False otherwise
        """
        self.ensure_one()
        
        if not self.partner_id.phone:
            _logger.warning("Cannot send WhatsApp to %s - no phone number", self.partner_id.name)
            return False
        
        try:
            # Get active WhatsApp instance
            whatsapp_instance = self.env['whatsapp.instance'].search([
                ('status', '=', 'enable')
            ], limit=1)
            
            if not whatsapp_instance:
                _logger.error("No active WhatsApp instance found")
                return False
            
            # Find template
            template = self.env['whatsapp.templates'].search([
                ('name', '=', template_name),
                ('whatsapp_instance_id', '=', whatsapp_instance.id),
                ('approval_state', '=', 'approved'),
            ], limit=1)
            
            if not template:
                _logger.warning("WhatsApp template '%s' not found or not approved", template_name)
                return False
            
            # Prepare context for template
            context = {
                'order': self,
                'partner': self.partner_id,
                'company': self.company_id,
            }
            if additional_context:
                context.update(additional_context)
            
            # Send message via pragtech
            mobile = self.partner_id.phone
            message_body = self._render_whatsapp_template(template, context)
            
            # Use pragtech's send_template_message if available
            if hasattr(whatsapp_instance, 'send_template_message'):
                result = whatsapp_instance.send_template_message(
                    mobile_number=mobile,
                    template=template,
                    record=self,
                )
            else:
                # Fallback to basic send
                result = whatsapp_instance.send_message(
                    mobile_number=mobile,
                    message=message_body,
                )
            
            if result:
                _logger.info("WhatsApp sent to %s for SO %s", mobile, self.name)
                return True
            else:
                _logger.error("Failed to send WhatsApp to %s for SO %s", mobile, self.name)
                return False
                
        except Exception as e:
            _logger.error("Error sending WhatsApp for SO %s: %s", self.name, str(e))
            return False

    def _render_whatsapp_template(self, template, context):
        """
        Render WhatsApp template with context
        
        Args:
            template: whatsapp.templates record
            context: Dictionary with context variables
        
        Returns:
            str: Rendered message body
        """
        # Simple template rendering - replace placeholders
        message = template.sample_message or template.body or ""
        
        # Replace common placeholders
        replacements = {
            '{{customer_name}}': context.get('partner', self.env['res.partner']).name or '',
            '{{order_name}}': context.get('order', self).name or '',
            '{{order_amount}}': str(context.get('order', self).amount_total or 0),
            '{{company_name}}': context.get('company', self.env['res.company']).name or '',
        }
        
        for placeholder, value in replacements.items():
            message = message.replace(placeholder, value)
        
        return message

    def action_view_whatsapp_messages(self):
        """View WhatsApp messages sent for this order"""
        self.ensure_one()
        
        return {
            'name': _('WhatsApp Messages'),
            'type': 'ir.actions.act_window',
            'res_model': 'whatsapp.messages',
            'view_mode': 'tree,form',
            'domain': [
                '|',
                ('message', 'ilike', self.name),
                ('message', 'ilike', 'SO%s' % self.id),
            ],
            'context': {
                'default_name': self.partner_id.name,
            }
        }

    def action_confirm(self):
        """
        REQ-00027 Task 29: Override to send automatic WhatsApp notification
        """
        result = super(SaleOrder, self).action_confirm()
        
        # Check if auto-notify is enabled
        auto_notify = self.env['ir.config_parameter'].sudo().get_param(
            'smart_view_whatsapp.auto_notify_so_confirm', default=False
        )
        
        if auto_notify:
            for order in self:
                if order.partner_id.phone:
                    try:
                        order._send_whatsapp_notification('so_confirmation')
                    except Exception as e:
                        # Don't block SO confirmation if WhatsApp fails
                        _logger.warning(
                            "Failed to send WhatsApp notification for SO %s: %s",
                            order.name, str(e)
                        )
        
        return result

