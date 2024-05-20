from odoo import models, fields, api



class CdnHotel(models.Model):
    _name = 'cdn.hotel'
    _description = 'Hotel'
    _inherits={'res.company':'company_id'}

    company_id = fields.Many2one(comodel_name='res.company', string='Hotel')
    type = fields.Selection(string='Type Hotel', selection=[('bintang_1', 'Bintang 1'), ('bintang_2', 'Bintang 2'), 
    ('bintang_3', 'Bintang 3'), ('bintang_4', 'Bintang 4'), ('bintang_5', 'Bintang 5')])
    keterangan = fields.Text(string='Keterangan')  
    harga = fields.Monetary('Harga', currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', string='Currency')