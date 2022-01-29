# -*- coding: utf-8 -*-
# © 2022
#   @Lucky Kurniawan <kurniawanluckyy@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import models, api, fields, _
from odoo.exceptions import UserError
from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_barcode = fields.Char(related='product_id.barcode')


class SaleOrder(models.Model):
    _name = 'sale.order'
    _inherit = ['sale.order', 'barcodes.barcode_events_mixin']

    def add_order_line_by_barcode(self, product, qty):
        sale_order_line = self.order_line.filtered(lambda r: r.product_id.id == product.id)
        if sale_order_line:
            sale_order_line.product_qty += qty
        else:
            line_values = {
                'name': product.name,
                'product_id': product.id,
                'product_uom_qty': qty,
                'product_uom': product.uom_id.id,
                'price_unit': product.list_price,
            }
            new_order_line = self.order_line.new(line_values)
            self.order_line += new_order_line
            new_order_line.product_id_change()
            new_order_line.product_uom_change()
            new_order_line._onchange_discount()

    def on_barcode_scanned(self, barcode):
        qty = 1
        product = self.env['product.product'].search(['|', ('barcode', '=', barcode), ('default_code', '=', barcode)], limit=1)
        if not product:
            packaging = self.env['product.packaging'].serach([('barcode', '=', barcode)], limit=1)
            product = packaging.product_id
            qty = packaging.qty
        self.add_order_line_by_barcode(product, qty)
