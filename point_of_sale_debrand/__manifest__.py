# -*- coding: utf-8 -*-
{
    'name': 'POS(Point of Sale) Debrand',
    'version': '1.1',
    'category': 'web',
    'summary': 'POS(Point of Sale) Debrand',
    'website': "https://github.com/kurniawanlucky/Odoo10.0",
    'description': """
        This module Change Odoo logo with company logo / Change logo in POS to company logo.
    """,
    'author': 'Lucky Kurniawan(kurniawanluckyy@gmail.com)',
    'depends': ['point_of_sale'],
    'data': [],
    'qweb': [
        'static/src/xml/base.xml',
    ],
    'license': "AGPL-3",
    'images': ['static/description/pos_debrand.png'],
    'installable': False,
    'auto_install': False,
    'application': True,
}
