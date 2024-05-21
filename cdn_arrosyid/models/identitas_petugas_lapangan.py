from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime        import date


class PetugasLapangan(models.Model):
    _name        = 'cdn.petugas.lapangan'
    _description = 'Cdn Petugas Lapangan'
    _inherits    = {'res.partner':'partner_id'}
    
    partner_id       = fields.Many2one(comodel_name='res.partner', string='Nama Petugas Jamaah')
    jenis_kel        = fields.Selection(string='Jenis Kelamin', selection=[('l', 'Laki-laki'), ('p', 'Perempuan'),], default='l')
    referensi        = fields.Char(string='No Referensi')
    paspor           = fields.Char(string='Nomor Paspor', required=True)
    masa_paspor      = fields.Date(string='Masa berlaku Paspor', required=True)
    tgl_lahir        = fields.Date(string='Tanggal Lahir', required=True)
    umur             = fields.Integer(string='Umur', compute='_compute_umur') 
    image            = fields.Image(string='image',)
    status_petugas   = fields.Selection(string='Status Kesiapan Petugas', selection=[('siap', 'Siap'), ('sibuk', 'Sibuk'),], default='siap')
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

    @api.model
    def create(self, vals):
        vals['referensi'] = self.env['ir.sequence'].next_by_code('cdn.identitas.jamaah.petugas')
        return super(PetugasLapangan, self).create(vals)
    
    def write(self, vals):
        if not self.referensi and not vals.get('referensi'):
            vals['referensi'] = self.env['ir.sequence'].next_by_code('cdn.identitas.jamaah.petugas')
        return super(PetugasLapangan, self).write(vals)