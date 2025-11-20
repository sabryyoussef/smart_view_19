# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    # WhatsApp Automation Settings
    auto_notify_so_confirm = fields.Boolean(
        string='Auto-notify on SO Confirmation',
        config_parameter='smart_view_whatsapp.auto_notify_so_confirm',
        help="Automatically send WhatsApp notification when Sales Order is confirmed"
    )
    
    auto_notify_project_create = fields.Boolean(
        string='Auto-notify on Project Creation',
        config_parameter='smart_view_whatsapp.auto_notify_project_create',
        help="Automatically send WhatsApp notification when Project is created from SO"
    )
    
    auto_notify_payment_received = fields.Boolean(
        string='Auto-notify on Payment',
        config_parameter='smart_view_whatsapp.auto_notify_payment_received',
        help="Automatically send WhatsApp notification when payment is received"
    )
    
    whatsapp_quotation_template = fields.Char(
        string='Quotation Template Name',
        config_parameter='smart_view_whatsapp.quotation_template',
        default='quotation_template',
        help="Name of WhatsApp template to use for sending quotations"
    )
    
    whatsapp_so_confirm_template = fields.Char(
        string='SO Confirmation Template Name',
        config_parameter='smart_view_whatsapp.so_confirm_template',
        default='so_confirmation',
        help="Name of WhatsApp template to use for SO confirmation notifications"
    )
    
    whatsapp_project_template = fields.Char(
        string='Project Creation Template Name',
        config_parameter='smart_view_whatsapp.project_template',
        default='project_created',
        help="Name of WhatsApp template to use for project creation notifications"
    )

