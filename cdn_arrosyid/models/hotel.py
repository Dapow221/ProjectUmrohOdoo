from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class CdnHotel(models.Model):
    _name = 'cdn.hotel'
    _description = 'Hotel'
    _inherits={'res.company':'company_id'}


    company_id = fields.Many2one(comodel_name='res.company', string='Hotel')
    type = fields.Selection(string='Type Hotel', selection=[('bintang_1', 'Bintang 1'), ('bintang_2', 'Bintang 2'), 
    ('bintang_3', 'Bintang 3'), ('bintang_4', 'Bintang 4'), ('bintang_5', 'Bintang 5')], default='bintang_5')
    keterangan = fields.Text(string='Keterangan')  
    harga = fields.Monetary('Harga', currency_field='currency_id', required=True)
    currency_id = fields.Many2one('res.currency')
    street = fields.Char(related='company_id.street', string='Street', readonly=False)
    phone = fields.Char(related='company_id.phone', string='Phone', readonly=False)
    email = fields.Char(related='company_id.email', string='Email', readonly=False)
    city = fields.Char(related='company_id.city', string='Kota', readonly=False)
    zip = fields.Char(related='company_id.zip', string='Kode Pos', readonly=False)
    country_id = fields.Many2one('res.country', related='company_id.country_id', string='Negara', readonly=False)
    image = fields.Image('image')

    @api.constrains('harga')
    def _constrains_harga(self):
        for rec in self:
            if rec.harga < 0:
                raise ValidationError (_("Harga tidak valid!"))
    
    
    
    


    
