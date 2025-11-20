# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProjectTaskTemplate(models.Model):
    _name = 'project.task.template'
    _description = 'Project Task Template'
    _order = 'sequence, name'

    name = fields.Char(
        string='Task Name',
        required=True,
        translate=True,
        help="Name of the task to be created"
    )
    
    sequence = fields.Integer(
        string='Sequence',
        default=10,
        help="Order of task creation"
    )
    
    description = fields.Html(
        string='Description',
        translate=True,
        help="Detailed task description"
    )
    
    template_code = fields.Char(
        string='Template Code',
        help="Unique code for identifying standard templates"
    )
    
    planned_hours = fields.Float(
        string='Planned Hours',
        help="Estimated hours for this task"
    )
    
    user_id = fields.Many2one(
        'res.users',
        string='Assigned To',
        help="Default assignee for this task (can be changed)"
    )
    
    stage_id = fields.Many2one(
        'project.task.type',
        string='Default Stage',
        help="Initial stage for this task"
    )
    
    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Normal'),
        ('2', 'High'),
        ('3', 'Urgent'),
    ], string='Priority', default='1')
    
    active = fields.Boolean(
        string='Active',
        default=True,
        help="If unchecked, this template won't be used for new projects"
    )
    
    tag_ids = fields.Many2many(
        'project.tags',
        string='Tags',
        help="Tags to apply to created tasks"
    )
    
    notes = fields.Text(
        string='Notes',
        help="Internal notes about this template"
    )

    def name_get(self):
        """Display template code in name if available"""
        result = []
        for template in self:
            if template.template_code:
                name = f"[{template.template_code}] {template.name}"
            else:
                name = template.name
            result.append((template.id, name))
        return result

    def create_task_from_template(self, project):
        """Create a task in the given project from this template"""
        self.ensure_one()
        
        task_vals = {
            'name': self.name,
            'project_id': project.id,
            'description': self.description or '',
            'planned_hours': self.planned_hours or 0.0,
            'user_ids': [(6, 0, [self.user_id.id])] if self.user_id else False,
            'priority': self.priority,
            'tag_ids': [(6, 0, self.tag_ids.ids)] if self.tag_ids else False,
        }
        
        # Set stage if available
        if self.stage_id:
            task_vals['stage_id'] = self.stage_id.id
        
        # Set partner from project
        if project.partner_id:
            task_vals['partner_id'] = project.partner_id.id
        
        task = self.env['project.task'].create(task_vals)
        return task

