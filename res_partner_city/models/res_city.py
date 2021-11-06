from odoo import fields, models, api, _
from odoo.tools.float_utils import float_compare
from odoo.exceptions import UserError
from odoo.addons import decimal_precision as dp


class ResCity(models.Model):
    _name = 'res.city'

    country_id = fields.Many2one('res.country', string='Country', readonly=True)
    name = fields.Char(string='City', index=True, required=True, translate=True)
