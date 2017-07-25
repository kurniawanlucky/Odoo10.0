
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo import api, fields, models, _
from datetime import datetime, timedelta


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    sum_order_qty = fields.Integer('Sum Order Qty', compute='sum_order_qty_action')
    sum_delivery_qty = fields.Integer('Sum Delivery', compute='sum_delivery_qty_action')
    percent_delivery = fields.Char('Progress (%)', compute='progress_delivery', help='To Show Progress Delivery')

    @api.one
    @api.depends('percent_delivery')
    def progress_delivery(self):
        percent = float(self.sum_delivery_qty) / float(self.sum_order_qty) * 100
        self.percent_delivery = str(percent) + '%'

    @api.one
    @api.depends('sum_order_qty')
    def sum_order_qty_action(self):
        sale_order_lines = self.order_line
        order_qty = 0
        for sol in sale_order_lines:
            order_qty += sol.product_uom_qty

        self.sum_order_qty = order_qty

    @api.one
    @api.depends('sum_delivery_qty')
    def sum_delivery_qty_action(self):
        sale_order_lines = self.order_line
        delivered_qty = 0
        for sol in sale_order_lines:
            delivered_qty += sol.qty_delivered

        self.sum_delivery_qty = delivered_qty