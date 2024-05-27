from odoo import models, fields, api
from dateutil import relativedelta
from datetime import date
from odoo.exceptions import ValidationError

class SesiUmroh(models.Model):
    _name                  = 'cdn.sesi.umroh'
    _description           = 'Sesi Umroh'
    _inherit               = ['mail.thread', 'mail.activity.mixin']

    name                   = fields.Char(string='Name', required=True)
    keterangan             = fields.Text(string='Description')
    paket_umroh_id         = fields.Many2one(comodel_name='cdn.paket.umroh', string='Paket Umroh')
    pembimbing_id          = fields.Many2one(comodel_name='cdn.ustadz.pembimbing', string='Pembimbing')
    petugas_lapangan       = fields.Many2many(comodel_name='cdn.petugas.lapangan', string='Petugas Lapangan')
    jammaah_ids            = fields.One2many('cdn.pendaftaran', 'sesi_id', string='jammaah', domain=lambda self: [('penagihan_ids.payment_state', '=', 'paid')])
    jumlah_jamaah          = fields.Char(compute='_compute_jml_jamaah', string='Jumlah Jamaah')
    state                  = fields.Selection([('akan_datang', 'Akan Datang'), ('proses', 'Sedang Berjalan'), ('selesai', 'Selesai'), ('batal_perjalanan', 'Perjalanan Batal'),], default="akan_datang", required=True, string="Status", tracking=True)
    tanggal_berangkat      = fields.Date(string='Tanggal Berangkat')
    durasi                 = fields.Integer(related='paket_umroh_id.durasi', string='Durasi Umroh (Hari)', store=True, compute='_compute_tanggal_pulang')
    tanggal_pulang         = fields.Date(string='Tanggal Pulang')
    rencana_perjalanan_ids = fields.Many2many(comodel_name='cdn.rencana.perjalanan', String="Itenerary")

    def write(self, values):
        res = super(SesiUmroh, self).write(values)
        if 'state' in values:
            for rec in self.rencana_perjalanan_ids:
                rec._compute_state()
        return res
        
    def action_akan_datang(self):
        for rec in self:
            rec.state = 'akan_datang'
    
    def action_proses(self):
        for rec in self:
            if rec.state == 'akan_datang':
                rec.state = 'proses'
    
    def action_selesai(self):
        for rec in self:
            rec.state = 'selesai'
    
    def action_batal_perjalanan(self):
        for rec in self:
            rec.state = 'batal_perjalanan'

    @api.depends('jammaah_ids')
    def _compute_jml_jamaah(self):
        for rec in self:
            rec.jumlah_jamaah = len(rec.jammaah_ids)
    
    @api.onchange('paket_umroh_id')
    def _onchange_paket_umroh_id(self):
        self.durasi = self.paket_umroh_id.durasi
     
    @api.onchange('tanggal_berangkat', 'durasi')
    def _compute_tanggal_pulang(self):
        for sesi in self:
            if sesi.tanggal_berangkat and sesi.durasi:
                durasi = relativedelta.relativedelta(days=sesi.durasi)
                sesi.tanggal_pulang = fields.Date.to_string(fields.Date.from_string(sesi.tanggal_berangkat) + durasi)