from odoo import models, fields, api
from odoo.exceptions import ValidationError

class CdnRencanaPerjalanan(models.Model):
    _name         = 'cdn.rencana.perjalanan'
    _description  = 'Cdn Rencana Perjalanan'
    _rec_name     = 'nama'

    sesi_umroh_id = fields.Many2one('cdn.sesi.umroh', string='Sesi Umroh')
    nama          = fields.Char(string='Nama')
    keterangan    = fields.Text(string='Keterangan')
    dimulai       = fields.Date('Dimulai')
    durasi        = fields.Integer(string='Durasi')
    state         = fields.Selection([('batal', 'Batal'),('proses', 'Proses'),('selesai', 'selesai')], string='state', compute='_compute_state', store=True, default='proses')

    @api.depends('sesi_umroh_id.state')
    def _compute_state(self):
        for rec in self:
            if rec.sesi_umroh_id:
                if rec.sesi_umroh_id.state == 'proses':
                    rec.state = 'proses'
                elif rec.sesi_umroh_id.state == 'selesai':
                    rec.state = 'selesai'
                elif rec.sesi_umroh_id.state == 'batal_perjalanan':
                    rec.state = 'batal'
            else:
                rec.state = 'proses'
    
    @api.constrains('dimulai', 'sesi_umroh_id.tanggal_berangkat', 'sesi_umroh_id.tanggal_pulang')
    def _check_dates_within_range(self):
        for rec in self:
            if rec.dimulai:
                if rec.dimulai < rec.sesi_umroh_id.tanggal_berangkat or rec.dimulai > rec.sesi_umroh_id.tanggal_pulang:
                    raise ValidationError("Tanggal dimulai harus berada dalam rentang tanggal berangkat dan tanggal pulang sesi umroh.")

    def action_done(self):
        for rec in self:
            self.state = 'selesai'

    def action_cancel(self):
        for rec in self:
            self.state = 'batal'
    
    def action_proses(self):
        for rec in self:
            self.state = 'proses'