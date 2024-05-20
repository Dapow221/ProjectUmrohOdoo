from odoo import models, fields, api

class SesiUmroh(models.Model):
    _name = 'cdn.sesi.umroh'
    _description = 'Sesi Umroh'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
    paket_umroh_id = fields.Many2one(comodel_name='cdn.paket.umroh', string='Paket Umroh')
    pembimbing_id = fields.Many2one(comodel_name='res.users', string='Pembimbing')
    petugas_lapangan = fields.Many2many(comodel_name='res.users', string='Petugas Lapangan')
    #maskapai_id = fields.Many2one(comodel_name='cdn.maskapai', string='Maskapai')
    #hotel_id = fields.Many2one(comodel_name='cdn.hotel', string='Hotel')
    #jammah_ids = fields.Many2many(comodel_name='cdn.jamaah', string='Jamaah')
    jumlah_jamaah = fields.Integer(string='Jumlah Jamaah')
    
    
    

    
