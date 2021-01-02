# -*- coding: utf-8 -*-
# © 2021 Lucky Kurniawan <kurniawanluckyy@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Putaway strategy per product',
    'summary': 'Set a product location and put-away strategy per product',
    'version': '10.0.1.0.1',
    'category': 'Inventory',
    'website': 'https://github.com/kurniawanlucky/Odoo10.0',
    'author': 'Lucky Kurniawan(kurniawanluckyy@gmail.com)',
    'license': 'AGPL-3',
    'depends': [
        'product',
        'stock'
    ],
    'data': [
        'views/product_template_views.xml',
    ],
    'demo': [],
    'images': ['static/description/icon.png'],
    'installable': True,
    'auto_install': False,
    'application': True,
}
