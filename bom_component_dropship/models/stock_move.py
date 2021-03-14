from odoo import api, fields, models


class StockMove(models.Model):
    _inherit = 'stock.move'

    @api.multi
    def action_explode(self):
        moves = super(StockMove, self).action_explode()
        if len(moves) == 1 and moves.filtered(lambda x: x.product_id.bom_line_ids and x.picking_type_id.code == 'outgoing'):
            phantom_moves = self.env['stock.move']
            for move in moves:
                bom = self.env['mrp.bom'].sudo()._bom_find(product=move.product_id, company_id=move.company_id.id)
                if bom or bom.type == 'phantom':
                    phantom_moves |= move
                elif move.filtered(lambda x: x.product_id.bom_line_ids):
                    # Just product with route "Dropship"
                    if move.product_id.route_ids.mapped('pull_ids').filtered(lambda r: r.action == 'buy' and r.location_id.usage == 'customer'):
                        move.procurement_id.copy({
                            'product_id': move.product_id.id,
                            'product_qty': move.product_qty,
                            'product_uom': move.product_uom.id,
                            'rule_id': False
                        })
                        move.sudo().unlink()
                    else:
                        if move.product_id.qty_available_not_res >= move.product_uom_qty:
                            move.procure_method = 'make_to_stock'
                        phantom_moves |= move
                else:
                    phantom_moves |= move
            return phantom_moves
        return moves
