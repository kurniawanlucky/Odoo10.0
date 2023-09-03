# © 2022 Lucky Kurniawan <kurniawanluckyy@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Generate Key - Auth Api',
    'version': '15.0.0.1',
    'category': 'Security Management',
    'description': """
Security.
=========
Auth Api Key:
-------------
    * Generate key from Auth Api Key
""",
    'author': 'Lucky Kurniawan<kurniawanluckyy@gmail.com>',
    'website': '',
    'images': ['static/description/icon.png'],
    'depends': ['auth_api_key'],
    'data': [],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    "external_dependencies": {
        "python": [
            "uuid",
        ]
    },
}
