# -*- coding: utf-8 -*-
# © 2023
#   @Lucky Kurniawan <kurniawanluckyy@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Product Barcode Lookup",
    "version": "15.0.1.0.0",
    "author": "Lucky Kurniawan ",
    "website": "https://github.com/kurniawanlucky/Odoo10.0",
    "category": "Product",
    'description': """
Get product from barcode lookup.
================================
Barcode Lookup (https://www.barcodelookup.com/api)

Key Features
------------
* Search Product with barcode lookup
""",
    "depends": ['project'],
    "data": [
        'security/security.xml',
        'security/ir.model.access.csv',
        'wizard/wizard_barcode_lookup_views.xml',
        'views/barcode_lookup_views.xml',
    ],
    "images": ['static/description/icon.png'],
    "license": "AGPL-3",
    "installable": True,
    "application": True,
}
