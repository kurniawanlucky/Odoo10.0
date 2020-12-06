# -*- coding: utf-8 -*-
# © 2020
#   @Lucky Kurniawan <kurniawanluckyy@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Booking Service",
    "version": "10.0.0",
    "category": "Other",
    "summary": "",
    "description": """
To allow users to create bookings for employees and equipments.
""",
    "author": "Lucky Kurniawan",
    "website": "https://github.com/kurniawanlucky/Odoo10.0",
    "images": [],
    "depends": ["calendar", "hr", "sales_team", "stock"],
    "data": [
        'data/module_data.xml',
        'security/booking_security.xml',
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'wizard/wizard_booking_sale_views.xml',
        'views/booking_views.xml',
        'views/calendar_event_views.xml',
        'views/hr_employee_views.xml',
        'views/product_template_views.xml',
        'views/sale_order_views.xml',
        'views/stock_production_lot_views.xml',
        'views/team_views.xml',
        'views/stock_picking_views.xml',
    ],
    "images": [],
    "demo": [],
    "test": [],
    "currency": "EUR",
    "license": "AGPL-3",
    "images": ['static/description/icon.png'],
    "installable": True,
    "application": True,
}
