# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    # REQ-00021: Internal Reference
    product_internal_ref = fields.Char(
        string='Internal Reference',
        related='product_id.default_code',
        readonly=True,
        store=False,
        help="Product internal reference code"
    )

    # REQ-00024: Enhanced discount visibility
    discount = fields.Float(
        string='Discount (%)',
        digits='Discount',
        default=0.0,
    )

    discount_amount = fields.Monetary(
        string='Discount Amount',
        compute='_compute_discount_amount',
        store=True,
        currency_field='currency_id',
        help="Calculated discount amount for this line"
    )

    @api.depends('product_uom_qty', 'price_unit', 'discount')
    def _compute_discount_amount(self):
        """Calculate discount amount for the line"""
        for line in self:
            if line.discount > 0:
                price_before_discount = line.price_unit * line.product_uom_qty
                line.discount_amount = price_before_discount * (line.discount / 100.0)
            else:
                line.discount_amount = 0.0

