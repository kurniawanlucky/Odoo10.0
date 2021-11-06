# -*- coding: utf-8 -*-
# © 2017
#   @Lucky Kurniawan <kurniawanluckyy@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Customer City",
    "version": "10.0.1.0.0",
    "author": "Lucky Kurniawan ",
    "website": "https://github.com/kurniawanlucky/Odoo10.0",
    "category": "Partner Management",
    'description': """
Customer City.
--------------
- Add city inside country

Add City:
- Sales > Configuration > Contact > Localization > Country

    """,
    "depends": ['base', 'sales_team'],
    "data": [
        'views/country_views.xml',
        'views/res_partner_views.xml',
        'views/res_city_views.xml',
    ],
    "images": [''],
    "license": "AGPL-3",
    "installable": True,
    "application": True,
}
