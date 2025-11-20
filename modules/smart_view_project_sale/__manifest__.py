# -*- coding: utf-8 -*-
{
    'name': 'Smart View - Project Sale Integration',
    'version': '19.0.1.0.0',
    'category': 'Sales/Projects',
    'summary': 'Create projects from sales orders with approval validation',
    'description': """
        Smart View Project-Sale Integration
        ====================================
        Bridge between Sales Orders and Projects with CRM approval integration.
        
        Features:
        * Manual "Create Project" button in Sales Orders
        * Client approval validation from CRM
        * Project creation from templates
        * Enhanced SO-Project linking
        * Automatic field mapping (project location, customer, etc.)
        * Project template selection
        * Bi-directional linking
        
        Requirements Covered:
        * REQ-00042: Project Creation from SO (Tasks 45-48)
          - Task 45: Create Project button
          - Task 46: Link to Client Approval state
          - Task 47: Create from template
          - Task 48: Enhanced SO-Project linking
    """,
    'author': 'Sabry Youssef',
    'maintainer': 'Sabry Youssef',
    'website': 'mailto:vendorah2@gmail.com',
    'license': 'LGPL-3',
    'depends': [
        'sale_management',
        'project',
        'sale_project',  # For basic SO-Project integration
        'smart_view_crm_enhanced',  # For approval validation
        'smart_view_project_enhanced',  # For project templates and stages
    ],
    'data': [
        # Security
        'security/ir.model.access.csv',
        
        # Views
        'views/sale_order_views.xml',
        'views/project_project_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}

