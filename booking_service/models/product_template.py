from odoo import api, models, tools, fields


class ProductTemplate(models.Model):
    _inherit = "product.template"

    is_equipment = fields.Boolean('Is an Equipment')
