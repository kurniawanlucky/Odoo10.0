# -*- coding: utf-8 -*-
# Copyright 2017 Lucky Kurniawan <kurniawanluckyy@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Product Group by Supplier",
    "summary": "Product Group by Supplier",
    "description": """
        This module Add group by supplier.
    """,
    "version": "10.0.1.0.0",
    "author": "Lucky Kurniawan",
    "website": "https://github.com/kurniawanlucky/Odoo10.0",
    "category": "Product",
    "depends": ['product'],
    "data": [
        'views/product_views.xml',
    ],
    "license": "AGPL-3",
    "images": ['static/description/icon.png'],
    "installable": True,
    "application": True,
}
