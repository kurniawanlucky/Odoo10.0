from odoo import api, models, tools, fields


class ProductTemplate(models.Model):
    _inherit = "product.template"

    location_id = fields.Many2one('stock.location', string='Location')
