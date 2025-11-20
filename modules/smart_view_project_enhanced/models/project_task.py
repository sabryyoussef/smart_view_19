# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProjectTask(models.Model):
    _inherit = 'project.task'

    template_id = fields.Many2one(
        'project.task.template',
        string='Created From Template',
        readonly=True,
        help="Template used to create this task"
    )
    
    is_template_task = fields.Boolean(
        string='Template Task',
        compute='_compute_is_template_task',
        store=True,
        help="Indicates if this task was created from a template"
    )

    @api.depends('template_id')
    def _compute_is_template_task(self):
        """Check if task was created from template"""
        for task in self:
            task.is_template_task = bool(task.template_id)

