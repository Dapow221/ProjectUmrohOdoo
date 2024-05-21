from odoo import models, fields, api

class ProductProduct(models.Model):
    _inherit = 'product.product'

    product_travel = fields.Selection(string='Jenis', selection=[('non_status', 'Non Status'), ('konsumen', 'Konsumen'), ('pelayanan', 'Pelayanan'),], default='non_status')  