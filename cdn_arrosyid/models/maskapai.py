from odoo import models, fields, api

class CdnMaskapai(models.Model):
    _name = 'cdn.maskapai'
    _description = 'Maskapai'
    _inherits={'res.company':'company_id'}

    company_id = fields.Many2one(comodel_name='res.company', string='Maskapai')
    keterangan = fields.Text(string='Keterangan')
    sesi_id = fields.Many2one(comodel_name='', string='Sesi Umroh')
    harga = fields.Monetary('Harga', currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', string='Currency')
    
    

    
    
