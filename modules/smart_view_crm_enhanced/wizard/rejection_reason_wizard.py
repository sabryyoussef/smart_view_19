# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class CrmLeadRejectionWizard(models.TransientModel):
    _name = 'crm.lead.rejection.wizard'
    _description = 'CRM Lead Rejection Wizard'

    lead_id = fields.Many2one(
        'crm.lead',
        string='Opportunity/Lead',
        required=True,
        ondelete='cascade'
    )

    rejection_reason = fields.Text(
        string='Rejection Reason',
        required=True,
        help="Please provide the reason for client rejection"
    )

    rejection_category = fields.Selection([
        ('price', 'Price Too High'),
        ('timeline', 'Timeline Issues'),
        ('scope', 'Scope Mismatch'),
        ('competitor', 'Chose Competitor'),
        ('budget', 'Budget Constraints'),
        ('postponed', 'Project Postponed'),
        ('other', 'Other Reason'),
    ], string='Rejection Category',
       required=True,
       default='other',
       help="Category of rejection for reporting")

    notify_team = fields.Boolean(
        string='Notify Sales Team',
        default=True,
        help="Send notification to sales team about rejection"
    )

    @api.constrains('rejection_reason')
    def _check_rejection_reason(self):
        """Ensure rejection reason is meaningful"""
        for wizard in self:
            if wizard.rejection_reason and len(wizard.rejection_reason.strip()) < 10:
                raise ValidationError(_(
                    "Please provide a more detailed rejection reason (at least 10 characters)."
                ))

    def action_confirm_rejection(self):
        """Confirm rejection and update lead"""
        self.ensure_one()
        
        if not self.lead_id:
            raise ValidationError(_("No lead/opportunity selected."))
        
        # Format rejection reason with category
        category_label = dict(self._fields['rejection_category'].selection)[self.rejection_category]
        full_reason = f"[{category_label}]\n{self.rejection_reason}"
        
        # Update lead
        self.lead_id.write({
            'client_approval_state': 'rejected',
            'rejection_reason': full_reason,
            'rejection_date': fields.Datetime.now(),
            'active': True,  # Keep it active for review
        })
        
        # Post message on lead
        self.lead_id.message_post(
            body=_(
                "<p><strong>Client Rejected</strong></p>"
                "<p><strong>Category:</strong> %s</p>"
                "<p><strong>Reason:</strong> %s</p>"
            ) % (category_label, self.rejection_reason),
            subject=_('Opportunity Rejected by Client'),
            message_type='notification',
        )
        
        # Send notification if requested
        if self.notify_team and self.lead_id.user_id:
            self.lead_id.activity_schedule(
                'mail.mail_activity_data_todo',
                summary=_('Client Rejected Opportunity'),
                note=_('Category: %s\nReason: %s') % (category_label, self.rejection_reason),
                user_id=self.lead_id.user_id.id,
            )
        
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _('Opportunity Rejected'),
                'message': _('The opportunity has been marked as rejected.'),
                'type': 'warning',
                'sticky': False,
                'next': {'type': 'ir.actions.act_window_close'},
            }
        }

    def action_cancel(self):
        """Cancel rejection"""
        return {'type': 'ir.actions.act_window_close'}

