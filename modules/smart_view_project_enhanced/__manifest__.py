# -*- coding: utf-8 -*-
{
    'name': 'Smart View - Project Enhanced',
    'version': '19.0.1.0.0',
    'category': 'Services/Project',
    'summary': 'Enhanced project management with custom stages and task templates',
    'description': """
        Smart View Project Enhancements
        ================================
        Advanced project workflow automation with custom stages and task templates.
        
        Features:
        * 5 custom project stages (in Arabic):
          - دراسة (Study)
          - توريد (Supply)
          - تركيب (Installation)
          - تسليم (Delivery)
          - خدمة ما بعد البيع (After-sales Service)
        * Locked stages (prevent accidental deletion)
        * Task templates:
          - تركيب (Installation)
          - برمجة (Programming)
          - اختبار (Testing)
          - تسليم نهائي (Final Delivery)
        * Automatic task generation from templates
        * Project workflow automation
        * Template-based project creation
        
        Requirements Covered:
        * REQ-00043: Project Customizations (Tasks 49-52)
          - Task 49: Create project with 5 stages
          - Task 50: Lock stages
          - Task 51: Create 4 task templates
          - Task 52: Auto-generate tasks
    """,
    'author': 'Smart View Development Team',
    'website': 'https://www.smartview.com',
    'license': 'LGPL-3',
    'depends': [
        'project',
    ],
    'data': [
        # Security
        'security/ir.model.access.csv',
        
        # Data (stages and templates)
        # 'data/project_stage_data.xml',  # Temporarily disabled - Odoo 19 compatibility
        'data/task_template_data.xml',
        
        # Views
        'views/project_project_views.xml',
        # 'views/project_stage_views.xml',  # Temporarily disabled - Odoo 19 compatibility
        'views/project_task_template_views.xml',
        'views/project_task_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}

