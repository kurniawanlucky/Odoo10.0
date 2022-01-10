{
    'name': 'Sales Purchase Button Plus Minus Quantity',
    'version': '1.1',
    'category': 'Sales Management',
    'description': """
Add Button to Sales And Purchase.
    * Add Button + and - at sales order line for qty
    * Add Button + and - at Purcase order line for qty
""",
    'author': 'Lucky Kurniawan',
    'website': '',
    'images': [],
    'depends': ['purchase','sale'],
    'data': [
        'views/sale_views.xml',
        'views/purchase_views.xml',
    ],
    'demo': [],
    'test': [],
    'installable': False,
    'auto_install': False,
    'application': True,
}