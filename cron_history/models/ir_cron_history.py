from odoo import models, fields, api


class IrCronHistory(models.Model):
    _name = "ir.cron.history"

    cron_id = fields.Many2one("ir.cron", 'Cron')
    start_time = fields.Datetime('Start', copy=False)
    finish_time = fields.Datetime('Finish', copy=False)
    duration = fields.Char('Duration', compute='_get_duration')

    @api.depends('duration')
    def _get_duration(self):
        for cron in self:
            if cron.start_time and cron.finish_time:
                difference = fields.Datetime.from_string(cron.finish_time) - fields.Datetime.from_string(cron.start_time)
                duration_in_s = difference.total_seconds()
                days = divmod(duration_in_s, 86400)
                hours = divmod(days[1], 3600)
                minutes = divmod(hours[1], 60)
                seconds = divmod(minutes[1], 1)
                difference = []
                if days[0] > 0:
                    difference.append('%sd' % days[0])
                if hours[0] > 0:
                    difference.append('%sh' % hours[0])
                if minutes[0] > 0:
                    difference.append('%sm' % minutes[0])
                if seconds[0] > 0:
                    difference.append('%ss' % seconds[0])
                cron.duration = ' '.join(difference)
