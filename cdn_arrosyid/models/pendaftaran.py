from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class CdnPendaftaran(models.Model):
    _name = 'cdn.pendaftaran'
    _description = 'Cdn Pendaftaran'
    _inherit = ['mail.thread','mail.activity.mixin']

    no_pendaftaran = fields.Char(string='Nomor Pendaftaran', tracking=True)
    state            = fields.Selection(string='Status', selection=[('draf', 'Draf'), ('batal', 'Batal'), ('konfirmasi', 'Kofirmasi'),('belum', 'Belum Lunas'), ('lunas', 'Lunas'),], compute="_cek_status_pembayaran", default="draf", tracking=True)

    # pilih_jamaah = fields.Selection(string='', selection=[('baru', 'Baru'), ('pilih', 'Pilih yang sudah terdaftar'),])
    jamaah_id      = fields.Many2one('cdn.identitas.jamaah', string='Jamaah', required=True, domain="[('state', '!=', 'proses')]", Tracking=True)
    # relatad jamaah
    partner_id     = fields.Many2one(related='jamaah_id.partner_id')
    nama           = fields.Char(related='jamaah_id.name', string="Nama")
    jenis_kel      = fields.Selection(related='jamaah_id.jenis_kel')
    referensi      = fields.Char(related='jamaah_id.referensi')
    paspor         = fields.Char(related='jamaah_id.paspor')
    masa_paspor    = fields.Date(related='jamaah_id.masa_paspor')
    tgl_lahir      = fields.Date(related='jamaah_id.tgl_lahir')
    umur           = fields.Integer(related='jamaah_id.umur') 
    image          = fields.Image(related='jamaah_id.image')
    is_menikah     = fields.Boolean(related='jamaah_id.is_menikah')
    nama_pasangan  = fields.Char(related='jamaah_id.nama_pasangan')
    riwayat_penyakit = fields.Char(related='jamaah_id.riwayat_penyakit')
    street         = fields.Char(related='jamaah_id.street')
    mobile         = fields.Char(related='jamaah_id.mobile')
    golongan_darah = fields.Selection(related='jamaah_id.golongan_darah')
    pekerjaan      = fields.Selection(related='jamaah_id.pekerjaan')
    email          = fields.Char(related='jamaah_id.email')
    is_umroh       = fields.Boolean(related='jamaah_id.is_umroh')
    tanggal_umroh  = fields.Date(related='jamaah_id.tanggal_umroh')
    pendidikan     = fields.Selection(related='jamaah_id.pendidikan')
    vaksin_meningitis = fields.Boolean(related='jamaah_id.vaksin_meningitis')
    vaksin_covid19 = fields.Selection(related='jamaah_id.vaksin_covid19')
    perlengkapan_line = fields.One2many(comodel_name='perlengkapan.detail', inverse_name='pendaftaran_id', string='Perlengkapan')

    sesi_id = fields.Many2one('cdn.sesi.umroh', string='Sesi Umroh',required=True, tracking=True)
    # related sesi
    name_sesi         = fields.Char(related='sesi_id.name', string="Nama")
    keterangan        = fields.Text(related='sesi_id.keterangan')
    paket_umroh       = fields.Char(related='sesi_id.paket_umroh_id.name', string="Nama Paket")
    lst_price         = fields.Float(string='Harga Paket',related='sesi_id.lst_price',store=True)
    pembimbing        = fields.Char(related='sesi_id.pembimbing_id.name', string="Nama Pembimbing")
    petugas_lapangan  = fields.Char(related='sesi_id.petugas_lapangan.name', string="Nama Petugas Lapangan")
    tanggal_berangkat = fields.Date(related='sesi_id.tanggal_berangkat')
    durasi            = fields.Integer(related='sesi_id.durasi')
    tanggal_pulang    = fields.Date(related='sesi_id.tanggal_pulang')

    penagihan_ids     = fields.One2many('account.move', 'pendaftaran_id', string='penagihan')
    btn_batal         = fields.Boolean(string='btn batal', default=False)
    status            = fields.Selection(string='status', selection=[('draf', 'Draf'), ('konfirmasi', 'konfirmasi'), ('batal', 'batal'), ('nol', 'nol')], default='nol')
    
    # action button
    def action_draf(self):
        for rec in self:
            rec.status = 'draf'
    
    def action_batal(self):
        for rec in self:
            for invoice in rec.penagihan_ids:
                if invoice.state == 'posted':
                    invoice.button_cancel()
            rec.penagihan_ids.unlink()
            rec.status = 'draf'

    def action_konfirmasi(self):
        for rec in self:
            rec.status = 'konfirmasi'
        
    @api.depends('penagihan_ids', 'status')
    def _cek_status_pembayaran(self):
        for rec in self:
            get_penagihan = self.env['account.move'].search([('pendaftaran_id','=', rec.id)])
            if get_penagihan:
                if get_penagihan.payment_state == 'paid':
                    rec.state = 'lunas'
                elif get_penagihan.payment_state == 'not_paid':
                    rec.state = 'belum'
                elif get_penagihan.payment_state == 'partial':
                    rec.state = 'belum'
            else:
                if rec.status == 'draf':
                    rec.state = 'draf'
                elif rec.status == 'konfirmasi':
                    rec.state = 'konfirmasi'
                elif rec.status == 'batal':
                    rec.state = 'batal'
                else:
                    rec.state = 'draf'



    def action_cek_tagihan(self):
        for pendaftaran in self:
        # Mendapatkan data Jamaah
            jamaah = pendaftaran.jamaah_id
            partner = jamaah.partner_id

            # Mendapatkan data Sesi Umroh
            sesi_umroh = pendaftaran.sesi_id
            sesi_harga = sesi_umroh.paket_umroh_id

            # Mendapatkan produk untuk invoice
            produk = self.env['product.product'].search([('paket_umroh_id', '=', sesi_harga.id)], limit=1)

            # Membuat data penagihan
            data_penagihan = [(0, 0, {
                'product_id': produk.id,
                'quantity': 1,
                'price_unit': sesi_umroh.lst_price,
            })]

            # Membuat invoice
            account_move = self.env['account.move']
            buat_penagian = account_move.create({
                'move_type': 'out_invoice',
                'partner_id': partner.id,
                'invoice_date': fields.Date.today(),
                'invoice_line_ids': data_penagihan,
                'paket_umroh': True,
                'pendaftaran_id': pendaftaran.id
            })

            view_penagihan = {
                'name': f'Invoice {partner.name}',
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                'res_model': 'account.move',
                'res_id': buat_penagian.id,
                'target': 'current', 
            }

            return view_penagihan

    def action_lunas(self):
        for pelunasan in self:
            get_pelunasan = self.env['account.move'].search([('pendaftaran_id', '=', pelunasan.id)])
            pelunasan_view = {
                'res_model': 'account.move',
                'name': 'Tagihan Jamaah',
                'res_id': get_pelunasan.id,
                'view_mode': 'form',
                'view_type': 'form',
                'target': 'current',
                'type': 'ir.actions.act_window'
            }
            return pelunasan_view


    # validasi jamaah double
    @api.constrains('jamaah_id', 'sesi_id')
    def _check_unique_jamaah(self):
        for rec in self:
            if rec.jamaah_id and rec.sesi_id:
                data_jamaah = self.env['cdn.pendaftaran'].search([
                    ('jamaah_id', '=', rec.jamaah_id.id),
                    ('sesi_id', '=', rec.sesi_id.id),
                    ('id', '!=', rec.id),  # Exclude the current record
                ])
                if data_jamaah:
                    raise ValidationError(_('Jamaah sudah terdaftar pada sesi ini!'))

    @api.model
    def create(self, vals):
        # Membuat nomor pendaftaran
        vals['no_pendaftaran'] = self.env['ir.sequence'].next_by_code('cdn.pendaftaran')
        return super(CdnPendaftaran, self).create(vals)

    def write(self, vals):
        if not self.no_pendaftaran and not vals.get('no_pendaftaran'):
            vals['no_pendaftaran'] = self.env['ir.sequence'].next_by_code('cdn.pendaftaran')
        return super(CdnPendaftaran, self).write(vals)
    
    def name_get(self):
        return [(record.id, "[%s] %s" % (record.no_pendaftaran, record.nama)) for record in self]


class PerlengkapanDetail(models.Model):
    _name = 'perlengkapan.detail'
    _description = 'Perlengkapan Detail'

    name = fields.Many2one('product.product', string="Name", domain=[('detailed_type', '=', 'consu')])
    pendaftaran_id = fields.Many2one('cdn.pendaftaran', string='Pendaftaran')
    cek_perlengkapan = fields.Boolean(string='Sudah Diambil', default=False)

    @api.model
    def create(self, vals):
        if 'name' in vals and 'pendaftaran_id' in vals:
            existing_record = self.env['perlengkapan.detail'].search([('name', '=', vals['name']), ('pendaftaran_id', '=', vals['pendaftaran_id'])])
            if existing_record:
                raise ValidationError("Perlengkapan tidak bisa dua")
        return super(PerlengkapanDetail, self).create(vals)

    def write(self, vals):
        if 'name' in vals and 'pendaftaran_id' in vals:
            existing_record = self.env['perlengkapan.detail'].search([('name', '=', vals['name']), ('pendaftaran_id', '=', vals['pendaftaran_id'])])
            if existing_record:
                raise ValidationError("Perlengkapan tidak bisa dua")
        return super(PerlengkapanDetail, self).write(vals)