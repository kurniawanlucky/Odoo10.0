# -*- coding: utf-8 -*-
# © 2019
#   @Lucky Kurniawan <kurniawanluckyy@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from collections import Counter
import odoo.addons.decimal_precision as dp
from odoo import models, api, fields, _
from odoo.exceptions import AccessError, UserError


class ProductProduct(models.Model):
    _inherit = 'product.product'

    potential_qty = fields.Float(
        compute='_get_potential_qty',
        type='float',
        digits_compute=dp.get_precision('Product Unit of Measure'),
        string='Potential',
        help="Quantity of this Product that could be produced using "
             "the materials already at hand.")

    # Needed for fields dependencies
    # When self.potential_qty is compute, we want to force the ORM
    # to compute all the components potential_qty too.
    component_ids = fields.Many2many(
        comodel_name='product.product',
        compute='_get_component_ids',
    )

    @api.multi
    def _compute_potential_quantities_dict(self):
        stock_dict = self._compute_quantities_dict(
            self._context.get('lot_id'),
            self._context.get('owner_id'),
            self._context.get('package_id'),
            self._context.get('from_date'),
            self._context.get('to_date'))
        res = {}
        for product in self:
            res[product.id] = {
                'potential_qty': product.potential_qty
            }
        return res, stock_dict

    @api.multi
    @api.depends('component_ids.potential_qty')
    def _get_potential_qty(self):
        """Compute the potential qty based on the available components."""
        bom_obj = self.env['mrp.bom']

        for product in self:
            bom_id = bom_obj._bom_find(product=product)
            if not bom_id:
                product.potential_qty = 0.0
                continue

            try:
                component_needs = self._get_components_needs(product, bom_id)
            except AccessError:
                # If user doesn't have access to BOM
                # he can't see potential_qty
                component_needs = None

            if not component_needs:
                # The BoM has no line we can use
                product.potential_qty = 0.0

            else:
                # Find the lowest quantity we can make with the stock at hand
                components_potential_qty = min(
                    [self._get_component_qty(component) // need
                     for component, need in component_needs.items()]
                )

                # Compute with bom quantity
                bom_qty = bom_id.product_qty
                product.potential_qty = bom_qty * components_potential_qty

    def _get_component_qty(self, component):
        icp = self.env['ir.config_parameter']
        stock_available_mrp_based_on = icp.get_param(
            'stock_available_mrp_based_on', 'qty_available'
        )

        return component[stock_available_mrp_based_on]

    def _get_components_needs(self, product, bom):

        needs = Counter()
        boms, lines = bom.explode(product, 1.0)
        for bom_component in lines:
            component = bom_component[0].product_id
            qty = bom_component[0].product_qty
            needs += Counter(
                {component: qty}
            )

        return needs

    def _get_component_ids(self):
        bom_obj = self.env['mrp.bom']

        bom_id = bom_obj._bom_find(product=self)
        if bom_id:
            boms, lines = bom_id.explode(self, 1.0)
            for bom_component in lines:
                self.component_ids |= self.browse(bom_component[0].product_id.id)
