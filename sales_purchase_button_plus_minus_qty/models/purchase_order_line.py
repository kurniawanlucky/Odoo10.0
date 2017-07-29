from odoo import api, exceptions, fields, models, _


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'


    @api.multi
    def plus_qty(self):
        self.ensure_one()
        self.product_qty += 1

    @api.multi
    def minus_qty(self):
        self.ensure_one()
        self.product_qty -= 1