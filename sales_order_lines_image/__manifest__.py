{
    'name': 'Sales Order Line Product Image',
    'version': '1.1',
    'category': 'Sales Management',
    'description': """
Add Image For Order Lines.
====================================
Usage:
-----------------------
    * Install web_tree_image(by OCA)
Feauture:
-------------------------
    * Add Image at sales order line
""",
    'author': 'Lucky Kurniawan',
    'website': '',
    'images': [],
    'depends': ['sale', 'web_tree_image'],
    'data': [
        'views/sale_order_views.xml',
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
}