from odoo import models, fields, api, _



class CdnPendaftaran(models.Model):
    _name = 'cdn.pendaftaran'
    _description = 'Cdn Pendaftaran'

    no_pendaftaran = fields.Char(string='Nomor Pendaftaran')
    state = fields.Selection(string='Status', selection=[('draf', 'Draf'), ('batal', 'Batal'), ('konfirmasi', 'Kofirmasi'), ('selesai', 'Selesai'),], default="draf")
    
    # pilih_jamaah = fields.Selection(string='', selection=[('baru', 'Baru'), ('pilih', 'Pilih yang sudah terdaftar'),])
    jamaah_id = fields.Many2one('cdn.identitas.jamaah', string='Jamaah', required=True)
    # relatad jamaah
    nama = fields.Char(related='jamaah_id.name', string="Nama")
    jenis_kel = fields.Selection(related='jamaah_id.jenis_kel', string="Nama")
    referensi = fields.Char(related='jamaah_id.referensi')
    paspor = fields.Char(related='jamaah_id.paspor')
    masa_paspor = fields.Date(related='jamaah_id.masa_paspor')
    tgl_lahir = fields.Date(related='jamaah_id.tgl_lahir')
    umur = fields.Integer(related='jamaah_id.umur') 
    image = fields.Image(related='jamaah_id.image')
    is_menikah = fields.Boolean(related='jamaah_id.is_menikah')
    nama_pasangan = fields.Char(related='jamaah_id.nama_pasangan')
    riwayat_penyakit = fields.Char(related='jamaah_id.riwayat_penyakit')

    sesi_id = fields.Many2one('cdn.sesi.umroh', string='Sesi Umroh')
    # related sesi
    name_sesi = fields.Char(related='sesi_id.name', string="Nama")
    keterangan = fields.Text(related='sesi_id.keterangan')
    paket_umroh = fields.Char(related='sesi_id.paket_umroh_id.name', string="Nama Paket")
    pembimbing = fields.Char(related='sesi_id.pembimbing_id.name', string="Nama Pembimbing")
    petugas_lapangan = fields.Char(related='sesi_id.petugas_lapangan.name', string="Nama Petugas Lapangan")
    tanggal_berangkat = fields.Date(related='sesi_id.tanggal_berangkat')
    durasi = fields.Integer(related='sesi_id.durasi')
    tanggal_pulang = fields.Date(related='sesi_id.tanggal_pulang')
    
    # action button
    def action_draf(self):
        for rec in self:
            rec.state = 'draf'
    
    def action_batal(self):
        for rec in self:
            rec.state = 'batal'

    def action_konfirmasi(self):
        for rec in self:
            rec.state = 'konfirmasi'

    def action_selesai(self):
        for rec in self:
            rec.state = 'selesai'

    @api.model
    def create(self, vals):
        vals['no_pendaftaran'] = self.env['ir.sequence'].next_by_code('cdn.pendaftaran')
        return super(CdnPendaftaran, self).create(vals)

    def write(self, vals):
        if not self.no_pendaftaran and not vals.get('no_pendaftaran'):
            vals['no_pendaftaran'] = self.env['ir.sequence'].next_by_code('cdn.pendaftaran')
        return super(CdnPendaftaran, self).write(vals)
    
    def name_get(self):
        return [(record.id, "[%s] %s" % (record.no_pendaftaran, record.nama)) for record in self]