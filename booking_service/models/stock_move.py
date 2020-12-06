from odoo import fields, models, api


class StockMove(models.Model):
    _inherit = "stock.move"

    @api.multi
    def _get_new_picking_values(self):
        values = super(StockMove, self)._get_new_picking_values()
        if self.procurement_id.sale_line_id:
            sale = self.procurement_id.sale_line_id.order_id
            if sale.is_booking:
                if sale.employee_ids:
                    employee = [(6, 0, sale.employee_ids.ids)]
                    values['employee_ids'] = employee
                if sale.equipments_ids:
                    equipments = [(6, 0, sale.equipments_ids.ids)]
                    values['equipments_ids'] = equipments
                values.update({
                    'is_booking': True,
                    'scheduled_start': sale.booking_start,
                    'scheduled_end': sale.booking_end,
                    'actual_start': sale.booking_start,
                    'actual_end': sale.booking_end,
                    'booking_team_id': sale.booking_team_id.id,
                    'team_leader_id': sale.team_leader_id.id,
                })
        return values
