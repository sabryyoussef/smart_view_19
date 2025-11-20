# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class ProjectStage(models.Model):
    _inherit = 'project.project.stage'

    # REQ-00043 Task 50: Stage locking
    is_locked = fields.Boolean(
        string='Locked Stage',
        default=False,
        help="Locked stages cannot be deleted or modified"
    )
    
    stage_code = fields.Char(
        string='Stage Code',
        help="Unique code for identifying standard stages"
    )

    def unlink(self):
        """REQ-00043 Task 50: Prevent deletion of locked stages"""
        for stage in self:
            if stage.is_locked:
                raise UserError(_(
                    "Cannot delete locked stage: %s\n\n"
                    "This is a standard stage required for project workflow.\n"
                    "To remove it, first uncheck 'Locked Stage' in the stage settings."
                ) % stage.name)
        return super(ProjectStage, self).unlink()

    def write(self, vals):
        """Prevent unlocking if user doesn't have permission"""
        # Allow unlocking only for system users
        if 'is_locked' in vals and not vals['is_locked']:
            if not self.env.user.has_group('base.group_system'):
                raise UserError(_(
                    "Only system administrators can unlock stages."
                ))
        return super(ProjectStage, self).write(vals)

