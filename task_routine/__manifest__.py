# -*- coding: utf-8 -*-
# © 2023
#   @Lucky Kurniawan <kurniawanluckyy@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Routine Organization',
    'version': '1.1',
    'website': 'https://www.odoo.com/app/events',
    'category': 'Marketing/Events',
    'summary': 'Trainings, Conferences, Meetings, Exhibitions, Registrations',
    'author': 'Lucky Kurniawan <kurniawnaluckyy@gmail.com>',
    'description': """
Organization and management of Daily Routine.
=============================================

The event module allows you to efficiently organize routine and all related tasks: planning, registration tracking,
attendances, etc.

Key Features
------------
* Manage your Routine and Registrations
""",
    'depends': ['project'],
    'data': [
        'data/task_recurrence_data.xml',
        'security/task_security.xml',
        'security/ir.model.access.csv',
        'views/routine_menu_views.xml',
        'views/task_recurrence_views.xml',
        'views/project_views.xml',
        'views/project_task_views.xml',
        'views/project_task_type_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
