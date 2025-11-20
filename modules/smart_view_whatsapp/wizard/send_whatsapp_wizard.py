# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError
import logging
import re

_logger = logging.getLogger(__name__)


class SendWhatsappWizard(models.TransientModel):
    _name = 'send.whatsapp.wizard'
    _description = 'Send WhatsApp Message Wizard'

    sale_order_id = fields.Many2one(
        'sale.order',
        string='Sales Order',
        required=True,
        ondelete='cascade'
    )
    
    partner_id = fields.Many2one(
        'res.partner',
        string='Customer',
        required=True
    )
    
    mobile = fields.Char(
        string='Mobile Number',
        required=True,
        help="Customer's WhatsApp number"
    )
    
    whatsapp_instance_id = fields.Many2one(
        'whatsapp.instance',
        string='WhatsApp Instance',
        domain=[('status', '=', 'enable')],
        help="WhatsApp instance to use for sending"
    )
    
    message_type = fields.Selection([
        ('quotation', 'Send Quotation'),
        ('confirmation', 'Order Confirmation'),
        ('custom', 'Custom Message'),
    ], string='Message Type', default='quotation', required=True)
    
    use_template = fields.Boolean(
        string='Use Template',
        default=True,
        help="Use WhatsApp template message (recommended for Meta)"
    )
    
    template_id = fields.Many2one(
        'whatsapp.templates',
        string='Template',
        domain="[('whatsapp_instance_id', '=', whatsapp_instance_id), ('approval_state', '=', 'approved')]"
    )
    
    message = fields.Text(
        string='Message',
        required=True,
        default=lambda self: self._default_message()
    )
    
    attach_pdf = fields.Boolean(
        string='Attach Quotation PDF',
        default=True,
        help="Attach quotation PDF to WhatsApp message"
    )
    
    mobile_valid = fields.Boolean(
        string='Mobile Valid',
        compute='_compute_mobile_valid',
        help="Check if mobile number is valid"
    )

    @api.model
    def _default_message(self):
        """Generate default message based on context"""
        sale_order_id = self.env.context.get('default_sale_order_id')
        if sale_order_id:
            order = self.env['sale.order'].browse(sale_order_id)
            return _(
                "Dear %s,\n\n"
                "Please find attached your quotation %s.\n\n"
                "Total Amount: %s %s\n\n"
                "We look forward to working with you!\n\n"
                "Best regards,\n%s"
            ) % (
                order.partner_id.name,
                order.name,
                order.amount_total,
                order.currency_id.name,
                order.company_id.name
            )
        return ""

    @api.depends('mobile')
    def _compute_mobile_valid(self):
        """Validate mobile number format"""
        for wizard in self:
            valid = False
            if wizard.mobile:
                # Remove spaces and special chars
                clean_mobile = re.sub(r'[^\d+]', '', wizard.mobile)
                # Check if it looks like a phone number (at least 8 digits)
                if len(re.sub(r'[^\d]', '', clean_mobile)) >= 8:
                    valid = True
            wizard.mobile_valid = valid

    @api.onchange('whatsapp_instance_id')
    def _onchange_whatsapp_instance(self):
        """Update template domain when instance changes"""
        if self.whatsapp_instance_id:
            # Try to find default quotation template
            template = self.env['whatsapp.templates'].search([
                ('whatsapp_instance_id', '=', self.whatsapp_instance_id.id),
                ('name', '=', 'quotation_template'),
                ('approval_state', '=', 'approved'),
            ], limit=1)
            if template:
                self.template_id = template

    @api.onchange('message_type')
    def _onchange_message_type(self):
        """Update message when type changes"""
        if self.message_type == 'quotation':
            self.message = self._default_message()
        elif self.message_type == 'confirmation':
            self.message = _(
                "Dear %s,\n\n"
                "Your order %s has been confirmed!\n\n"
                "We will start processing it shortly.\n\n"
                "Thank you for your business!\n\n"
                "Best regards,\n%s"
            ) % (
                self.partner_id.name,
                self.sale_order_id.name,
                self.sale_order_id.company_id.name
            )

    def action_send_whatsapp(self):
        """
        REQ-00027 Tasks 27-29: Send WhatsApp message
        """
        self.ensure_one()
        
        # Validate mobile number
        if not self.mobile_valid:
            raise UserError(_(
                "Invalid mobile number: %s\n\n"
                "Please enter a valid WhatsApp number."
            ) % self.mobile)
        
        # Get or validate WhatsApp instance
        if not self.whatsapp_instance_id:
            self.whatsapp_instance_id = self.env['whatsapp.instance'].search([
                ('status', '=', 'enable')
            ], limit=1)
        
        if not self.whatsapp_instance_id:
            raise UserError(_(
                "No active WhatsApp instance found.\n\n"
                "Please configure WhatsApp in Settings > Technical > WhatsApp."
            ))
        
        try:
            # Prepare attachment if needed
            attachment = None
            if self.attach_pdf:
                attachment = self._generate_quotation_pdf()
            
            # Send message
            if self.use_template and self.template_id:
                # Send via template (for Meta)
                result = self._send_template_message(attachment)
            else:
                # Send direct message (for 1msg/Gupshup)
                result = self._send_direct_message(attachment)
            
            if result:
                # Mark SO as sent
                self.sale_order_id.write({
                    'whatsapp_sent': True,
                    'whatsapp_sent_date': fields.Datetime.now(),
                })
                
                # Success notification
                return {
                    'type': 'ir.actions.client',
                    'tag': 'display_notification',
                    'params': {
                        'title': _('WhatsApp Sent!'),
                        'message': _('Quotation sent successfully to %s') % self.mobile,
                        'type': 'success',
                        'sticky': False,
                    }
                }
            else:
                raise UserError(_("Failed to send WhatsApp message. Please check the logs."))
                
        except Exception as e:
            _logger.error("Error sending WhatsApp: %s", str(e))
            raise UserError(_(
                "Error sending WhatsApp message:\n\n%s\n\n"
                "Please check your WhatsApp configuration and try again."
            ) % str(e))

    def _send_template_message(self, attachment=None):
        """Send message using WhatsApp template"""
        try:
            # Use pragtech's template send method
            result = self.whatsapp_instance_id.send_template_message(
                mobile_number=self.mobile,
                template=self.template_id,
                record=self.sale_order_id,
            )
            
            # Send attachment separately if needed
            if attachment and result:
                self.whatsapp_instance_id.send_document(
                    mobile_number=self.mobile,
                    document=attachment,
                    caption=_("Quotation %s") % self.sale_order_id.name,
                )
            
            return result
            
        except Exception as e:
            _logger.error("Error sending template message: %s", str(e))
            return False

    def _send_direct_message(self, attachment=None):
        """Send direct message (non-template)"""
        try:
            # Clean mobile number
            mobile = re.sub(r'[^\d+]', '', self.mobile)
            
            # Send message
            if hasattr(self.whatsapp_instance_id, 'send_message'):
                result = self.whatsapp_instance_id.send_message(
                    mobile_number=mobile,
                    message=self.message,
                )
            else:
                # Fallback method
                _logger.warning("send_message method not found, using alternative")
                return False
            
            # Send attachment if available
            if attachment and result:
                if hasattr(self.whatsapp_instance_id, 'send_document'):
                    self.whatsapp_instance_id.send_document(
                        mobile_number=mobile,
                        document=attachment,
                        caption=_("Quotation %s") % self.sale_order_id.name,
                    )
            
            return result
            
        except Exception as e:
            _logger.error("Error sending direct message: %s", str(e))
            return False

    def _generate_quotation_pdf(self):
        """Generate quotation PDF"""
        try:
            # Get quotation report
            report = self.env.ref('sale.action_report_saleorder')
            
            # Generate PDF
            pdf_content, content_type = report._render_qweb_pdf([self.sale_order_id.id])
            
            # Create attachment
            attachment = self.env['ir.attachment'].create({
                'name': '%s.pdf' % self.sale_order_id.name,
                'type': 'binary',
                'datas': pdf_content,
                'res_model': 'sale.order',
                'res_id': self.sale_order_id.id,
                'mimetype': 'application/pdf',
            })
            
            return attachment
            
        except Exception as e:
            _logger.error("Error generating PDF: %s", str(e))
            return None

