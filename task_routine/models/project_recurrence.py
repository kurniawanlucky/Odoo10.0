from odoo import _, fields, models
from dateutil.relativedelta import relativedelta


class ProjectTaskRecurrence(models.Model):
    _inherit = 'project.task.recurrence'

    name = fields.Char(string='Name')
    project_ids = fields.One2many('project.project', 'recurrence_id', copy=False)

    def _create_next_task(self):
        super(ProjectTaskRecurrence, self)._create_next_task()
        for recurrence in self:
            projects = recurrence.sudo().project_ids
            for project in projects:
                project_task_id = self.env['project.task'].search([('project_id', '=', project.id), ('user_ids', '=', project.user_ids.ids)], limit=1)
                if project_task_id:
                    stage_id = project.type_ids[0].id if project.type_ids else False
                    project_task_id.write({'stage_id': stage_id})
                else:
                    create_values = project._new_task_values()
                    self.env['project.task'].sudo().create(create_values)
