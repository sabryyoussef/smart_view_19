# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # REQ-00023 & REQ-00039: Quotation Description
    quotation_description = fields.Text(
        string='Quotation Description',
        translate=True,
        help="Description to show in quotations (used in technical template)"
    )

    # Enhanced for better display in reports
    # REQ-00019: Product name full display
    display_name = fields.Char(
        compute='_compute_display_name',
        store=False
    )

    def _compute_display_name(self):
        """Compute full display name for products"""
        for product in self:
            name = product.name or ''
            if product.default_code:
                name = f'[{product.default_code}] {name}'
            product.display_name = name

