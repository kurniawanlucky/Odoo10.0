from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    city_id = fields.Many2one('res.city', string='City', domain="[('country_id','=',country_id)]")
