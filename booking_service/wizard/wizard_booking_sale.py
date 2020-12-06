from odoo import api, fields, models, _


class WizardBookingSale(models.TransientModel):
    _name = "wizard.booking.sale"

    sale_id = fields.Many2one('sale.order', "Sale")
    picking_id = fields.Many2one('stock.picking', "Picking")
    note = fields.Char('Note')

    @api.multi
    def button_confirm(self):
        self.ensure_one()
        if self.sale_id:
            self.sale_id.write({'ignore_warning': True})
        else:
            picking_id = self.picking_id
            picking_id.write({'ignore_warning': True})
            description = picking_id.display_name + ' from:' + str(picking_id.scheduled_start) + ' to:' + str(picking_id.scheduled_end)
            partner_ids = picking_id.employee_ids.mapped('user_id').mapped('partner_id').ids
            partner_ids.append(picking_id.team_leader_id.user_id.partner_id.id)
            picking_id.makebookingorder(picking_id.display_name, description, picking_id.team_leader_id.user_id.id, picking_id.scheduled_start,
                                  picking_id.scheduled_end, partner_ids, picking_id.equipments_ids.ids)

    @api.model
    def default_get(self, fields):
        rec = super(WizardBookingSale, self).default_get(fields)
        context = dict(self._context or {})
        active_ids = context.get('active_ids')
        if active_ids:
            if 'sale_id' in fields and 'picking_id' in fields:
                if context.get('active_model') == 'sale.order':
                    sale = self.env['sale.order'].browse(active_ids)
                    employee, equipment = sale.check_available_booking()
                    rec.update({'sale_id': sale.id})
                else:
                    picking = self.env['stock.picking'].browse(active_ids)
                    employee, equipment = picking.check_available_booking()
                    rec.update({'picking_id': picking.id})
                note = ''
                if employee:
                    note = ', '.join(employee)
                    note += 'And '
                if equipment:
                    note += ', '.join(equipment)
                note += ' has an event on that day and time, are you sure you want to validate?'
                rec.update({
                    'note': note
                })
        return rec
