# -*- coding: utf-8 -*-
{
    'name': 'Smart View - CRM Enhanced',
    'version': '19.0.1.0.0',
    'category': 'Sales/CRM',
    'summary': 'Enhanced CRM with custom fields and pipeline stages',
    'description': """
        Smart View CRM Enhancements
        ============================
        Customizations for CRM pipeline and lead management.
        
        Features:
        * Project location field in leads/opportunities
        * Custom pipeline stages (Site Visit, Technical Description, Client Approval)
        * Client approval workflow with accept/reject buttons
        * Rejection reason tracking
        * Prevent SO creation on rejection
        * Enhanced kanban tooltips
        
        Requirements Covered:
        * REQ-00037: Lead Custom Field (project_location)
        * REQ-00038: New Pipeline Stages with approval workflow
    """,
    'author': 'Smart View Development Team',
    'website': 'https://www.smartview.com',
    'license': 'LGPL-3',
    'depends': [
        'crm',
        'sale_crm',
    ],
    'data': [
        # Security
        'security/ir.model.access.csv',
        
        # Data
        'data/crm_stage_data.xml',
        
        # Wizards
        'wizard/rejection_reason_wizard_views.xml',
        
        # Views
        'views/crm_lead_views.xml',
        # 'views/crm_stage_views.xml',  # Temporarily disabled - Odoo 19 XPath compatibility
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}

