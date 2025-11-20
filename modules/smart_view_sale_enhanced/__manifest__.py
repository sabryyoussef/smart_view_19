# -*- coding: utf-8 -*-
{
    'name': 'Smart View - Sales Enhanced',
    'version': '19.0.1.0.0',
    'category': 'Sales',
    'summary': 'Enhanced sales order and quotation features',
    'description': """
        Sales Order & Quotation Enhancements
        ====================================
        Features:
        * Quotation create date field (editable)
        * Internal reference column in SO lines
        * Product image resize in reports (30% smaller)
        * Multiple quotation templates (Standard & Technical)
        * Enhanced discount visibility (line & total)
        * Total discount calculation field
        * Pre-confirmation state with payment validation
        * Product name full display fix
        * Prevent SO creation before payment confirmation
        
        Requirements Covered:
        * REQ-00017: Quotation Create Date
        * REQ-00019: Product Name Display
        * REQ-00020: Prevent SO Creation
        * REQ-00021: Internal Reference Column
        * REQ-00022: Product Image Resize
        * REQ-00023: Multiple Quotation Templates
        * REQ-00024: Line Discount Visibility
        * REQ-00025: Total Discount in SO
        * REQ-00026: Pre-Confirmation State
        * REQ-00039: Technical Quotation Template
    """,
    'author': 'Smart View Development Team',
    'website': 'https://www.smartview.com',
    'license': 'LGPL-3',
    'depends': [
        'sale_management',
        'product',
        'account',
    ],
    'data': [
        # Security
        'security/ir.model.access.csv',
        
        # Data
        # 'data/sale_order_states.xml',
        # 'data/quotation_templates.xml',
        
        # Views
        'views/sale_order_views.xml',
        # 'views/sale_order_line_views.xml',  # Temporarily disabled - Odoo 19 compatibility
        'views/product_template_views.xml',
        
        # Reports
        'report/sale_report_templates.xml',
        'report/quotation_template_standard.xml',
        'report/quotation_template_technical.xml',
        
        # Wizards
        # 'wizard/payment_validation_wizard_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}

