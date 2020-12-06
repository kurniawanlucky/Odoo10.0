from odoo import fields, models, api


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    event_count = fields.Float('Count Event', compute='_compute_event')
    calendar_event_ids = fields.One2many(comodel_name='calendar.event', string='Event', compute='_compute_event', readonly=True)

    @api.multi
    def _compute_event(self):
        for employee in self:
            calendar_event_ids = employee.user_id.partner_id.mapped('calendar_event_ids')
            employee.calendar_event_ids = calendar_event_ids
            employee.event_count = len(calendar_event_ids)

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
