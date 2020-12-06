from odoo import api, fields, models


class CalendarEvent(models.Model):
    _inherit = 'calendar.event'

    serial_number_ids = fields.Many2many('stock.production.lot', 'calendar_stock_serial_rel',
                                         'calendar_id', 'serial_id', string="Serial")

    def makebookingorder(self, name, description, user_id, start, stop, partner_ids, serial_number_ids):
        event_values = {
            'name': name,
            'description': description,
            'user_id': user_id,
            'start': start,
            'stop': stop,
            'allday': False,
            'state': 'open',  # to block that meeting date in the calendar
            'privacy': 'confidential',
            'partner_ids': [(6, 0, partner_ids)],
            'serial_number_ids': [(6, 0, serial_number_ids)]
        }
        self.with_context(no_mail_to_attendees=True, mail_post_autofollow=False, mail_create_nosubscribe=True).create(event_values)
