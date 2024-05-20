from odoo import models, fields, api


class CdnMaskapai(models.Model):
    _name = 'cdn.maskapai'
    _description = 'Maskapai'
    _inherits={'res.company':'company_id'}

    company_id = fields.Many2one(comodel_name='res.company', string='Maskapai')
    keterangan = fields.Text(string='Keterangan')
    sesi_id = fields.Many2one(comodel_name='cdn.paket.umroh', string='Sesi Umroh')
    harga = fields.Monetary('Harga', currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', string='Currency')
    street = fields.Char(related='company_id.street', string='Street', readonly=False)
    phone = fields.Char(related='company_id.phone', string='Phone', readonly=False)
    email = fields.Char(related='company_id.email', string='Email', readonly=False)
    city = fields.Char(related='company_id.city', string='Kota', readonly=False)
    zip = fields.Char(related='company_id.zip', string='Kode Pos', readonly=False)
    country_id = fields.Many2one('res.country',related='company_id.country_id', string='Negara', readonly=False)

    



    

    



    
    
    
    
    

    
    
