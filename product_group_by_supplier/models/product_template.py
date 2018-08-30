# -*- coding: utf-8 -*-
# Copyright 2017 Lucky Kurniawan <kurniawanluckyy@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, api, fields, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    supplier_id = fields.Many2one('res.partner', string="Supplier",
                                  compute='_compute_supplierinfor', store=True)

    @api.depends('seller_ids')
    def _compute_supplierinfor(self):
        for product in self:
            if len(product.seller_ids) > 0:
                product.supplier_id = product.seller_ids[0].name.id
