from odoo import models, fields, api



class CdnRencanaPerjalanan(models.Model):
    _name = 'cdn.rencana.perjalanan'
    _description = 'Cdn Rencana Perjalanan'
    _rec_name = 'nama'

    sesi_umroh_id = fields.Many2one('cdn.sesi.umroh', string='sesi_umroh')
    nama = fields.Char(string='Nama')
    keterangan = fields.Text(string='Keterangan')
    dimulai = fields.Date('Dimulai')
    durasi = fields.Float(string='Durasi')
    state = fields.Selection([('batal', 'Batal'),('belum', 'Belum'),('proses', 'Proses'),('selesai', 'selesai')], string='state')
    
