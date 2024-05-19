from odoo import models, fields, api


class IdentitasJamaah(models.Model):
    _name            = 'cdn.identitas.jamaah' 
    _description     = 'Identitas Jamaah'
    _inherits        = {'res.partner':'partner_id'}

    partner_id       = fields.Many2one(comodel_name='res.partner', string='Nama Jamaah', required=True, ondelete='cascade')
    kategori         = fields.Selection(string='Jenis Jamaah', selection=[('peserta', 'Peserta Umroh'), ('petugas_lap', 'Petugas Lapangan'),('penanggung_jawab', 'Penanggung Jawab')], default ='peserta')
    jenis_kel        = fields.Selection(string='Jenis Kelamin', selection=[('l', 'Laki-laki'), ('p', 'Perempuan'),], default='l')
    paspor           = fields.Integer(string='Nomor Paspor')
    masa_paspor      = fields.Date(string='Masa berlaku Paspor')
    # alamat           = fields.Text(string='Alamat') #ambil dari res.partner saja
    # no_hp = fields.Integer(string='Nomor Handphone') #ambil dari res.partner saja
    tgl_lahir        = fields.Date(string='Tanggal Lahir')
    umur             = fields.Integer(string='umur') #compute tgllahir
    is_menikah = fields.Boolean(string='Sudah menikah?', default = False)
    nama_pasangan    = fields.Char(string='Nama Pasangan')
    status_petugas   = fields.Selection(string='Status Petugas', selection=[('siap', 'Siap'), ('sibuk', 'Sibuk'),], default ='siap')
    riwayat_penyakit = fields.Char(string='Riwayat Penyakit')
    
    