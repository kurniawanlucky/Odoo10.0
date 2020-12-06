from odoo import api, fields, models, _
from dateutil.relativedelta import relativedelta
from datetime import datetime
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    is_booking = fields.Boolean('Booking')

    def _get_default_booking_end(self):
        booking_end = datetime.now() + relativedelta(hours=1)
        return booking_end

    partner_id = fields.Many2one('res.partner', string='Customer')
    booking_team_id = fields.Many2one('booking.team', 'Team')
    team_leader_id = fields.Many2one('hr.employee', 'Team Leader')

    employee_ids = fields.Many2many('hr.employee', 'employee_booking_sale_rel',
                                        'employee_id', 'sale_id', string="Employees")
    equipments_ids = fields.Many2many('stock.production.lot', 'serial_booking_sale_rel',
                                    'serial_id', 'sale_id', string="Equipments")

    # employee_ids = fields.One2many('hr.employee', 'sale_id', 'Employees')
    # equipments_ids = fields.One2many('booking.equipments', 'sale_id', 'Equipments')

    booking_start = fields.Datetime('Booking Start', default=fields.Datetime.now)
    booking_end = fields.Datetime('Booking End', default=_get_default_booking_end)

    ignore_warning = fields.Boolean('Ignore Warning', default=False)

    @api.multi
    def write(self, vals):
        if vals.get('employee_ids'):
            employees = [employee[1] for employee in vals.get('employee_ids') if employee[1]]
            if employees:
                vals.update({'employee_ids': [(6, 0, employees)]})
        if vals.get('equipments_ids'):
            equipments = [equipment[1] for equipment in vals.get('equipments_ids') if equipment[1]]
            if equipments:
                vals.update({'equipments_ids': [(6, 0, equipments)]})
        res = super(SaleOrder, self).write(vals)
        return res

    def makebookingorder(self, name, description, user_id, start, stop, partner_ids, serial_number_ids):
        self.env['calendar.event'].makebookingorder(name, description, user_id, start, stop, partner_ids, serial_number_ids)

    @api.multi
    def action_confirm(self):
        for sale in self.filtered(lambda x: x.is_booking and not x.ignore_warning and x.state not in ('sale', 'done', 'cancel')):
            employee, equipment = sale.check_available_booking()
            if employee or equipment:
                self.ensure_one()
                return {
                    'name': _('Booking Confirmation'),
                    'view_type': 'form',
                    'view_mode': 'form',
                    'res_model': 'wizard.booking.sale',
                    'view_id': self.env.ref('booking_service.confirm_ignore_warning').id,
                    'type': 'ir.actions.act_window',
                    'target': 'new',
                    'context': {
                        'active_id': sale.id,
                        'active_model': sale._name
                    }
                }
        res = super(SaleOrder, self).action_confirm()
        for sale in self.filtered(lambda x: x.is_booking):
            description = sale.display_name + ' from:' + str(sale.booking_start) + ' to:' + str(sale.booking_end)
            partner_ids = sale.employee_ids.mapped('user_id').mapped('partner_id').ids
            partner_ids.append(sale.team_leader_id.user_id.partner_id.id)
            self.makebookingorder(sale.display_name, description, sale.team_leader_id.user_id.id, sale.booking_start, sale.booking_end, partner_ids, sale.equipments_ids.ids)
        return res

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
                if employee.calendar_event_ids.filtered(lambda x: (x.start <= self.booking_start <= x.stop) or (x.start <= self.booking_end <= x.stop)):
                    employees.append('Employee ' + employee.name)
            for equipment in self.equipments_ids:
                if equipment.calendar_event_ids.filtered(lambda x: (x.start <= self.booking_start <= x.stop) or (x.start <= self.booking_end <= x.stop)):
                    equipments.append('Equipment ' + equipment.product_id.name)
            return employees, equipments

    @api.onchange('booking_team_id')
    def _onchange_booking_team_id(self):
        if self.booking_team_id:
            self.team_leader_id = self.booking_team_id.team_leader_id.id
            self.employee_ids = [(6, 0, self.booking_team_id.employee_ids.ids)]
            self.equipments_ids = [(6, 0, self.booking_team_id.serial_number_ids.ids)]
