# 📦 Module Structure Templates - Odoo 19

This document provides ready-to-use templates for each module's `__manifest__.py` file.

---

## 🎨 Module 1: smart_view_company_branding

```python
# -*- coding: utf-8 -*-
{
    'name': 'Smart View - Company Branding',
    'version': '19.0.1.0.0',
    'category': 'Customizations',
    'summary': 'Custom header and footer for company documents',
    'description': """
        Company Branding Customization
        ================================
        * Custom report header
        * Custom report footer
        * Professional document layout
        * Consistent branding across all reports
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'web',
        'sale_management',
    ],
    'data': [
        'report/external_layout_custom.xml',
        'report/report_templates.xml',
    ],
    'assets': {
        'web.report_assets_common': [
            'smart_view_company_branding/static/src/img/header.png',
            'smart_view_company_branding/static/src/img/footer.png',
        ],
    },
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
```

---

## 💼 Module 2: smart_view_sale_enhanced

```python
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
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
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
        'data/sale_order_states.xml',
        'data/quotation_templates.xml',
        
        # Views
        'views/sale_order_views.xml',
        'views/sale_order_line_views.xml',
        'views/product_template_views.xml',
        
        # Reports
        'report/sale_report_templates.xml',
        'report/quotation_template_standard.xml',
        'report/quotation_template_technical.xml',
        
        # Wizards
        'wizard/payment_validation_wizard_views.xml',
    ],
    'demo': [],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
```

---

## 💬 Module 3: smart_view_whatsapp

```python
# -*- coding: utf-8 -*-
{
    'name': 'Smart View - WhatsApp Integration',
    'version': '19.0.1.0.0',
    'category': 'Marketing',
    'summary': 'Send quotations and notifications via WhatsApp',
    'description': """
        WhatsApp Business Integration
        ==============================
        Features:
        * WhatsApp Business API integration
        * Meta Cloud API support
        * Send quotations via WhatsApp
        * Automated status notifications
        * Template message management
        * Message history tracking
        * Bulk messaging support
        
        Requirements Covered:
        * REQ-00027: WhatsApp Integration
        
        Configuration Required:
        * WhatsApp Business API credentials
        * Meta Cloud API access token
        * Phone number verification
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'license': 'LGPL-3',
    'depends': [
        'sale_management',
        'mail',
        'contacts',
    ],
    'external_dependencies': {
        'python': ['requests'],
    },
    'data': [
        # Security
        'security/ir.model.access.csv',
        'security/whatsapp_security.xml',
        
        # Data
        'data/whatsapp_templates.xml',
        'data/message_templates.xml',
        
        # Views
        'views/whatsapp_config_views.xml',
        'views/whatsapp_message_views.xml',
        'views/sale_order_views.xml',
        'views/res_partner_views.xml',
        
        # Wizards
        'wizard/send_whatsapp_wizard_views.xml',
        'wizard/bulk_whatsapp_wizard_views.xml',
    ],
    'demo': [],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
```

---

## 🎯 Module 4: smart_view_crm_enhanced

```python
# -*- coding: utf-8 -*-
{
    'name': 'Smart View - CRM Enhanced',
    'version': '19.0.1.0.0',
    'category': 'Sales/CRM',
    'summary': 'Enhanced CRM with custom pipeline and approval workflow',
    'description': """
        CRM & Sales Pipeline Enhancements
        ==================================
        Features:
        * Project location field on leads
        * Custom pipeline stages:
          - Site Visit
          - Technical Description
          - Client Approval
        * Approval/Rejection workflow
        * Rejection reason wizard
        * Block SO creation on rejection
        * Enhanced Kanban tooltips
        * Stage validation logic
        
        Requirements Covered:
        * REQ-00037: Lead Custom Field (project_location)
        * REQ-00038: New Pipeline Stages with Approval
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'license': 'LGPL-3',
    'depends': [
        'crm',
        'sale_crm',
    ],
    'data': [
        # Security
        'security/ir.model.access.csv',
        
        # Data
        'data/crm_stages.xml',
        
        # Views
        'views/crm_lead_views.xml',
        'views/crm_stage_views.xml',
        
        # Wizards
        'wizard/rejection_reason_wizard_views.xml',
        'wizard/approval_wizard_views.xml',
    ],
    'demo': [],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
```

---

## 🔗 Module 5: smart_view_project_sale

```python
# -*- coding: utf-8 -*-
{
    'name': 'Smart View - Project Sale Bridge',
    'version': '19.0.1.0.0',
    'category': 'Services/Project',
    'summary': 'Create projects from sales orders after client approval',
    'description': """
        Sales Order to Project Bridge
        ==============================
        Features:
        * "Create Project" button in sale orders
        * Stage validation (only after client approval)
        * Project template selection
        * Automated field mapping (SO → Project)
        * Project-SO linking
        * Customer information propagation
        * Prevent duplicate project creation
        
        Requirements Covered:
        * REQ-00042: Project Creation from SO
        
        Dependencies:
        * Requires smart_view_crm_enhanced for approval stages
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'license': 'LGPL-3',
    'depends': [
        'sale_management',
        'project',
        'smart_view_crm_enhanced',  # For approval stage validation
    ],
    'data': [
        # Security
        'security/ir.model.access.csv',
        
        # Views
        'views/sale_order_views.xml',
        'views/project_project_views.xml',
        
        # Wizards
        'wizard/create_project_wizard_views.xml',
    ],
    'demo': [],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
```

---

## 📋 Module 6: smart_view_project_enhanced

