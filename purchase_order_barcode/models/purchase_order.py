# -*- coding: utf-8 -*-
# © 2022
#   @Lucky Kurniawan <kurniawanluckyy@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import models, api, fields, _


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    product_barcode = fields.Char(related='product_id.barcode')


class PurchaseOrder(models.Model):
    _name = 'purchase.order'
    _inherit = ['purchase.order', 'barcodes.barcode_events_mixin']

    def add_order_line_by_barcode(self, product, qty):
        purchase_order_line = self.order_line.filtered(lambda r: r.product_id.id == product.id)
        if purchase_order_line:
            purchase_order_line.product_qty += qty
        else:
            line_values = {
                'name': product.name,
                'product_id': product.id,
                'product_qty': qty,
                'product_uom': product.uom_id.id,
                'price_unit': product.list_price,
            }
            new_order_line = self.order_line.new(line_values)
            self.order_line += new_order_line
            new_order_line._product_id_change()

    def on_barcode_scanned(self, barcode):
        qty = 1
        product = self.env['product.product'].search(['|', ('barcode', '=', barcode), ('default_code', '=', barcode)], limit=1)
        if not product:
            packaging = self.env['product.packaging'].serach([('barcode', '=', barcode)], limit=1)
            product = packaging.product_id
            qty = packaging.qty
        self.add_order_line_by_barcode(product, qty)
