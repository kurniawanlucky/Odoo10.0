from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo import api, fields, models, _
from datetime import datetime, timedelta


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_image = fields.Binary(
        "image", related='product_id.product_tmpl_id.image_small',
        help="Small-sized image of the product. It is automatically "
             "resized as a 64x64px image, with aspect ratio preserved. "
             "Use this field anywhere a small image is required.")

