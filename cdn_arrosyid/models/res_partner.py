from odoo import models, fields, api

class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    jenis = fields.Selection(string='Jenis', selection=[('maskapai', 'Maskapai'), ('hotel', 'Hotel'),])

    
