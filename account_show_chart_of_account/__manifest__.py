# -*- coding: utf-8 -*-
# © 2021 Lucky Kurniawan <kurniawanluckyy@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Accounting Show Menu Chart of Accounts(COA)',
    'version': '15.0.0.1',
    'category': 'Accounting/Accounting',
    'description': """
Invoice Show Menu Chart of Accounts.
====================================
Usage:
------
    * Just Install and you can see the menu of Chart of Accounts(COA)
    * Menu: go to Accounting ‣ Configuration ‣ Chart of Accounts
Feature:
--------
    * Show Menu Chart of Accounts(COA)
""",
    'author': 'Lucky Kurniawan(kurniawanluckyy@gmail.com)',
    'website': '',
    'images': [],
    'depends': ['account'],
    'data': [
        'views/account_menuitem.xml',
    ],
    'qweb': [],
    "images": ['static/description/icon.png'],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}