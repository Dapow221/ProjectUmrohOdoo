from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class CdnPendaftaran(models.Model):
    _name = 'cdn.pendaftaran'
    _description = 'Cdn Pendaftaran'
    _inherit = ['mail.thread','mail.activity.mixin']

    no_pendaftaran = fields.Char(string='Nomor Pendaftaran', tracking=True)
    state = fields.Selection(string='Status', selection=[('draf', 'Draf'), ('batal', 'Batal'), ('konfirmasi', 'Kofirmasi'), ('selesai', 'Selesai'),], default="draf", tracking=True)
    
    jamaah_id = fields.Many2one('cdn.identitas.jamaah', string='Jamaah', required=True, tracking=True)
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

    sesi_id = fields.Many2one('cdn.sesi.umroh', string='Sesi Umroh',required=True, tracking=True)
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

        # Membuat pendaftaran   
        pendaftaran = super(CdnPendaftaran, self).create(vals)

        # Mendapatkan data Jamaah
        jamaah = pendaftaran.jamaah_id
        partner = jamaah.partner_id

        # Mendapatkan data Sesi Umroh
        sesi_umroh = pendaftaran.sesi_id
        paket_umroh = sesi_umroh.paket_umroh_id

        # Mendapatkan produk untuk invoice
        produk = self.env['product.product'].search([('paket_umroh_id', '=', paket_umroh.id)], limit=1)

        # Membuat data penagihan
        data_penagihan = [(0, 0, {
            'product_id': produk.id,
            'quantity': 1,
            'price_unit': produk.lst_price,
        })]

        # Membuat invoice
        account_move = self.env['account.move']
        invoice = account_move.create({
            'move_type': 'out_invoice',
            'partner_id': partner.id,
            'invoice_date': fields.Date.today(),
            'invoice_line_ids': data_penagihan,
            'paket_umroh': True,
            # 'sequence_prefix': f'pkt_umroh-{self.no_pendaftaran}',
            # 'state': 'posted',
        })

        return pendaftaran

    def write(self, vals):
        if not self.no_pendaftaran and not vals.get('no_pendaftaran'):
            vals['no_pendaftaran'] = self.env['ir.sequence'].next_by_code('cdn.pendaftaran')
        return super(CdnPendaftaran, self).write(vals)
    
    def name_get(self):
        return [(record.id, "[%s] %s" % (record.no_pendaftaran, record.nama)) for record in self]