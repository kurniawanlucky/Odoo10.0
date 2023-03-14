# -*- coding: utf-8 -*-
# © 2023
#   @Lucky Kurniawan <kurniawanluckyy@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Project User Group",
    "version": "10.0.1.0.0",
    "author": "Lucky Kurniawan ",
    "website": "https://github.com/kurniawanlucky/Odoo10.0",
    "category": "Marketing/Events",
    'description': """
Organization and management of Daily Routine with User Group.
=============================================================

The event module allows you to efficiently organize project by user group

Key Features
------------
* Manage your Project with group
""",
    "depends": ['project'],
    "data": [
        'security/ir.model.access.csv',
        'views/project_user_group_views.xml',
        'views/project_views.xml',
        'views/project_task_views.xml',
    ],
    "images": [],
    "license": "AGPL-3",
    "installable": True,
    "application": True,
}
