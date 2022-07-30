from odoo import api, fields, models


class ProductBrand(models.Model):
    _name = 'product.brand'

    name = fields.Char('Brand Name', required=True)
    description = fields.Text('Description', translate=True)

    logo = fields.Binary('Logo File')
    product_ids = fields.One2many('product.template', 'brand_id', string='Products')
    products_count = fields.Integer(string='Number of products', compute='_get_products_count')

    @api.depends('product_ids.brand_id')
    def _get_products_count(self):
        for brand in self:
            brand.products_count = len(brand.product_ids)
