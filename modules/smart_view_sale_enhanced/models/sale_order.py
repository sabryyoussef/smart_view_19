# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # REQ-00017: Quotation Create Date (editable)
    quotation_create_date = fields.Date(
        string='Quotation Create Date',
        default=fields.Date.context_today,
        copy=False,
        tracking=True,
        help="Date when the quotation was created. Can be manually adjusted if needed."
    )

    # REQ-00025: Total Discount
    total_discount = fields.Monetary(
        string='Total Discount',
        compute='_compute_total_discount',
        store=True,
        currency_field='currency_id',
        help="Total discount amount across all order lines"
    )

    total_discount_percent = fields.Float(
        string='Total Discount %',
        compute='_compute_total_discount',
        store=True,
        help="Total discount percentage"
    )

    # REQ-00026: Pre-confirmation State
    state = fields.Selection(
        selection_add=[
            ('pending_payment', 'Pending Payment'),
        ],
        ondelete={'pending_payment': 'cascade'}
    )

    payment_validated = fields.Boolean(
        string='Payment Validated',
        default=False,
        copy=False,
        tracking=True,
        help="Indicates if down payment has been received"
    )

    # REQ-00023: Quotation Template Type
    quotation_template_type = fields.Selection([
        ('standard', 'Standard (with prices)'),
        ('technical', 'Technical (without prices)'),
    ], string='Quotation Template Type', default='standard',
        help="Select template type for printing quotations")

    @api.depends('order_line.discount', 'order_line.price_subtotal', 'order_line.price_unit', 'order_line.product_uom_qty')
    def _compute_total_discount(self):
        """Calculate total discount amount and percentage"""
        for order in self:
            total_discount = 0.0
            total_before_discount = 0.0
            
            for line in order.order_line:
                if line.discount > 0:
                    # Calculate price before discount
                    price_before_discount = line.price_unit * line.product_uom_qty
                    # Calculate discount amount
                    discount_amount = price_before_discount * (line.discount / 100.0)
                    total_discount += discount_amount
                    total_before_discount += price_before_discount
                else:
                    total_before_discount += line.price_unit * line.product_uom_qty
            
            order.total_discount = total_discount
            
            # Calculate percentage
            if total_before_discount > 0:
                order.total_discount_percent = (total_discount / total_before_discount) * 100.0
            else:
                order.total_discount_percent = 0.0

    # REQ-00026: Payment validation before confirmation
    def action_confirm(self):
        """Override to check payment validation before confirming"""
        for order in self:
            if order.state == 'pending_payment' and not order.payment_validated:
                raise UserError(_(
                    'Cannot confirm order "%s".\n'
                    'Please validate the down payment first.'
                ) % order.name)
        return super(SaleOrder, self).action_confirm()

    def action_set_pending_payment(self):
        """Move order to pending payment state"""
        self.ensure_one()
        if self.state in ['draft', 'sent']:
            self.write({'state': 'pending_payment'})
        return True

    def action_validate_payment(self):
        """Validate payment and allow confirmation"""
        self.ensure_one()
        self.write({
            'payment_validated': True,
        })
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _('Payment Validated'),
                'message': _('Payment has been validated. You can now confirm the order.'),
                'type': 'success',
                'sticky': False,
            }
        }

    # REQ-00020: Prevent SO creation message
    @api.model
    def create(self, vals):
        """Override create to show proper message"""
        order = super(SaleOrder, self).create(vals)
        # Message will be customized in the interface
        return order

    def copy(self, default=None):
        """Override copy to handle custom fields"""
        default = dict(default or {})
        default.update({
            'quotation_create_date': fields.Date.context_today(self),
            'payment_validated': False,
        })
        return super(SaleOrder, self).copy(default)

