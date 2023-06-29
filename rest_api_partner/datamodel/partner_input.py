from marshmallow import fields
from odoo.addons.datamodel.core import Datamodel


class PartnerInput(Datamodel):
    _name = "partner.input"

    name = fields.String()
