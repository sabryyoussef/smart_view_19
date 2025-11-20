# -*- coding: utf-8 -*-
{
    'name': 'Smart View - Base',
    'version': '19.0.1.0.0',
    'category': 'Customizations',
    'summary': 'Base module for Smart View customizations',
    'description': """
        Smart View Base Module
        ======================
        Common utilities and configurations for Smart View modules.
        
        Features:
        * Custom security groups
        * Enhanced settings access
        * User permission management
        * Shared Python utilities
        * Common configurations
        
        Requirements Covered:
        * REQ-00018: User Permissions (Settings group for specific users)
        
        Note: This module is optional but provides shared functionality
        for other Smart View modules. Install first if using multiple modules.
    """,
    'author': 'Sabry Youssef',
    'maintainer': 'Sabry Youssef',
    'website': 'mailto:vendorah2@gmail.com',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'web',
    ],
    'data': [
        # Security
        'security/base_security.xml',
        'security/ir.model.access.csv',
        
        # Views
        'views/res_users_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}

