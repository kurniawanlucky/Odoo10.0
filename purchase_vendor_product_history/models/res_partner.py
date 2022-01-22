# © 2022 Lucky Kurniawan <kurniawanluckyy@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import api, fields, models, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    purchase_order_ids = fields.One2many('purchase.order', 'partner_id', 'Purchase Order')
    product_purchase_history_ids = fields.One2many('purchase.order.line', compute='_compute_vendor_history_ids', string='Product Purchase')
    count_product_purchase_history = fields.Integer(string="Count Product Sale", compute='_compute_vendor_history_ids', readonly=False)

    def action_view_purchase_product(self):
        view_id_list = self.env.ref('purchase.purchase_order_line_tree').id
        view_id_form = self.env.ref('purchase.purchase_order_line_form2').id
        return {
            'type': 'ir.actions.act_window',
            'name': _('Purchase Product'),
            'res_model': 'purchase.order.line',
            'target': 'current',
            'domain': [('id', 'in', self.product_purchase_history_ids.ids)],
            'views': [[view_id_list, 'list'], [view_id_form, 'form']],
            'context': {'search_default_groupby_product': True},
        }

    def _compute_vendor_history_ids(self):
        for partner in self:
            partner.product_purchase_history_ids = partner.purchase_order_ids.mapped('order_line')
            partner.count_product_purchase_history = len(partner.purchase_order_ids.mapped('order_line'))
