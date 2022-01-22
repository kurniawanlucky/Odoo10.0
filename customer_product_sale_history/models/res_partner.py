# © 2022 Lucky Kurniawan <kurniawanluckyy@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import api, fields, models, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    product_sale_history_ids = fields.One2many('sale.order.line', compute='_compute_customer_history_ids', string='Product Sales')
    count_product_sale_history = fields.Integer(string="Count Product Sale", compute='_compute_customer_history_ids', readonly=False)

    def action_view_sale_product(self):
        view_id_list = self.env.ref('sale.view_order_line_tree').id
        view_id_form = self.env.ref('sale.sale_order_line_view_form_readonly').id
        return {
            'type': 'ir.actions.act_window',
            'name': _('Product Sales'),
            'res_model': 'sale.order.line',
            'target': 'current',
            'domain': [('id', 'in', self.product_sale_history_ids.ids)],
            'views': [[view_id_list, 'list'], [view_id_form, 'form']],
            'context': {'search_default_product': True},
        }

    def _compute_customer_history_ids(self):
        for partner in self:
            partner.product_sale_history_ids = partner.sale_order_ids.mapped('order_line')
            partner.count_product_sale_history = len(partner.sale_order_ids.mapped('order_line'))
