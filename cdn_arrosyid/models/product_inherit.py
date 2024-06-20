from odoo import models, fields, api

class ProductProduct(models.Model):
    _inherit       = 'product.product'

    paket_umroh    = fields.Boolean(string='Paket Umroh')
    paket_umroh_id = fields.Integer(string='')
    sesi_id        = fields.Integer(string='')