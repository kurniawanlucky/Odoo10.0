# -*- coding: utf-8 -*-
# Copyright 2017 Lucky Kurniawan <kurniawanluckyy@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, api, fields, _
from odoo.exceptions import UserError
from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def _add_supplier_to_product(self):
        super(PurchaseOrder, self)._add_supplier_to_product()
        for line in self.order_line:
            partner = self.partner_id if not self.partner_id.parent_id else self.partner_id.parent_id
            supplier = line.product_id.seller_ids.filtered(lambda x: x.name.id == partner.id)
            if supplier:
                currency = partner.property_purchase_currency_id or self.env.user.company_id.currency_id
                supplier.write({'price': self.currency_id.compute(line.price_unit, currency)})
