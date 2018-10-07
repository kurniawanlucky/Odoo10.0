# -*- coding: utf-8 -*-
{
    'name': 'Pivot Search By Range',
    'version': '1.1',
    'category': 'web',
    'summary': 'Pivot view Search by range',
    'website': "https://github.com/kurniawanlucky/Odoo10.0",
    'description': """
        This module Add search by range.
    """,
    'author': 'Lucky Kurniawan(kurniawanluckyy@gmail.com)',
    'depends': ['web'],
    'data': [
        'views/template_views.xml',
    ],
    'qweb': [
        'static/src/xml/pivot_views.xml',
    ],
    'license': "AGPL-3",
    'images': ['static/description/pivot_search_with_range.png'],
    'installable': True,
    'auto_install': False,
    'application': True,
}
