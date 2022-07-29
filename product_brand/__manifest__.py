# -*- coding: utf-8 -*-
# © 2017
#   @Lucky Kurniawan <kurniawanluckyy@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Product Brand",
    "version": "10.0.1.0.0",
    "author": "Lucky Kurniawan ",
    "website": "https://github.com/kurniawanlucky/Odoo10.0",
    "category": "Product",
    'description': """
Product Brand.
--------------
* Add Brand at product

Setting:
- Sales > Configuration > Products > Product Brands

    """,
    "depends": ['sales_team'],
    "data": [
        'views/product_brand_views.xml',
        'views/product_template_views.xml',
    ],
    "images": [],
    "license": "AGPL-3",
    "installable": True,
    "application": True,
}
