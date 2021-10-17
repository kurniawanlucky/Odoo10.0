# -*- coding: utf-8 -*-
# Copyright 2021 Lucky Kurniawan <kurniawanluckyy@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Product Image Url",
    "summary": "Product image from Url",
    "description": """
        This module show image from url.
    """,
    "version": "10.0.1.0.0",
    "author": "Lucky Kurniawan, ",
    "website": "https://github.com/kurniawanlucky/Odoo10.0",
    "category": "Product",
    "depends": ['product'],
    "data": [
        'views/product_template_views.xml',
    ],
    "license": "AGPL-3",
    "images": ['static/description/hidden_config.png'],
    "installable": True,
    "application": True,
}
