from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    jenis = fields.Selection(string='Jenis', selection=[('maskapai', 'Maskapai'), ('hotel', 'Hotel')])
    kelas = fields.Selection(string='Bintang', selection=[('bintang_0', 'Bintang 0'),('bintang_1', 'Bintang 1'), ('bintang_2', 'Bintang 2'), 
    ('bintang_3', 'Bintang 3'), ('bintang_4', 'Bintang 4'), ('bintang_5', 'Bintang 5'),], default='bintang_5')
    
    lokasi_hotel = fields.Float(string='Lokasi Hotel')