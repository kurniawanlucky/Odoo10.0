# -*- coding: utf-8 -*-
# Copyright 2017 Lucky Kurniawan <kurniawanluckyy@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Product Average Cost Price",
    "summary": "Product Average Cost Price from Purchase",
    "description": """
        This module calculate cost price from purchase.
    """,
    "version": "15.0.1.0.0",
    "author": "Lucky Kurniawan, ",
    "website": "https://github.com/kurniawanlucky/Odoo10.0",
    "category": "Product",
    "depends": ['purchase'],
    "data": [
        'views/product_template_views.xml',
    ],
    "license": "AGPL-3",
    "images": ['static/description/hidden_config.png'],
    "installable": True,
    "application": True,
}
