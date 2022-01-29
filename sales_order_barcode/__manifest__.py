# -*- coding: utf-8 -*-
# © 2022
#   @Lucky Kurniawan <kurniawanluckyy@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Sale Order Barcode",
    "summary": "Add Product With Barcode at Sale Order",
    "version": "15.0.1.0.0",
    "author": "Lucky Kurniawan ",
    "website": "https://github.com/kurniawanlucky/Odoo10.0",
    "category": "Sale",
    "depends": ['sale', 'barcodes', 'web'],
    "data": [
        'views/sale_order_views.xml',
    ],
    "assets": {
        "web.assets_backend": [
            "/sales_order_barcode/static/src/js/sale_barcode_handler.js"
        ],
    },
    "images": ['static/description/icon.png'],
    "license": "AGPL-3",
    "installable": True,
    "application": True,
}
