# -*- coding: utf-8 -*-
# Copyright 2017 Lucky Kurniawan <kurniawanluckyy@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Hide Cost Price and Sale Price of product",
    "summary": "Hide product cost price and sale price",
    "description": """
        This module hide product sale price or cost price.
    """,
    "version": "15.0.1.0.0",
    "author": "Lucky Kurniawan, ",
    "website": "https://github.com/kurniawanlucky/Odoo10.0",
    "category": "Product",
    "depends": ['base', 'product'],
    "data": [
        'security/product_security.xml',
        'views/product_template_views.xml',
        'views/product_views.xml',
    ],
    "license": "AGPL-3",
    "images": ['static/description/hidden_config.png'],
    "installable": True,
    "application": True,
}
