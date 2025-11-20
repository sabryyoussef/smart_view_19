# -*- coding: utf-8 -*-
{
    'name': 'Smart View - WhatsApp Integration',
    'version': '19.0.1.0.0',
    'category': 'Sales/CRM',
    'summary': 'Send quotations and notifications via WhatsApp using Pragtech base',
    'description': """
        Smart View WhatsApp Integration
        ================================
        Business logic wrapper for pragtech_whatsapp_base module.
        
        Features:
        * Send quotations via WhatsApp from Sales Orders
        * Automated notifications on SO confirmation
        * Automated notifications on payment received
        * Automated notifications on project creation
        * Phone number validation
        * Quotation template management
        * Integration with Smart View workflow
        
        Requirements Covered:
        * REQ-00027: WhatsApp Integration (Tasks 27-29)
          - Task 27: WhatsApp API (via pragtech_whatsapp_base)
          - Task 28: Template messages
          - Task 29: Meta Cloud API (via pragtech_whatsapp_base)
        
        Dependencies:
        * Requires: pragtech_whatsapp_base (infrastructure)
        * Integrates: smart_view_sale_enhanced
        * Integrates: smart_view_crm_enhanced
        * Integrates: smart_view_project_sale
    """,
    'author': 'Sabry Youssef',
    'maintainer': 'Sabry Youssef',
    'website': 'mailto:vendorah2@gmail.com',
    'license': 'LGPL-3',
    'depends': [
        # 'pragtech_whatsapp_base',      # WhatsApp infrastructure - Install separately if needed
        'sale_management',              # Sales orders
        # 'smart_view_sale_enhanced',    # Our enhanced sales - Enable after sale_enhanced is stable
        # 'smart_view_crm_enhanced',     # CRM notifications - Enable after crm_enhanced is stable
        # 'smart_view_project_sale',     # Project creation notifications - Enable after project_sale is stable
    ],
    'data': [
        # Security
        'security/ir.model.access.csv',
        
        # Data (templates and automation)
        'data/whatsapp_templates_data.xml',
        'data/automated_actions.xml',
        
        # Views
        # 'views/sale_order_views.xml',  # Disabled - Module not installable without pragtech_whatsapp_base
        # 'views/res_config_settings_views.xml',  # Temporarily disabled - Odoo 19 compatibility
        
        # Wizards
        # 'wizard/send_whatsapp_wizard_views.xml',  # Disabled - Module not installable without pragtech_whatsapp_base
    ],
    'demo': [],
    'images': ['static/description/icon.png'],
    'installable': False,  # Requires pragtech_whatsapp_base - Install separately
    'application': False,
    'auto_install': False,
}

