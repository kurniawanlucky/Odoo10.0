from odoo import _, fields, models


class ProjectProject(models.Model):
    _inherit = 'project.project'

    group_id = fields.Many2one('project.user.group', copy=False)
