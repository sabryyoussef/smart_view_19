# -*- coding: utf-8 -*-

from odoo import models, fields


class CrmStage(models.Model):
    _inherit = 'crm.stage'

    is_approval_stage = fields.Boolean(
        string='Is Approval Stage',
        default=False,
        help="Mark this stage as requiring client approval"
    )

    is_site_visit_stage = fields.Boolean(
        string='Is Site Visit Stage',
        default=False,
        help="Mark this stage as site visit stage"
    )

    is_technical_stage = fields.Boolean(
        string='Is Technical Stage',
        default=False,
        help="Mark this stage as technical description stage"
    )

