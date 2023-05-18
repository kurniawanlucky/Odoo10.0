from odoo import models, fields, api


class IrCron(models.Model):
    _inherit = "ir.cron"

    cron_history_ids = fields.One2many("ir.cron.history", "cron_id")

    @classmethod
    def _process_job(cls, db, cron_cr, job):
        start_time = fields.Datetime.now()
        try:
            res = super(IrCron, cls)._process_job(db, cron_cr, job)
        finally:
            end_time = fields.Datetime.now()
            query = """
                INSERT INTO ir_cron_history (cron_id, start_time, finish_time) 
                VALUES (%s, '%s', '%s');
            """ % (job['id'], start_time, end_time)
            cron_cr.execute(query)
            cron_cr.commit()
        return res
