# © 2022 Lucky Kurniawan <kurniawanluckyy@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Sale Customer History - Sale Order',
    'version': '15.0.0.1',
    'category': 'Sale Management',
    'description': """
Sale Order.
===========
Sale Customer History:
----------------------
    * Show all History Transaction Customer at Sales Order Tab Page
""",
    'author': 'Lucky Kurniawan<kurniawanluckyy@gmail.com>',
    'website': '',
    'images': ['static/description/icon.png'],
    'depends': ['sale'],
    'data': [
        'views/res_partner_views.xml',
    ],
    'demo': [],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
