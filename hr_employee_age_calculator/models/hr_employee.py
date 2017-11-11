# -*- coding: utf-8 -*-
# Copyright 2017 Lucky Kurniawan <kurniawanluckyy@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import fields, models, api
from datetime import timedelta, date
from dateutil.relativedelta import relativedelta


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    age = fields.Char('Age', compute='_age_product')

    @api.multi
    @api.depends('birthday')
    def _age_product(self):
        today = date.today()
        for record in self:
            age = []
            dob = fields.Date.from_string(record.birthday)
            gap = relativedelta(today, dob)
            if gap.years > 0:
                record.age = str(gap.years) + ' Years'
