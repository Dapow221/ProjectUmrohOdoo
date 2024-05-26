from odoo import models, fields, api

class CdnRencanaPerjalanan(models.Model):
    _name = 'cdn.rencana.perjalanan'
    _description = 'Cdn Rencana Perjalanan'
    _rec_name = 'nama'

    sesi_umroh_id = fields.Many2one('cdn.sesi.umroh', string='Sesi Umroh')
    nama = fields.Char(string='Nama')
    keterangan = fields.Text(string='Keterangan')
    dimulai = fields.Date('Dimulai')
    durasi  = fields.Integer(related='sesi_umroh_id.durasi', string='Durasi Umroh (Hari)')
    state = fields.Selection([('batal', 'Batal'),('belum', 'Belum'),('proses', 'Proses'),('selesai', 'selesai')], string='state', compute='_compute_state', store=True)

    @api.depends('sesi_umroh_id.state')
    def _compute_state(self):
        for rec in self:
            if rec.sesi_umroh_id:
                if rec.sesi_umroh_id.state == 'akan_datang':
                    rec.state = 'belum'
                elif rec.sesi_umroh_id.state == 'prosess':
                    rec.state = 'proses'
                elif rec.sesi_umroh_id.state == 'selesai':
                    rec.state = 'selesai'
                elif rec.sesi_umroh_id.state == 'batal_perjalanan':
                    rec.state = 'batal'
            else:
                rec.state = 'belum'
    
    