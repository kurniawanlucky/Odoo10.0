from odoo import api, Command, fields, models, tools, SUPERUSER_ID, _


class ProjectUserGroup(models.Model):
    _name = 'project.user.group'

    name = fields.Char(string='Name', required=True, translate=True)
    user_ids = fields.Many2many('res.users', relation='project_user_group_rel', column1='group_id', column2='user_id',
                                string='Users', context={'active_test': False}, tracking=True)
    description = fields.Char(string='Label on Invoices')
