# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class ProjectProject(models.Model):
    _inherit = 'project.project'

    # REQ-00043: Auto-generate tasks
    auto_generate_tasks = fields.Boolean(
        string='Auto-Generate Tasks',
        default=True,
        help="Automatically generate tasks from templates when project is created"
    )
    
    use_standard_stages = fields.Boolean(
        string='Use Standard Stages',
        default=True,
        help="Use Smart View standard 5 stages"
    )
    
    task_template_ids = fields.Many2many(
        'project.task.template',
        string='Task Templates',
        help="Templates to use for generating tasks"
    )
    
    generated_tasks_count = fields.Integer(
        string='Generated Tasks',
        compute='_compute_generated_tasks_count',
        help="Number of tasks generated from templates"
    )

    @api.depends('task_ids.template_id')
    def _compute_generated_tasks_count(self):
        """Count tasks generated from templates"""
        for project in self:
            project.generated_tasks_count = len(project.task_ids.filtered('template_id'))

    @api.model
    def create(self, vals):
        """
        REQ-00043 Task 49 & 52: Auto-create stages and tasks
        """
        # Create project first
        project = super(ProjectProject, self).create(vals)
        
        # Task 49: Apply standard stages if requested and not a template
        if project.use_standard_stages and not project.is_template:
            project._apply_standard_stages()
        
        # Task 52: Auto-generate tasks if requested and not a template
        if project.auto_generate_tasks and not project.is_template:
            project._generate_tasks_from_templates()
        
        return project

    def _apply_standard_stages(self):
        """
        REQ-00043 Task 49: Apply Smart View standard 5 stages to project
        NOTE: Temporarily disabled for Odoo 19 compatibility
        """
        self.ensure_one()
        # TODO: Implement custom project stages for Odoo 19
        # Odoo 19 uses a different stage structure for projects
        pass

    def _generate_tasks_from_templates(self):
        """
        REQ-00043 Task 52: Generate tasks from templates
        """
        self.ensure_one()
        
        # Get task templates to use
        if self.task_template_ids:
            # Use specified templates
            templates = self.task_template_ids
        else:
            # Use all active standard templates
            templates = self.env['project.task.template'].search([
                ('active', '=', True),
                ('template_code', '!=', False),
            ], order='sequence')
        
        # Generate tasks from each template
        created_tasks = self.env['project.task']
        for template in templates:
            task = template.create_task_from_template(self)
            # Link task to template
            task.write({'template_id': template.id})
            created_tasks |= task
        
        return created_tasks

    def action_generate_tasks(self):
        """Manual action to generate tasks from templates"""
        self.ensure_one()
        
        # Count existing template tasks
        existing_count = len(self.task_ids.filtered('template_id'))
        
        if existing_count > 0:
            # Ask user if they want to regenerate
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': _('Tasks Already Generated'),
                    'message': _('This project already has %d tasks generated from templates.') % existing_count,
                    'type': 'warning',
                    'sticky': False,
                }
            }
        
        # Generate tasks
        created_tasks = self._generate_tasks_from_templates()
        
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _('Tasks Generated'),
                'message': _('%d tasks have been created from templates.') % len(created_tasks),
                'type': 'success',
                'sticky': False,
            }
        }

    def action_view_generated_tasks(self):
        """View tasks generated from templates"""
        self.ensure_one()
        
        template_tasks = self.task_ids.filtered('template_id')
        
        return {
            'name': _('Generated Tasks'),
            'type': 'ir.actions.act_window',
            'res_model': 'project.task',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', template_tasks.ids)],
            'context': {
                'default_project_id': self.id,
            }
        }

