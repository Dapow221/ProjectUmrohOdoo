from odoo import models, fields, api
from dateutil import relativedelta
from datetime import date
from odoo.exceptions import ValidationError

class SesiUmroh(models.Model):
    _name                  = 'cdn.sesi.umroh'
    _description           = 'Sesi Umroh'
    _inherit               = ['mail.thread', 'mail.activity.mixin']
    _order                 = 'tanggal_berangkat asc'

    name                   = fields.Char(string='Name', required=True)
    keterangan             = fields.Text(string='Description')
    paket_umroh_id         = fields.Many2one(comodel_name='cdn.paket.umroh', string='Paket Umroh')
    lst_price              = fields.Float(string='Harga Paket',related='paket_umroh_id.lst_price', required=True, store=True)
    pembimbing_id          = fields.Many2one(comodel_name='cdn.ustadz.pembimbing', string='Pembimbing')
    petugas_lapangan       = fields.Many2many(comodel_name='cdn.petugas.lapangan', string='Petugas Lapangan')
    jammaah_ids            = fields.One2many('cdn.pendaftaran', 'sesi_id', string='jammaah')
    jumlah_jamaah          = fields.Char(compute='_compute_jml_jamaah', string='Jumlah Jamaah')
    state                  = fields.Selection([('akan_datang', 'Akan Datang'), ('proses', 'Sedang Berjalan'), ('selesai', 'Selesai'), ('batal_perjalanan', 'Perjalanan Batal'),], default="akan_datang", required=True, string="Status", tracking=True)
    tanggal_berangkat      = fields.Date(string='Tanggal Berangkat')
    durasi                 = fields.Integer(related='paket_umroh_id.durasi', string='Durasi Umroh (Hari)', store=True, compute='_compute_tanggal_pulang')
    tanggal_pulang         = fields.Date(string='Tanggal Pulang')
    rencana_perjalanan_ids = fields.One2many('cdn.rencana.perjalanan', 'sesi_umroh_id', string='rencana_perjalanan')
    maskapai_id            = fields.Many2one(related='paket_umroh_id.maskapai_id')
    hotel_id               = fields.Many2many(related='paket_umroh_id.hotel_id')
    proses_perjalanan      = fields.Float(compute='_compute_rencana_perjalanan_count', string='Proses Perjalanan (%)')
    company_id          = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)
    currency_id         = fields.Many2one('res.currency', related='company_id.currency_id', required=True)

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
                if not rec.jammaah_ids:
                    raise ValidationError('Tidak bisa memulai sesi karena belum memiliki jamaah yang telah membayar.')
                rec.state = 'proses'
    
    def action_selesai(self):
        for rec in self:
            if rec.rencana_perjalanan_ids.filtered(lambda x: x.state not in ['selesai', 'batal']):
                raise ValidationError("Tidak dapat menandai sesi umroh selesai karena ada perjalanan yang belum diselesaikan.")
            else:
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
                durasi = relativedelta.relativedelta(days=sesi.durasi - 1)
                sesi.tanggal_pulang = fields.Date.to_string(fields.Date.from_string(sesi.tanggal_berangkat) + durasi)

    @api.constrains('rencana_perjalanan_ids')
    def _check_rencana_perjalanan_dates(self):
        for session in self:
            for itinerary in session.rencana_perjalanan_ids:
                if itinerary.dimulai and (itinerary.dimulai < session.tanggal_berangkat or itinerary.dimulai > session.tanggal_pulang):
                    raise ValidationError("Tanggal dimulai rencana perjalanan harus berada dalam rentang tanggal berangkat dan tanggal pulang sesi umroh.")

    def _compute_rencana_perjalanan_count(self):
        for record in self:
            total_rencana = len(record.rencana_perjalanan_ids)
            proses_rencana = 0
            for dt_proses in record.rencana_perjalanan_ids:
                if dt_proses.state != 'proses':
                    proses_rencana += 1
            if proses_rencana > 0:
                persentase_rencana = (proses_rencana / total_rencana) * 100
            else:
                persentase_rencana = 0
            record.proses_perjalanan = persentase_rencana


    def action_lihat_perjalanan(self):
        action = {
            'name': 'Perjalanan Umroh',
            'type': 'ir.actions.act_window',
            'res_model': 'cdn.rencana.perjalanan',
            'view_mode': 'tree',
            'target': 'new',
            'view_id': self.env.ref('cdn_arrosyid.wizard_custom_rencana_perjalanan_view_tree').id,
            'domain': [('sesi_umroh_id', '=', self.id)],
        }
        return action
    
    def action_pilih_sesi(self):
        return