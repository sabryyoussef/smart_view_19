# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # REQ-00042: Enhanced project linking
    project_id = fields.Many2one(
        'project.project',
        string='Project',
        copy=False,
        help="Project created from this sales order"
    )
    
    project_count = fields.Integer(
        string='Project Count',
        compute='_compute_project_count',
        help="Number of projects linked to this SO"
    )
    
    can_create_project = fields.Boolean(
        string='Can Create Project',
        compute='_compute_can_create_project',
        help="Indicates if project can be created from this SO"
    )
    
    project_template_id = fields.Many2one(
        'project.project',
        string='Project Template',
        domain="[('is_template', '=', True)]",
        help="Template to use for project creation"
    )

    @api.depends('project_id')
    def _compute_project_count(self):
        """Count linked projects"""
        for order in self:
            order.project_count = 1 if order.project_id else 0

    @api.depends('state', 'opportunity_id', 'opportunity_id.client_approval_state', 'project_id')
    def _compute_can_create_project(self):
        """
        REQ-00042 Task 46: Check if project can be created
        Requires:
        - SO is confirmed (sale state)
        - No existing project
        - If linked to opportunity, must be approved
        """
        for order in self:
            can_create = False
            
            # Must be in sale or done state
            if order.state in ['sale', 'done']:
                # No existing project
                if not order.project_id:
                    # Check opportunity approval if linked
                    if order.opportunity_id:
                        # Must be in approved state
                        if order.opportunity_id.client_approval_state == 'approved':
                            can_create = True
                    else:
                        # No opportunity link, allow creation
                        can_create = True
            
            order.can_create_project = can_create

    def action_create_project(self):
        """
        REQ-00042: Create project from sales order
        Tasks 45-48 implementation
        """
        self.ensure_one()
        
        # Task 46: Validate client approval
        self._validate_project_creation()
        
        # Task 47: Create project from template (if specified) or new
        project = self._create_project_from_so()
        
        # Task 48: Link project to SO
        self.write({'project_id': project.id})
        
        # Open the created project
        return {
            'name': _('Project'),
            'type': 'ir.actions.act_window',
            'res_model': 'project.project',
            'res_id': project.id,
            'view_mode': 'form',
            'target': 'current',
        }

    def _validate_project_creation(self):
        """
        REQ-00042 Task 46: Validate approval state before creating project
        """
        self.ensure_one()
        
        # Check SO state
        if self.state not in ['sale', 'done']:
            raise UserError(_(
                "Cannot create project. Sales order must be confirmed first.\n\n"
                "Current State: %s"
            ) % dict(self._fields['state'].selection).get(self.state))
        
        # Check if project already exists
        if self.project_id:
            raise UserError(_(
                "A project already exists for this sales order.\n\n"
                "Project: %s"
            ) % self.project_id.name)
        
        # Task 46: Check CRM approval if opportunity is linked
        if self.opportunity_id:
            approval_state = self.opportunity_id.client_approval_state
            
            if not approval_state or approval_state == 'pending':
                raise UserError(_(
                    "Cannot create project. Client approval is pending.\n\n"
                    "The linked opportunity must be approved by the client before creating a project.\n"
                    "Please go to the opportunity and click 'Client Approved' button."
                ))
            
            if approval_state == 'rejected':
                raise UserError(_(
                    "Cannot create project. Client has rejected the opportunity.\n\n"
                    "Rejection Reason: %s\n\n"
                    "Please revise the proposal or create a new opportunity."
                ) % (self.opportunity_id.rejection_reason or 'No reason provided'))
            
            # If we reach here, approval_state is 'approved' - proceed
        
        return True

    def _create_project_from_so(self):
        """
        REQ-00042 Task 47-48: Create project with template support
        """
        self.ensure_one()
        
        # Prepare project values
        project_vals = self._prepare_project_values()
        
        # Task 47: If template specified, copy from template
        if self.project_template_id:
            project = self.project_template_id.copy(default=project_vals)
        else:
            # Create new project
            project = self.env['project.project'].create(project_vals)
        
        return project

    def _prepare_project_values(self):
        """
        REQ-00042 Task 48: Prepare project values with field mapping
        """
        self.ensure_one()
        
        # Base values
        values = {
            'name': _('Project - %s') % self.name,
            'partner_id': self.partner_id.id,
            'user_id': self.user_id.id,
            'company_id': self.company_id.id,
            'sale_order_id': self.id,
            'sale_line_id': False,  # SO-level project, not line-level
        }
        
        # Task 48: Copy project_location from CRM opportunity if available
        if self.opportunity_id and self.opportunity_id.project_location:
            values['project_location'] = self.opportunity_id.project_location
        
        # Copy other relevant fields
        if self.date_order:
            values['date_start'] = self.date_order.date()
        
        # Add notes with SO reference
        notes = _("Project created from Sales Order: %s\n") % self.name
        if self.opportunity_id:
            notes += _("Linked Opportunity: %s\n") % self.opportunity_id.name
            if self.opportunity_id.project_location:
                notes += _("Project Location: %s\n") % self.opportunity_id.project_location
        values['description'] = notes
        
        return values

    def action_view_project(self):
        """View linked project"""
        self.ensure_one()
        
        if not self.project_id:
            return False
        
        return {
            'name': _('Project'),
            'type': 'ir.actions.act_window',
            'res_model': 'project.project',
            'res_id': self.project_id.id,
            'view_mode': 'form',
            'target': 'current',
        }

