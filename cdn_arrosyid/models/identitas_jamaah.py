from odoo     import models, fields, api
from datetime import date

class IdentitasJamaah(models.Model):
    _name            = 'cdn.identitas.jamaah' 
    _description     = 'Identitas Jamaah'
    _inherits        = {'res.partner':'partner_id'}

    partner_id       = fields.Many2one(comodel_name='res.partner', string='Nama Jamaah', required=True, ondelete="cascade")
    kategori         = fields.Selection(string='Jenis Jamaah', selection=[('peserta', 'Peserta Umroh'), ('petugas_lap', 'Petugas Lapangan'),('penanggung_jawab', 'Penanggung Jawab')], default ='peserta')
    jenis_kel        = fields.Selection(string='Jenis Kelamin', selection=[('l', 'Laki-laki'), ('p', 'Perempuan'),], default='l')
    paspor           = fields.Char(string='Nomor Paspor', required=True)
    masa_paspor      = fields.Date(string='Masa berlaku Paspor')
    tgl_lahir        = fields.Date(string='Tanggal Lahir')
    umur             = fields.Integer(string='Umur', compute='_compute_umur') #compute tgllahir
    is_menikah       = fields.Boolean(string='Sudah menikah?', default = False)
    nama_pasangan    = fields.Char(string='Nama Pasangan')
    status_petugas   = fields.Selection(string='Status Petugas', selection=[('siap', 'Siap'), ('sibuk', 'Sibuk'),], default ='siap')
    riwayat_penyakit = fields.Char(string='Riwayat Penyakit')

    
    @api.depends('tgl_lahir')
    def _compute_umur(self):
        for rec in self:
            today = date.today()
            if rec.tgl_lahir:
                rec.umur = today.year - rec.tgl_lahir.year
            else:
                rec.umur = 1
    
    _sql_constraints = [
        ("paspor_unique", "unique(paspor)", "Nomor Paspor sudah tercatat"),
    ]