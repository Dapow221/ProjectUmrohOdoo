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
    is_menikah       = fields.Boolean(string='Sudah menikah?', default = False)
    nama_pasangan    = fields.Char(string='Nama Pasangan')
    riwayat_penyakit = fields.Char(string='Riwayat Penyakit')
    active           = fields.Boolean(string='Active', default= True)
    state = fields.Selection(string='Status Umroh Jamaah', selection=[('draft', 'Draft'), ('berlangsung', 'Sedang Umroh'),('selesai', 'Selesai Umroh')])
    
    
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

     # Use @api.model if you're using Odoo version 10 or later
    def action_view_jemaah_invoices(self):
        # self.ensure_one()  # Ensure that there's only one record being processed

        # # Assuming 'partner_id' is the field linking the current record to the partner
        # partner_id = self.partner_id.id

        # # Define the action
        # action = {
        #     'type': 'ir.actions.act_window',
        #     'name': 'View Partner Invoices',
        #     'res_model': 'account.move',  # Assuming the model is account.move
        #     'view_mode': 'tree,form',  # Set the desired view mode
        #     'domain': [('partner_id', '=', partner_id)],  # Filter invoices by the current partner
        #     'context': {'search_default_partner_id': partner_id},  # Pass the partner's ID as a default search filter
        # }

        # return action
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
    