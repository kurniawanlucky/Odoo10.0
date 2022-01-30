# -*- coding: utf-8 -*-
# © 2022
#   @Lucky Kurniawan <kurniawanluckyy@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Purchase Barcode",
    "summary": "Add Product With Barcode at Purchase Order",
    "version": "15.0.1.0.0",
    "author": "Lucky Kurniawan",
    "website": "https://github.com/kurniawanlucky/Odoo10.0",
    "category": "Purchase",
    "depends": ['purchase', 'barcodes'],
    "data": [
        'views/purchase_order_views.xml',
    ],
    "assets": {
        "web.assets_backend": [
            "/purchase_order_barcode/static/src/js/purchase_barcode_handler.js"
        ],
    },
    "images": ['static/description/icon.png'],
    "license": "AGPL-3",
    "installable": True,
    "application": True,
}
