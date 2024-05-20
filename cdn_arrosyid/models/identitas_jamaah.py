from odoo            import models, fields, api, _
from datetime        import date
from dateutil        import relativedelta
from odoo.exceptions import ValidationError

class IdentitasJamaah(models.Model):
    _name            = 'cdn.identitas.jamaah' 
    _description     = 'Identitas Jamaah'
    _inherits        = {'res.partner':'partner_id'}

    partner_id       = fields.Many2one(comodel_name='res.partner', string='Nama Jamaah', required=True, ondelete="cascade")
    kategori         = fields.Selection(string='Jenis Jamaah', selection=[('peserta', 'Peserta Umroh'), ('petugas_lap', 'Petugas Lapangan'),('pembimbing', 'Ustadz Pembimbing')], default ='peserta')
    jenis_kel        = fields.Selection(string='Jenis Kelamin', selection=[('l', 'Laki-laki'), ('p', 'Perempuan'),], default='l')
    paspor           = fields.Char(string='Nomor Paspor', required=True)
    referensi        = fields.Char(string='No Referensi')
    masa_paspor      = fields.Date(string='Masa berlaku Paspor', required=True)
    tgl_lahir        = fields.Date(string='Tanggal Lahir', required=True)
    umur             = fields.Integer(string='Umur', compute='_compute_umur') 
    image            = fields.Image(string='image',)
    is_menikah       = fields.Boolean(string='Sudah menikah?', default = False)
    nama_pasangan    = fields.Char(string='Nama Pasangan')
    status_petugas   = fields.Selection(string='Status Petugas', selection=[('siap', 'Siap'), ('sibuk', 'Sibuk'),], default ='siap')
    riwayat_penyakit = fields.Char(string='Riwayat Penyakit')
    active           = fields.Boolean(string='Active', default= True)
    
    @api.depends('tgl_lahir')
    def _compute_umur(self):    
        for rec in self:
            today = date.today()
            if rec.tgl_lahir:
                rec.umur = today.year - rec.tgl_lahir.year
            else:
                rec.umur = 1
                
    @api.constrains('tgl_lahir')
    def _check_tgl_lahir(self):
        for rec in self:
            today = date.today()
            if rec.tgl_lahir and rec.tgl_lahir > today:
                raise ValidationError(_('Tanggal lahir yang dimasukkan tidak tepat!'))
    
                
    _sql_constraints = [
        ("paspor_unique", "unique(paspor)", "Nomor Paspor sudah tercatat"),
    ]
    
    @api.constrains('masa_paspor')
    def _check_masa_paspor(self):
        for rec in self:
            today = date.today()
            masa_berlaku_paspor = today - relativedelta.relativedelta(month=6)
            if rec.masa_paspor and rec.masa_paspor < masa_berlaku_paspor:
                raise ValidationError (_("Masa Berlaku Paspor harus lebih dari 6 bulan dari hari ini."))

    @api.model
    def create(self, vals):
        if vals['kategori'] == 'peserta':
            vals['referensi'] = self.env['ir.sequence'].next_by_code('cdn.identitas.jamaah.peserta')
        elif vals['kategori'] == 'petugas_lap':
            vals['referensi'] = self.env['ir.sequence'].next_by_code('cdn.identitas.jamaah.petugas')
        elif vals['kategori'] == 'pembimbing':
            vals['referensi'] = self.env['ir.sequence'].next_by_code('cdn.identitas.jamaah.pembimbing')
        return super(IdentitasJamaah, self).create(vals)
    
    def write(self, vals):
        if not self.referensi and not vals.get('referensi'):
            if vals['kategori'] == 'peserta':
                vals['referensi'] = self.env['ir.sequence'].next_by_code('cdn.identitas.jamaah.peserta')
            elif vals['kategori'] == 'petugas_lap':
                vals['referensi'] = self.env['ir.sequence'].next_by_code('cdn.identitas.jamaah.petugas')
            elif vals['kategori'] == 'pembimbing':
                vals['referensi'] = self.env['ir.sequence'].next_by_code('cdn.identitas.jamaah.pembimbing')
        return super(IdentitasJamaah, self).write(vals)