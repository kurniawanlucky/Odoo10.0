from odoo import _, fields, models


class ProjectTask(models.Model):
    _inherit = 'project.task'

    group_id = fields.Many2one('project.user.group', related='project_id.group_id', store=True)
