from odoo import models, fields, api



class PaketUmroh(models.Model):
    _name = 'cdn.paket.umroh'
    _description = 'Master Data Paket Umroh'
    # _inherit = 'product.product'

    keterangan = fields.Text('Keterangan')
    # harga = fields.Monetary('harga')

    # sesi_umroh = fields.One2many(comodel_name='cdn.transaksi.umroh', inverse_name='paket_umroh_id', string='Sesi Umroh')
    # perlengkapan_ids = fields.Many2many('product.product', string='perlengkapan')