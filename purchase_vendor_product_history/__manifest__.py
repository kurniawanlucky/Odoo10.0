# © 2022 Lucky Kurniawan <kurniawanluckyy@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Purchase Vendor Product History',
    'version': '15.0.0.1',
    'category': 'Purchase Management',
    'description': """
Purchase Order.
===============
Purchase Vendor Product History:
--------------------------------
    * Show all Purchase History Transaction
""",
    'author': 'Lucky Kurniawan<kurniawanluckyy@gmail.com>',
    'website': '',
    'images': ['static/description/icon.png'],
    'depends': ['purchase'],
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
