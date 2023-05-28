from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    avg_cost_price = fields.Float(string='AVG Cost', digits='Product Price', help="AVG Cost Price from Purchase Order.",
                                  compute="_compute_avg_cost_price", store=False)

    def _compute_avg_cost_price(self):
        product = {}
        sql = """select pt.id, (sum(pol.price_unit)*sum(pol.product_qty))/sum(pol.product_qty) FROM product_template pt
            INNER JOIN product_product pp ON pp.product_tmpl_id = pt.id
            INNER JOIN purchase_order_line pol ON pol.product_id = pp.id
            WHERE pt.id in (%s)
            GROUP by pt.id;
        """ % str(self.ids).replace('[', '').replace(']', '')
        self.env.cr.execute(sql)
        for template_id, avg in self.env.cr.fetchall():
            product[template_id] = avg
        for record in self:
            record.avg_cost_price = product[record.id] if record.id in product else 0
