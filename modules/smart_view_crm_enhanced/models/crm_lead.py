# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    # REQ-00037: Project Location Field
    project_location = fields.Char(
        string='Project Location',
        help="Location where the project will be executed",
        tracking=True,
    )

    # REQ-00038: Client Approval Fields
    client_approval_state = fields.Selection([
        ('pending', 'Pending Approval'),
        ('approved', 'Client Approved'),
        ('rejected', 'Client Rejected'),
    ], string='Client Approval Status', 
       default=False,
       tracking=True,
       help="Client approval status for this opportunity")

    rejection_reason = fields.Text(
        string='Rejection Reason',
        readonly=True,
        tracking=True,
        help="Reason provided by client for rejection"
    )

    rejection_date = fields.Datetime(
        string='Rejection Date',
        readonly=True,
        help="Date when the opportunity was rejected"
    )

    is_in_approval_stage = fields.Boolean(
        string='In Approval Stage',
        compute='_compute_is_in_approval_stage',
        store=False,
        help="Indicates if opportunity is in Client Approval stage"
    )

    @api.depends('stage_id')
    def _compute_is_in_approval_stage(self):
        """Check if lead is in Client Approval stage"""
        approval_stage = self.env.ref(
            'smart_view_crm_enhanced.stage_client_approval',
            raise_if_not_found=False
        )
        for lead in self:
            if approval_stage:
                lead.is_in_approval_stage = lead.stage_id == approval_stage
            else:
                lead.is_in_approval_stage = False

    def action_client_approve(self):
        """REQ-00038: Client approval action"""
        self.ensure_one()
        
        if not self.is_in_approval_stage:
            raise UserError(_("This action is only available in Client Approval stage."))
        
        self.write({
            'client_approval_state': 'approved',
            'rejection_reason': False,
            'rejection_date': False,
        })
        
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _('Approved'),
                'message': _('Client has approved the opportunity. You can now create a quotation.'),
                'type': 'success',
                'sticky': False,
            }
        }

    def action_client_reject(self):
        """REQ-00038: Client rejection action - opens wizard"""
        self.ensure_one()
        
        if not self.is_in_approval_stage:
            raise UserError(_("This action is only available in Client Approval stage."))
        
        return {
            'name': _('Rejection Reason'),
            'type': 'ir.actions.act_window',
            'res_model': 'crm.lead.rejection.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_lead_id': self.id,
            }
        }

    def action_new_quotation(self):
        """Override to check approval status"""
        # Check if in approval stage and not approved
        if self.is_in_approval_stage and self.client_approval_state != 'approved':
            raise UserError(_(
                "Cannot create quotation. Client approval is required.\n\n"
                "Current Status: %s"
            ) % (dict(self._fields['client_approval_state'].selection).get(
                self.client_approval_state, 'Pending Approval'
            )))
        
        # Check if rejected
        if self.client_approval_state == 'rejected':
            raise UserError(_(
                "Cannot create quotation. This opportunity was rejected by the client.\n\n"
                "Rejection Reason: %s"
            ) % (self.rejection_reason or 'No reason provided'))
        
        return super(CrmLead, self).action_new_quotation()

    @api.model
    def create(self, vals):
        """Set default approval state when creating in approval stage"""
        lead = super(CrmLead, self).create(vals)
        
        if lead.is_in_approval_stage and not lead.client_approval_state:
            lead.client_approval_state = 'pending'
        
        return lead

    def write(self, vals):
        """Handle stage changes"""
        res = super(CrmLead, self).write(vals)
        
        # If moving to approval stage, set pending status
        if 'stage_id' in vals:
            for lead in self:
                if lead.is_in_approval_stage and not lead.client_approval_state:
                    lead.client_approval_state = 'pending'
                # If moving out of approval stage and not decided, reset
                elif not lead.is_in_approval_stage and lead.client_approval_state == 'pending':
                    lead.client_approval_state = False
        
        return res

