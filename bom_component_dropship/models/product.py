from odoo import api, fields, models, _


class ProductProduct(models.Model):
    _inherit = 'product.product'

    bom_line_ids = fields.One2many('mrp.bom.line', 'product_id', 'BoM Lines')
