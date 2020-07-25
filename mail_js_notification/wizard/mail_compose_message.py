# -*- coding: utf-8 -*-
# Copyright 2020 Lucky Kurniawan <kurniawanluckyy@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import models, fields, api


class MailComposeMessage(models.TransientModel):
    _inherit = 'mail.compose.message'

    @api.multi
    def send_mail_action(self):
        super(MailComposeMessage, self).send_mail_action()
        return {
            'type': 'ir.actions.act_js_notification',
            'title': "Success",
            'message': "Email has been Sent",
        }