```python
# -*- coding: utf-8 -*-
{
    'name': 'Smart View - Project Enhanced',
    'version': '19.0.1.0.0',
    'category': 'Services/Project',
    'summary': 'Project templates with automated stages and tasks',
    'description': """
        Project Workflow & Task Automation
        ===================================
        Features:
        * Project templates with predefined stages:
          - دراسة (Study)
          - توريد (Supply)
          - تركيب (Installation)
          - تسليم (Delivery)
          - خدمة ما بعد البيع (After-sales Service)
        
        * Task templates:
          - تركيب (Installation)
          - برمجة (Programming)
          - اختبار (Testing)
          - تسليم نهائي (Final Delivery)
        
        * Locked stages (prevent deletion/reorder)
        * Auto-generate tasks from templates
        * Task dependencies (optional)
        * Project workflow automation
        * Template configuration UI
        
        Requirements Covered:
        * REQ-00043: Project Customizations (Stages & Tasks)
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'license': 'LGPL-3',
    'depends': [
        'project',
    ],
    'data': [
        # Security
        'security/ir.model.access.csv',
        
        # Data - Load in specific order
        'data/project_stage_templates.xml',
        'data/project_task_templates.xml',
        'data/default_project_templates.xml',
        
        # Views
        'views/project_project_views.xml',
        'views/project_task_views.xml',
        'views/project_stage_template_views.xml',
        'views/project_task_template_views.xml',
        'views/project_template_views.xml',
        
        # Menu
        'views/menu_views.xml',
    ],
    'demo': [],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
```

---

## 🎫 Module 7: smart_view_helpdesk

```python
# -*- coding: utf-8 -*-
{
    'name': 'Smart View - Helpdesk',
    'version': '19.0.1.0.0',
    'category': 'Services/Helpdesk',
    'summary': 'Simple helpdesk module for customer support',
    'description': """
        Helpdesk Module Activation
        ===========================
        Features:
        * Basic ticket management
        * Helpdesk menu visibility
        * Access rights configuration
        * Team management
        * SLA tracking (basic)
        
        Requirements Covered:
        * REQ-00036: Helpdesk Activation
        
        Note: This is a lightweight implementation for Odoo Community.
        For enterprise features, consider upgrading to Odoo Enterprise
        or using OCA helpdesk_mgmt module.
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'license': 'LGPL-3',
    'depends': [
        'mail',
        'portal',
    ],
    'data': [
        # Security
        'security/helpdesk_security.xml',
        'security/ir.model.access.csv',
        
        # Views
        'views/helpdesk_ticket_views.xml',
        'views/helpdesk_team_views.xml',
        
        # Menu
        'views/helpdesk_menu.xml',
    ],
    'demo': [],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,  # Show as separate app
    'auto_install': False,
}
```

---

## 🔧 Module 8 (Optional): smart_view_base

```python
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
        * Settings access configuration
        * Shared Python utilities
        * Common JavaScript assets
        * Base configurations
        
        Requirements Covered:
        * REQ-00018: User Permissions (Settings group)
        
        Note: This module is optional. Only install if you need
        shared utilities across multiple Smart View modules.
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'web',
    ],
    'data': [
        # Security
        'security/security_groups.xml',
        'security/ir.model.access.csv',
        
        # Views
        'views/res_users_views.xml',
    ],
    'demo': [],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
```

---

## 📝 Common Fields for All Manifests

### Version Numbering
Format: `MAJOR.MINOR.PATCH.BUILD`
- `19.0` = Odoo version
- `1.0.0` = Module version

### License Options
- `LGPL-3` - Most common for Odoo Community
- `OPL-1` - Odoo Proprietary License (if needed)
- `GPL-3` - Full open source

### Categories
Standard Odoo categories:
- `Sales`
- `Sales/CRM`
- `Services/Project`
- `Services/Helpdesk`
- `Marketing`
- `Customizations`

### Images
Each module should have:
- `static/description/icon.png` (256x256)
- `static/description/banner.png` (560x280) - optional
- `static/description/screenshot_*.png` - optional

---

## 🔄 Installation Order

Due to dependencies, install in this order:

```bash
# Phase 1: Base (optional)
odoo-bin -d your_db -i smart_view_base --stop-after-init

# Phase 2: Independent modules
odoo-bin -d your_db -i smart_view_company_branding --stop-after-init
odoo-bin -d your_db -i smart_view_sale_enhanced --stop-after-init

# Phase 3: CRM (depends on base modules)
odoo-bin -d your_db -i smart_view_crm_enhanced --stop-after-init

# Phase 4: Projects (depends on CRM)
odoo-bin -d your_db -i smart_view_project_enhanced --stop-after-init
odoo-bin -d your_db -i smart_view_project_sale --stop-after-init

# Phase 5: Integrations
odoo-bin -d your_db -i smart_view_whatsapp --stop-after-init
odoo-bin -d your_db -i smart_view_helpdesk --stop-after-init
```

Or install all at once (Odoo will resolve dependencies):

```bash
odoo-bin -d your_db -i smart_view_base,smart_view_company_branding,smart_view_sale_enhanced,smart_view_crm_enhanced,smart_view_project_enhanced,smart_view_project_sale,smart_view_whatsapp,smart_view_helpdesk --stop-after-init
```

---

## 🧹 Uninstallation

To uninstall, reverse the order:

```bash
# Remove dependent modules first
odoo-bin -d your_db -u smart_view_whatsapp,smart_view_helpdesk --stop-after-init

# Then project modules
odoo-bin -d your_db -u smart_view_project_sale,smart_view_project_enhanced --stop-after-init

# Then CRM
odoo-bin -d your_db -u smart_view_crm_enhanced --stop-after-init

# Finally base modules
odoo-bin -d your_db -u smart_view_sale_enhanced,smart_view_company_branding,smart_view_base --stop-after-init
```

---

**Document Version:** 1.0  
**Last Updated:** 2025-11-19  
**Odoo Version:** 19.0 Community

