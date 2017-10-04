{
    'name': 'Product Image For Order Lines',
    'version': '1.1',
    'category': 'Sales Management',
    'description': """
Add Image For Order Lines.
====================================
Usage:
-----------------------
    * Install dusal_web_tree_image(by OCA)
Feauture:
-------------------------
    * Add Image at sales order line
""",
    'author': 'Lucky Kurniawan',
    'website': '',
    'images': [],
    'depends': ['sale', 'dusal_web_tree_image'],
    'data': [
        'views/sale_order_views.xml',
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
}