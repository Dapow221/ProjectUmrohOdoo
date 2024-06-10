from odoo            import models, fields, api, _
from datetime        import date
# from dateutil        import relativedelta
from odoo.exceptions import ValidationError

class IdentitasJamaah(models.Model):
    _name               = 'cdn.identitas.jamaah' 
    _description        = 'Identitas Jamaah'
    _inherits           = {'res.partner':'partner_id'}

    partner_id          = fields.Many2one(comodel_name='res.partner', string='Nama Jamaah', required=True, ondelete="cascade")
    jenis_kel           = fields.Selection(string='Jenis Kelamin', selection=[('l', 'Laki-laki'), ('p', 'Perempuan'),], default='l')
    referensi           = fields.Char(string='No Referensi')
    paspor              = fields.Char(string='Nomor Paspor', required=True)
    masa_paspor         = fields.Date(string='Masa berlaku Paspor', required=True)
    tgl_lahir           = fields.Date(string='Tanggal Lahir', required=True)
    umur                = fields.Integer(string='Umur', compute='_compute_umur') 
    image               = fields.Image(string='image',)
    is_menikah          = fields.Boolean(string='Sudah menikah', default = False)
    nama_pasangan       = fields.Char(string='Nama Pasangan')
    riwayat_penyakit    = fields.Char(string='Riwayat Penyakit')
    active              = fields.Boolean(string='Active', default= True)
    state               = fields.Selection(string='Status', selection=[('draft', 'draft'),('proses', 'Sedang Umroh'),('selesai', 'Selesai'),('batal', 'Perjalanan Batal')], default='draft')
    pendaftaran_ids     = fields.One2many('cdn.pendaftaran', 'jamaah_id', string='Pendaftaran')
    jumlah_pendaftaran  = fields.Integer(compute="_compute_jumlah_pendaftaran")
    penagihan_ids       = fields.One2many('account.move', 'partner_id', string='Penagihan')
    jumlah_penagihan    = fields.Integer(string='Jumlah penagihan ', compute="_compute_jumlah_penagihan")
    lunas               = fields.Char(string='Lunas')
    golongan_darah      = fields.Selection(string='Golongan Darah', selection=[('oplus', 'O+'), ('ominus', 'O-'),('aplus', 'A+'),('aminus', 'A-'),('bplus', 'B+'), ('bminus', 'B-'),('abplus', 'AB+'),('abminus', 'AB-')], default='oplus')
    pekerjaan           = fields.Selection(string='Pekerjaan', selection=[('pns', 'PNS'), ('irt', 'Ibu Rumah Tangga'),('tni', 'TNI'),('dagang', 'Pedagang'),('tani', 'Petani'),('swasta', 'Swasta'),('pelajar', 'Pelajar'),('bumn', 'BUMN'),], default='pns')
    pendidikan          = fields.Selection(string='Pendidikan Terakhir', selection=[('sd', 'SD'), ('smp', 'SMP'),('sma', 'SMA'),('kuliah', 'Perguruan Tinggi')], default='sd')
    vaksin_meningitis   = fields.Boolean(string='Vaksinasi Meningitis', default=False)
    vaksin_covid19      = fields.Selection(string='Vaksinasi Covid19', selection=[('belum', 'Belum Vaksin'), ('vaksin1', 'Vaksinasi Pertama'), ('vaksin2', 'Vaksinasi Kedua'), ('booster', 'Vaksin Booster')], default='belum')
    is_umroh            = fields.Boolean(string='Pernah Umroh')
    tanggal_umroh       = fields.Date(string='Tanggal Umroh')
    company_id          = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)
    currency_id         = fields.Many2one('res.currency', related='company_id.currency_id', required=True)

    total_pembayaran    = fields.Float(string='Total Pembayaran', compute='_compute_total_pembayaran')
    total_due           = fields.Float(string='Total Due', compute='_compute_total_due')

    def _get_company_currency(self):
        for partner in self:
            if partner.company_id:
                partner.currency_id = partner.sudo().company_id.currency_id
            else:
                partner.currency_id = self.env.company.currency_id

    @api.depends('penagihan_ids')
    def _compute_total_pembayaran(self):
        for rec in self:
            jmlh_total            = self.env['account.move'].search([('partner_id', '=', rec.partner_id.id)])
            rec.total_pembayaran = sum(total.amount_untaxed for total in jmlh_total)

    @api.depends('penagihan_ids')
    def _compute_total_due(self):
        for rec in self:
            jmlh_total            = self.env['account.move'].search([('partner_id', '=', rec.partner_id.id)])
            rec.total_due = sum(total.amount_residual for total in jmlh_total)

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
            'context': {'default_partner_id': self.partner_id.id, 'default_move_type': 'out_invoice'},
            'domain': [('partner_id', '=', self.partner_id.id), ('move_type', '=', 'out_invoice')],
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
    # action button
    def action_draft(self):
        for rec in self:
            rec.state = 'draft'
    
    def action_batal(self):
        for rec in self:
            rec.state = 'batal'

    def action_proses(self):
        for rec in self:
            rec.state = 'proses'

    def action_selesai(self):
        for rec in self:
            rec.state = 'selesai'
    