from odoo import _, api, fields, models


class ProductPutaway(models.Model):
    _inherit = 'product.putaway'

    @api.model
    def _get_putaway_options(self):
        ret = super(ProductPutaway, self)._get_putaway_options()
        return ret + [('per_product', 'Fixed per product location')]

    def _putaway_apply_per_product(self, product):
        if product.location_id:
            return product.location_id.id
        return self.env['stock.location']

    # def putaway_apply(self, product):
    #     if self.method == 'per_product':
    #         strategies = self.get_product_putaway_strategies(
    #             product)
    #         return strategies[:1].fixed_location_id.id
    #     else:
    #         return super(ProductPutaway, self).putaway_apply(product)
