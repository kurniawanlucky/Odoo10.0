from odoo import api, fields, models
from odoo.tools.safe_eval import safe_eval


class BookingTeam(models.Model):
    _name = 'booking.team'
    # _inherit = ['crm.team']

    name = fields.Char('Name', index=True, required=True, translate=True)
    team_leader_id = fields.Many2one('hr.employee', 'Team Leader')
    employee_ids = fields.Many2many('hr.employee', 'employee_booking_team_rel', 'team_id', 'employee_id',
                                    string="Employees")
    serial_number_ids = fields.Many2many('stock.production.lot', 'booking_team_stock_serial_rel',
                                         'booking_team_id', 'serial_id', string="Serial")
