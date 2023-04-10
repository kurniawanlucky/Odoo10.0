from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class BarcodeLookup(models.Model):
    _name = "barcode.lookup"
    _description = "Search Product with Barcode lookup"
    _order = "name"

    url = fields.Char('Url', required=True, default="https://api.barcodelookup.com/v3/products")
    name = fields.Char('Name', index=True, required=True)
    api_key = fields.Char('Api Key', required=True)
    search_column = fields.Selection([
        ("barcode", "Barcode"),
        ("mpn", "MPN"),
        ("asin", "ASIN"),
        ("title", "Title"),
        ("category", "Category"),
        ("manufacturer", "Manufacturer"),
        ("brand", "Brand"),
        ("search", "Search"),
    ], string="Search Column")
