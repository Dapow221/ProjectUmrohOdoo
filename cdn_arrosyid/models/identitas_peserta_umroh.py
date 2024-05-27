from odoo            import models, fields, api, _
from datetime        import date
# from dateutil        import relativedelta
from odoo.exceptions import ValidationError

class IdentitasJamaah(models.Model):
    _name            = 'cdn.identitas.jamaah' 
    _description     = 'Identitas Jamaah'
    _inherits        = {'res.partner':'partner_id'}

    partner_id       = fields.Many2one(comodel_name='res.partner', string='Nama Jamaah', required=True, ondelete="cascade")
    jenis_kel        = fields.Selection(string='Jenis Kelamin', selection=[('l', 'Laki-laki'), ('p', 'Perempuan'),], default='l')
    referensi        = fields.Char(string='No Referensi')
    paspor           = fields.Char(string='Nomor Paspor', required=True)
    masa_paspor      = fields.Date(string='Masa berlaku Paspor', required=True)
    tgl_lahir        = fields.Date(string='Tanggal Lahir', required=True)
    umur             = fields.Integer(string='Umur', compute='_compute_umur') 
    image            = fields.Image(string='image',)
    is_menikah       = fields.Boolean(string='Sudah menikah', default = False)
    nama_pasangan    = fields.Char(string='Nama Pasangan')
    riwayat_penyakit = fields.Char(string='Riwayat Penyakit')
    active           = fields.Boolean(string='Active', default= True)
    pendaftaran_ids  = fields.One2many('cdn.pendaftaran', 'jamaah_id', string='Pendaftaran')
    jumlah_pendaftaran = fields.Integer(string='Jumlah pendaftaran ', compute="_compute_jumlah_pendaftaran")
    penagihan_ids    = fields.One2many('account.move', 'partner_id', string='Penagihan')
    jumlah_penagihan = fields.Integer(string='Jumlah penagihan ', compute="_compute_jumlah_penagihan")
    lunas = fields.Char(string='Lunas')
    
    
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
    
    # @api.constrains('masa_paspor')
    # def _check_masa_paspor(self):
    #     for rec in self:
    #         today = date.today()
    #         masa_berlaku_paspor = today - relativedelta.relativedelta(month=6)
    #         if rec.masa_paspor and rec.masa_paspor < masa_berlaku_paspor:
    #             raise ValidationError (_("Masa Berlaku Paspor harus lebih dari 6 bulan dari hari ini."))

    @api.model
    def create(self, vals):
        vals['referensi'] = self.env['ir.sequence'].next_by_code('cdn.identitas.jamaah.peserta')
        return super(IdentitasJamaah, self).create(vals)
    
    def write(self, vals):
        if not self.referensi and not vals.get('referensi'):
            vals['referensi'] = self.env['ir.sequence'].next_by_code('cdn.identitas.jamaah.peserta')
        return super(IdentitasJamaah, self).write(vals)
    
    @api.depends('pendaftaran_ids')
    def _compute_jumlah_pendaftaran(self):
        for rec in self:
            jumlah_pendaftaran = self.env['cdn.pendaftaran'].search_count([('jamaah_id','=', rec.id)])
            rec.jumlah_pendaftaran = jumlah_pendaftaran

    def action_view_pendaftaran(self):
        return {
            'name': _('Pendaftaran'),
            'res_model': 'cdn.pendaftaran',
            'view_mode': 'list,form',
            'context': {'default_jamaah_id': self.id},
            'domain': [('jamaah_id', '=', self.id)],
            'target': 'current',
            'type': 'ir.actions.act_window'
        }

    @api.depends('penagihan_ids')
    def _compute_jumlah_penagihan(self):
        for rec in self:
            jumlah_penagihan = self.env['account.move'].search_count([('partner_id','=', rec.partner_id.id)])
            rec.jumlah_penagihan = jumlah_penagihan
        # self.jumlah_penagihan = 3
    
    def action_view_penagihan(self):
        return {
            'name': _('Penagihan'),
            'res_model': 'account.move',
            'view_mode': 'list,form',
            'context': {'default_partner_id': self.partner_id.id},
            'domain': [('partner_id', '=', self.partner_id.id)],
            'target': 'current',
            'type': 'ir.actions.act_window'
        }
    
    def action_view_jemaah_invoices(self):
        jamaah_id = self.partner_id.id
        return {
            'name': 'Pembayaran Jamaah',
            'view_mode': 'tree,form',
            'res_model': 'account.move',
            'context': {'search_default_partner_id': jamaah_id},
            'domain': [('partner_id', '=', jamaah_id)],
            'target': 'current',
            'type': 'ir.actions.act_window',
        }
    