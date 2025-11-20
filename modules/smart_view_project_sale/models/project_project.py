# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProjectProject(models.Model):
    _inherit = 'project.project'

    # REQ-00042 Task 48: Enhanced SO linking
    sale_order_id = fields.Many2one(
        'sale.order',
        string='Sales Order',
        copy=False,
        help="Sales order that created this project"
    )
    
    # REQ-00042 Task 48: Project location from CRM
    project_location = fields.Char(
        string='Project Location',
        help="Location where the project will be executed (from CRM opportunity)"
    )
    
    # Template support for Task 47
    is_template = fields.Boolean(
        string='Is Template',
        default=False,
        help="Check if this project is a template for creating new projects"
    )
    
    template_name = fields.Char(
        string='Template Name',
        help="Name of this template (for easy selection)"
    )

    def name_get(self):
        """Override to show template indicator"""
        result = []
        for project in self:
            if project.is_template:
                name = f"[TEMPLATE] {project.name}"
            else:
                name = project.name
            result.append((project.id, name))
        return result

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        """Improve search for templates"""
        args = args or []
        if name:
            # Search in both name and template_name
            domain = ['|', ('name', operator, name), ('template_name', operator, name)]
            return self._search(domain + args, limit=limit, access_rights_uid=name_get_uid)
        return super(ProjectProject, self)._name_search(name, args, operator, limit, name_get_uid)

