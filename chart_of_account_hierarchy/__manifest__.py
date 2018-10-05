{
    'name': 'Chart of Account Hierarchy',
    'version': '1.1',
    'category': 'Accounting Management',
    'description': """
Use Chart of Account Hierarchy.
============================================

Usage:
-----------
- Add Parent Account at: Accounting > Adviser > Chart of Accounts > Parent Account

View:
--------
- Accounting > Adviser > Chart of Account Hierarchy

""",
    'author': 'Lucky Kurniawan',
    'website': '',
    'images': [],
    'depends': ['account'],
    'data': [
        'views/account_views.xml',
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}