# -*- coding: utf-8 -*-
# © 2017
#   @Lucky Kurniawan <kurniawanluckyy@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import models, api, fields, _
from odoo.exceptions import UserError
from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _barcode_scanned = fields.Char("Barcode Scanned", help="Value of the last barcode scanned.", store=False)

    @api.model
    def so_barcode(self, barcode, so_id):
        sale_order = self.env['sale.order'].search([('id', '=', so_id)])
        if not sale_order:
            # with asumtation Sale Order is created
            raise UserError(_('Please Choose Your Customer And Fix Your Sale Order'))
        product_id = self.env['product.product'].search([('barcode', '=', barcode)])
        sale_order_line = sale_order.order_line.search([('product_id', '=', product_id.id)], limit=1)
        if sale_order_line:
            sale_order_line.product_uom_qty = sale_order_line.product_uom_qty + 1
        else:
            line_values = {
                'name': product_id.name,
                'product_id': product_id.id,
                'product_qty': 1,
                'product_uom': product_id.product_tmpl_id.uom_id.id,
                'price_unit': product_id.product_tmpl_id.list_price,
                'order_id': sale_order.id,
                'date_planned': datetime.today().strftime(DEFAULT_SERVER_DATETIME_FORMAT),
            }
            sale_order.update({'order_line': [(0, 0, line_values)]})


