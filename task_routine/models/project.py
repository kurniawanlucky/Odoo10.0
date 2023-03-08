from odoo import _, fields, models


class RoutineTask(models.Model):
    _inherit = 'project.project'

    recurrence_id = fields.Many2one('project.task.recurrence', copy=False)
    user_ids = fields.Many2many('res.users', relation='project_user_rel', column1='project_id', column2='user_id',
                                string='Assignees', context={'active_test': False}, tracking=True)

    def run_manually_task(self):
        self.check_access_rights('write')
        return True

    def _new_task_values(self):
        val = {
            'name': self.name,
            'description': self.description,
            'project_id': self.id,
            'user_ids': [(6, 0, self.user_ids.ids)],
            'stage_id': self.type_ids[0].id if self.type_ids else False
        }
        return val
