from odoo import models, fields, api

class SesiUmroh(models.Model):
    _name = 'cdn.sesi.umroh'
    _description = 'Sesi Umroh'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
    paket_umroh_id = fields.Many2one(comodel_name='cdn.paket.umroh', string='Paket Umroh')
    pembimbing_id = fields.Many2one(comodel_name='res.users', string='Pembimbing')
    petugas_lapangan = fields.Many2many(comodel_name='res.users', string='Petugas Lapangan')
    maskapai_id = fields.Many2one(comodel_name='res.company', string='Maskapai')
    hotel_id = fields.Many2one(comodel_name='res.company', string='Hotel')
    jammaah_ids = fields.Many2many(comodel_name='res.partner', string='Jamaah')
    jumlah_jamaah = fields.Integer(string='Jumlah Jamaah')
    rencana_perjalanan_ids = fields.One2many('cdn.rencana.perjalanan', 'sesi_umroh_id', string='rencana_perjalanan')
    
    
    

    
