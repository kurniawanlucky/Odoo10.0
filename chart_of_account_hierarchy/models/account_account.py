from odoo import api, fields, models, _


class AccountAccount(models.Model):
    _inherit = 'account.account'

    parent_id = fields.Many2one('account.account', 'Parent Account')
    child_ids = fields.One2many('account.account', 'parent_id', 'Children')

