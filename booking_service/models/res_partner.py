from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    calendar_event_ids = fields.Many2many('calendar.event', 'calendar_event_res_partner_rel', 'calendar_event_id', 'res_partner_id', string='Event')
