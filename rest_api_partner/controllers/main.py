from odoo.addons.base_rest.controllers import main


class PrivateApiController(main.RestController):
   _root_path = '/api/private/partner/'
   _collection_name = "private.partner.service"
