# -*- coding: utf-8 -*-
{
    'name': 'Tree or List Search Date By Range',
    'version': '1.1',
    'category': 'web',
    'summary': 'Tree or List view Search Date by range',
    'website': "https://github.com/kurniawanlucky/Odoo10.0",
    'description': """
        This module Add search date by range.
    """,
    'author': 'Lucky Kurniawan(kurniawanluckyy@gmail.com)',
    'depends': ['web'],
    'data': [
        'views/template_views.xml',
    ],
    'qweb': [
        'static/src/xml/tree_views.xml',
    ],
    'license': "AGPL-3",
    'images': ['static/description/tree_search_with_range.png'],
    'installable': True,
    'auto_install': False,
    'application': True,
}
