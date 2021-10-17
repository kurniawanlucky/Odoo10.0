import requests
import base64
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class ProductImage(models.Model):
    _inherit = 'product.template'

    image_url = fields.Char(string='Image URL')

    # @api.multi
    # def add_image_url(self):
    #     return {
    #         'name': _('Add image Url'),
    #         'view_type': 'form',
    #         'view_mode': 'form',
    #         'res_model': 'product.template',
    #         'view_id': self.env.ref('product_images_url.product_template_image_url_form').id,
    #         'type': 'ir.actions.act_window',
    #         'target': 'new',
    #         'res_id': self.id,
    #         'context': {
    #             'active_id': self.id,
    #             'edit': True,
    #             'create': False,
    #         }
    #     }

    @api.onchange('image_url')
    def _onchange_image_url(self):
        image = False
        try:
            if self.image_url:
                image = base64.b64encode(requests.get(self.image_url).content)
            self.image_medium = image
        except:
            raise UserError(_("Please provide correct URL or check your image size!"))
