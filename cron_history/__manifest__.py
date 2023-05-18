# © 2022 Lucky Kurniawan <kurniawanluckyy@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Cron History',
    'version': '15.0.0.1',
    'category': 'Cron Management',
    'description': """
Cron.
======
Cron History:
-------------
    * Show all History from Cron
""",
    'author': 'Lucky Kurniawan<kurniawanluckyy@gmail.com>',
    'website': '',
    'images': ['static/description/icon.png'],
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/ir_cron_views.xml',
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
