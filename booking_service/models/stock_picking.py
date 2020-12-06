from odoo import api, fields, models, _
from odoo.tools.float_utils import float_compare
from odoo.exceptions import ValidationError


class StockPicking(models.Model):
    _inherit = "stock.picking"

    # state = fields.Selection(
    #     selection_add=[('pending', 'Pending')],
    # )

    state = fields.Selection([
        ('draft', 'Draft'), ('cancel', 'Cancelled'),
        ('waiting', 'Waiting Another Operation'),
        ('confirmed', 'Waiting Availability'),
        ('partially_available', 'Partially Available'),
        ('pending', 'Pending'),
        ('assigned', 'Started'), ('done', 'Done')], string='Status', compute='_compute_state',
        copy=False, index=True, readonly=True, store=True, track_visibility='onchange',
        help=" * Draft: not confirmed yet and will not be scheduled until confirmed\n"
             " * Waiting Another Operation: waiting for another move to proceed before it becomes automatically available (e.g. in Make-To-Order flows)\n"
             " * Waiting Availability: still waiting for the availability of products\n"
             " * Partially Available: some products are available and reserved\n"
             " * Ready to Transfer: products reserved, simply waiting for confirmation.\n"
             " * Transferred: has been processed, can't be modified or cancelled anymore\n"
             " * Cancelled: has been cancelled, can't be confirmed anymore")

    is_booking = fields.Boolean('Booking')

    scheduled_start = fields.Datetime('Scheduled Start')
    scheduled_end = fields.Datetime('Scheduled End')

    actual_start = fields.Datetime('Actual Start')
    actual_end = fields.Datetime('Actual End')

    booking_team_id = fields.Many2one('booking.team', 'Team')
    team_leader_id = fields.Many2one('hr.employee', 'Team Leader')

    employee_ids = fields.Many2many('hr.employee', 'employee_booking_picking_rel',
                                    'employee_id', 'picking_id', string="Employees")
    equipments_ids = fields.Many2many('stock.production.lot', 'serial_booking_picking_rel',
                                      'serial_id', 'picking_id', string="Equipments")
    ignore_warning = fields.Boolean('Ignore Warning', default=False)

    def action_mark_to_do(self):
        for picking in self.filtered(lambda x: x.is_booking and not x.ignore_warning):
            employee, equipment = picking.check_available_booking()
            if employee or equipment:
                self.ensure_one()
                return {
                    'name': _('Mark to do Confirmation'),
                    'view_type': 'form',
                    'view_mode': 'form',
                    'res_model': 'wizard.booking.sale',
                    'view_id': self.env.ref('booking_service.confirm_ignore_warning').id,
                    'type': 'ir.actions.act_window',
                    'target': 'new',
                    'context': {
                        'active_id': picking.id,
                        'active_model': picking._name
                    }
                }

    @api.multi
    def action_check_booking(self):
        employee, equipment = self.check_available_booking()
        if employee or equipment:
            note = ''
            if employee:
                note = ', '.join(employee)
                note += 'And '
            if equipment:
                note += ', '.join(equipment)
            note += ' has an event on that day and time'
            raise ValidationError(_(note))
        else:
            raise ValidationError(_('Everyone is available for the booking'))

    def check_available_booking(self):
        if self.is_booking:
            employees = []
            equipments = []
            for employee in self.employee_ids:
                if employee.calendar_event_ids.filtered(lambda x: (x.start <= self.scheduled_start <= x.stop) or (x.start <= self.scheduled_end <= x.stop)):
                    employees.append('Employee ' + employee.name)
            for equipment in self.equipments_ids:
                if equipment.calendar_event_ids.filtered(lambda x: (x.start <= self.scheduled_start <= x.stop) or (x.start <= self.scheduled_end <= x.stop)):
                    equipments.append('Equipment ' + equipment.product_id.name)
            return employees, equipments

    def makebookingorder(self, name, description, user_id, start, stop, partner_ids, serial_number_ids):
        self.env['calendar.event'].makebookingorder(name, description, user_id, start, stop, partner_ids, serial_number_ids)

    @api.model
    def create(self, vals):
        if vals.get('name', '/') == '/' and vals.get('is_booking'):
            vals['name'] = self.env['ir.sequence'].next_by_code('work.order') or '/'
        res = super(StockPicking, self).create(vals)
        return res
