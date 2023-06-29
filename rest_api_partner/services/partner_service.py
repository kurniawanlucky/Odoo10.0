from odoo.addons.base_rest import restapi
from odoo.addons.base_rest_datamodel.restapi import Datamodel
from odoo.addons.component.core import Component


class PartnerService(Component):
    _inherit = "base.rest.service"
    _name = "partner.service"
    _usage = "partner"
    _collection = "private.partner.service"

    @restapi.method([(['/search'], 'GET')],
                    input_param=Datamodel('partner.input'),
                    output_param=Datamodel("partner.info", is_list=True),
                    auth='api_key',)
    def search(self, body):
        partner_obj = self.env['res.partner']
        res = []
        partner_short_info = self.env.datamodels["partner.info"]
        partner_ids = partner_obj._name_search(body.name)
        partner_ids = partner_obj.browse(partner_ids)
        for partner in partner_ids:
            res.append(partner_short_info(id=partner.id, name=partner.name, email=partner.email))
        return res
