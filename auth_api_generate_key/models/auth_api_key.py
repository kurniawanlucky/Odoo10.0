from odoo import fields, models, api, _
import uuid


class AuthApiKey(models.Model):
    _inherit = 'auth.api.key'

    def _default_generate_key(self):
        return str(uuid.uuid4())

    key = fields.Char(required=True, help="""The API key. Enter a dummy value in this field if it is
            obtained from the server environment configuration.""", default=lambda self: self._default_generate_key())
