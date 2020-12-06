from odoo import api, fields, models


class StockProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    calendar_event_ids = fields.Many2many('calendar.event', 'calendar_stock_serial_rel',
                                          'serial_id', 'calendar_id', string="Calendar Event")
    event_count = fields.Float('Count Event', compute='_compute_event')

    @api.multi
    def _compute_event(self):
        for serial in self:
            serial.event_count = len(serial.calendar_event_ids)

    @api.multi
    def action_view_calendar_event(self):
        self.ensure_one()
        action = self.env.ref('calendar.action_calendar_event').read()[0]
        action['context'] = {}
        calendar_event_ids = self.calendar_event_ids.ids
        if len(calendar_event_ids) > 1:
            action['views'] = [(self.env.ref('calendar.view_calendar_event_tree').id, 'tree')]
            action['domain'] = [('id', 'in', calendar_event_ids)]
        elif calendar_event_ids:
            action['views'] = [(self.env.ref('calendar.view_calendar_event_form').id, 'form')]
            action['res_id'] = calendar_event_ids[0]
        return action
