# -*- coding: utf-8 -*-

from odoo import models, api, _
import logging

_logger = logging.getLogger(__name__)


class ProjectProject(models.Model):
    _inherit = 'project.project'

    @api.model
    def create(self, vals):
        """
        REQ-00027 Task 29: Send WhatsApp notification when project is created
        """
        project = super(ProjectProject, self).create(vals)
        
        # Check if auto-notify is enabled
        auto_notify = self.env['ir.config_parameter'].sudo().get_param(
            'smart_view_whatsapp.auto_notify_project_create', default=False
        )
        
        if auto_notify and project.partner_id and project.partner_id.phone:
            try:
                # Send notification via related SO if exists
                if project.sale_order_id:
                    project.sale_order_id._send_whatsapp_notification(
                        'project_created',
                        additional_context={'project': project}
                    )
                else:
                    # Send direct notification
                    self._send_project_whatsapp_notification(project)
            except Exception as e:
                # Don't block project creation if WhatsApp fails
                _logger.warning(
                    "Failed to send WhatsApp notification for project %s: %s",
                    project.name, str(e)
                )
        
        return project

    def _send_project_whatsapp_notification(self, project):
        """Send WhatsApp notification for project creation"""
        if not project.partner_id or not project.partner_id.phone:
            return False
        
        try:
            # Get active WhatsApp instance
            whatsapp_instance = self.env['whatsapp.instance'].search([
                ('status', '=', 'enable')
            ], limit=1)
            
            if not whatsapp_instance:
                return False
            
            # Find template
            template = self.env['whatsapp.templates'].search([
                ('name', '=', 'project_created'),
                ('whatsapp_instance_id', '=', whatsapp_instance.id),
                ('approval_state', '=', 'approved'),
            ], limit=1)
            
            if not template:
                # Send simple message if no template
                message = _(
                    "Dear %s,\n\n"
                    "Your project '%s' has been created and we're ready to start!\n\n"
                    "Best regards,\n%s"
                ) % (project.partner_id.name, project.name, project.company_id.name)
                
                whatsapp_instance.send_message(
                    mobile_number=project.partner_id.phone,
                    message=message,
                )
            else:
                # Use template
                whatsapp_instance.send_template_message(
                    mobile_number=project.partner_id.phone,
                    template=template,
                    record=project,
                )
            
            return True
            
        except Exception as e:
            _logger.error("Error sending WhatsApp for project %s: %s", project.name, str(e))
            return False

