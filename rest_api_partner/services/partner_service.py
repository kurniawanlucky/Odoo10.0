from odoo.addons.base_rest import restapi
from odoo.addons.base_rest_datamodel.restapi import Datamodel
from odoo.addons.component.core import Component


class PartnerService(Component):
    _inherit = "base.rest.service"
    _name = "partner.service"
    _usage = "partner"
    _collection = "private.partner.service"

    def response(self, type, reason):
        return {
            type: reason
        }

    @restapi.method([(["/<int:id>/change_name"], "POST")],
                    input_param=restapi.CerberusValidator("_get_partner_schema"),
                    auth="api_key")
    def update_name(self, partner_id, **params):
        partner = self.env['res.partner'].browse(partner_id)
        if not partner:
            return self.response('error', 'Partner not found')
        partner.write(params)
        return self.response('success', 'Partner already updated')

    def _get_partner_schema(self):
        return {
            "name": {"type": "string", "required": True}
        }

    @restapi.method([(['/search'], 'GET')],
                    input_param=Datamodel('partner.input'),
                    output_param=Datamodel("partner.info", is_list=True),
                    auth='api_key',)
    def search(self, body):
        partner_obj = self.env['res.partner']
        res = []
        partner_short_info = self.env.datamodels["partner.info"]
        if body.name:
            partner_ids = partner_obj._name_search(body.name)
        if body.id:
            partner_ids = body.id
        partner_ids = partner_obj.browse(partner_ids)
        for partner in partner_ids:
            res.append(partner_short_info(id=partner.id, name=partner.name, email=partner.email))
        return res
