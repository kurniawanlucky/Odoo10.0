from odoo import api, exceptions, fields, models, _


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.multi
    def plus_qty(self):
        self.ensure_one()
        self.product_uom_qty += 1

    @api.multi
    def minus_qty(self):
        self.ensure_one()
        self.product_uom_qty -= 1
