# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResUsers(models.Model):
    _inherit = 'res.users'

    # REQ-00018: Additional user fields for Smart View
    smart_view_access_level = fields.Selection([
        ('none', 'No Access'),
        ('user', 'User'),
        ('manager', 'Manager'),
        ('admin', 'Administrator'),
    ], string='Smart View Access Level', default='none',
        help="Define user's access level for Smart View modules")

    smart_view_notes = fields.Text(
        string='Smart View Notes',
        help="Internal notes about this user's Smart View permissions"
    )

    is_smart_view_manager = fields.Boolean(
        string='Smart View Manager',
        compute='_compute_is_smart_view_manager',
        store=False,
        help="Indicates if user is a Smart View Manager"
    )

    def _compute_is_smart_view_manager(self):
        """Check if user has Smart View Manager group"""
        manager_group = self.env.ref('smart_view_base.group_smart_view_manager', raise_if_not_found=False)
        for user in self:
            if manager_group:
                user.is_smart_view_manager = manager_group in user.group_ids
            else:
                user.is_smart_view_manager = False

    def grant_settings_access(self):
        """REQ-00018: Grant Settings Access to user"""
        self.ensure_one()
        settings_group = self.env.ref('smart_view_base.group_settings_access')
        if settings_group not in self.group_ids:
            self.write({'group_ids': [(4, settings_group.id)]})
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Settings Access Granted',
                'message': f'Settings access has been granted to {self.name}',
                'type': 'success',
                'sticky': False,
            }
        }

    def revoke_settings_access(self):
        """Revoke Settings Access from user"""
        self.ensure_one()
        settings_group = self.env.ref('smart_view_base.group_settings_access')
        if settings_group in self.group_ids:
            self.write({'group_ids': [(3, settings_group.id)]})
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Settings Access Revoked',
                'message': f'Settings access has been revoked from {self.name}',
                'type': 'warning',
                'sticky': False,
            }
        }

