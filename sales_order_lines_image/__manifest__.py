# -*- coding: utf-8 -*-
# © 2021 Lucky Kurniawan <kurniawanluckyy@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Sales Order Line Product Image',
    'version': '1.1',
    'category': 'Sales Management',
    'description': """
Add Image For Order Lines.
==========================
Usage:
------
    * Install web_tree_image_tooltip(https://github.com/kurniawanlucky/web/tree/15.0 -> by OCA)
Feature:
--------
    * Add Image at sales order line
""",
    'author': 'Lucky Kurniawan',
    'website': '',
    'images': [],
    'depends': ['sale', 'web_tree_images_tooltip'],
    'data': [
        'views/sale_order_views.xml',
    ],
    'qweb': [],
    "images": ['static/description/icon.png'],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}