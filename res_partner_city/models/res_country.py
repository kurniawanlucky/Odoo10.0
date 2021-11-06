from odoo import fields, models


class ResCountry(models.Model):
    _inherit = 'res.country'

    city_ids = fields.One2many('res.city', 'country_id', string='Cities')
