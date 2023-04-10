from odoo import api, fields, models
from urllib.parse import urlencode
import requests
import json


class WizardBarcodeLookup(models.TransientModel):
    _name = 'wizard.barcode.lookup'

    wizard_barcode_lookup_value_ids = fields.One2many("wizard.barcode.lookup.value", "wizard_id")
    barcode_val = fields.Char('Barcode')
    mpn_val = fields.Char('MPN')
    asin_val = fields.Char('Asin')
    title_val = fields.Char('Title')
    category_val = fields.Char('Category')
    manufacturer_val = fields.Char('Manufacturer')
    brand_val = fields.Char('Brand')
    search_val = fields.Char('Search')

    def action_search_product(self):
        search = {}
        barcode_lookup_id = self.env['barcode.lookup'].search([], limit=1)
        if self.barcode_val:
            search.update({'barcode': self.barcode_val})
        if self.mpn_val:
            search.update({'mpn': self.mpn_val})
        if self.asin_val:
            search.update({'asin': self.asin_val})
        if self.title_val:
            search.update({'title': self.title_val})
        if self.category_val:
            search.update({'category': self.category_val})
        if self.manufacturer_val:
            search.update({'manufacturer': self.manufacturer_val})
        if self.brand_val:
            search.update({'brand': self.brand_val})
        if self.search_val:
            search.update({'search': self.search_val})
        search.update({'key': barcode_lookup_id.api_key})
        params = urlencode(search)
        response = requests.get(barcode_lookup_id.url, params=params)
        values = json.loads(response.text)
        datas = []
        for value in values.get('products'):
            data = (0, 0, {
                'barcode': value.get('barcode_number'),
                'barcode_formats': value.get('barcode_formats'),
                'mpn': value.get('mpn'),
                'model': value.get('model'),
                'asin': value.get('asin'),
                'title': value.get('title'),
                'category': value.get('category'),
                'manufacturer': value.get('manufacturer'),
                'brand': value.get('brand'),
                'contributors': ','.join(value.get('contributors')),
                'age_group': value.get('age_group'),
                'ingredients': value.get('ingredients'),
                'nutrition_facts': value.get('nutrition_facts'),
                'energy_efficiency_rating': value.get('energy_efficiency_class'),
                'color': value.get('color'),
                'gender': value.get('gender'),
                'material': value.get('material'),
                'pattern': value.get('pattern'),
                'multipack': value.get('multipack'),
                'size': value.get('size'),
                'length': value.get('length'),
                'width': value.get('width'),
                'height': value.get('height'),
                'weight': value.get('weight'),
                'release_date': value.get('release_date'),
                'description': value.get('description'),
                'features': ','.join(value.get('features')),
                'images': ','.join(value.get('images')),
                'last_update': value.get('last_update'),
                'reviews': ','.join(value.get('reviews')),
            })
            datas.append(data)
        self.wizard_barcode_lookup_value_ids = datas
