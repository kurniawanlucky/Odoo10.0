{
    'name': 'Progress Delivery on Sales Order',
    'version': '1.1',
    'category': 'Sales Management',
    'description': """
Add Progres information to the sales order.
    * Add Information About Delivery Progress at sale order Tree
""",
    'author': 'Lucky Kurniawan',
    'website': '',
    'images': [],
    'depends': ['sale_stock', 'sale_order_dates'],
    'data': [
        'views/sale_order_views.xml',
    ],
    'demo': [],
    'test': [],
    'installable': False,
    'auto_install': False,
    'application': True,
}