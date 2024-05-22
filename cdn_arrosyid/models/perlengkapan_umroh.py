from odoo import models, fields, api


class Perlengkapan(models.Model):
    _inherit = 'product.product'

    perlengkapan_umroh = fields.Selection(string='Jenis Perlengkapan Umroh', selection=[('konsumsi_umroh', 'Konsumsi Training'), ('peralatan_umroh', 'Perlatan Training')])
    
