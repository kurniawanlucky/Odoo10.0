from marshmallow import fields
from odoo.addons.datamodel.core import Datamodel


class PartnerInfo(Datamodel):
    _name = "partner.info"

    id = fields.Integer()
    name = fields.String()
    email = fields.String()
