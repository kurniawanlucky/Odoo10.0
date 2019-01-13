# -*- coding: utf-8 -*-
# © 2019
#   @Lucky Kurniawan <kurniawanluckyy@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import odoo.addons.decimal_precision as dp
from odoo import models, api, fields, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    potential_qty = fields.Float(
        compute='_compute_potential_quantities',
        digits=dp.get_precision('Product Unit of Measure'),
        string='Potential',
        help="Quantity of this Product that could be produced using "
             "the materials already at hand. "
             "If the product has several variants, this will be the biggest "
             "quantity that can be made for a any single variant.")

    @api.multi
    @api.depends('product_variant_ids.potential_qty')
    def _compute_potential_quantities(self):
        res = self._compute_potential_quantities_dict()
        for product in self:
            for key, value in res[product.id].iteritems():
                if key in product._fields:
                    product[key] = value

    @api.multi
    def _compute_potential_quantities_dict(self):
        variants_dict, _ = self.mapped('product_variant_ids')._compute_potential_quantities_dict()
        res = {}
        for template in self:
            potential_qty = max(
                [variants_dict[p.id]["potential_qty"] for p in
                 template.product_variant_ids] or [0.0])
            res[template.id] = {
                "potential_qty": potential_qty,
            }
        return res

    @api.multi
    def action_view_mrp_component(self):
        self.ensure_one()
        action = self.env.ref('stock.product_open_quants')
        return {
            'name': action.name,
            'help': action.help,
            'type': action.type,
            'view_type': action.view_type,
            'view_mode': action.view_mode,
            'target': action.target,
            'context': {'search_default_internal_loc': 1, 'search_default_locationgroup':1},
            'res_model': action.res_model,
            'domain': [('product_id', 'in', self.product_variant_ids[0].component_ids.ids)],
        }