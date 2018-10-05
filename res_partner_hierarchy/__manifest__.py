# -*- coding: utf-8 -*-
# © 2017
#   @Lucky Kurniawan <kurniawanluckyy@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Customer Hierarchy",
    "version": "10.0.1.0.0",
    "author": "Lucky Kurniawan ",
    "website": "https://github.com/kurniawanlucky/Odoo10.0",
    "category": "Sales Management",
    'description': """
Customer Hierarchy.
----------------------

View:
- Sales > Sales > Customers Hierarchy
    
    """,
    "depends": ['sales_team'],
    "data": [
        'views/res_partner_views.xml',
    ],
    "images": ['static/description/icon.png'],
    "license": "AGPL-3",
    "installable": True,
    "application": True,
}
