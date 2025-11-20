# -*- coding: utf-8 -*-
{
    'name': 'Smart View - Helpdesk Wrapper',
    'version': '19.0.1.0.0',
    'category': 'Services/Helpdesk',
    'summary': 'Helpdesk integration using OCA helpdesk_mgmt',
    'description': """
        Smart View Helpdesk Wrapper
        ============================
        This module wraps the OCA helpdesk_mgmt module to satisfy REQ-00036.
        
        Features:
        * Uses battle-tested OCA helpdesk_mgmt module
        * Ensures helpdesk is visible and accessible
        * Minimal wrapper for easy maintenance
        
        Requirements Covered:
        * REQ-00036: Helpdesk Activation
        
        Note: This is a wrapper module that depends on OCA's helpdesk_mgmt.
    """,
    'author': 'Sabry Youssef',
    'maintainer': 'Sabry Youssef',
    'website': 'mailto:vendorah2@gmail.com',
    'license': 'LGPL-3',
    'depends': [
        'helpdesk_mgmt',  # OCA Helpdesk Management
    ],
    'data': [
        # Just ensure visibility - the OCA module handles everything else
    ],
    'demo': [],
    'installable': True,
    'application': False,  # Not a separate app, just extends helpdesk_mgmt
    'auto_install': False,
}
