from odoo import models, fields, api

class PaketUmroh(models.Model):
    _name = 'cdn.paket.umroh'
    _description = 'Master Data Paket Umroh'
    _rec_name = 'keterangan'

    keterangan = fields.Text('Keterangan', required=True)
    sesi_umroh = fields.Many2many(comodel_name='cdn.sesi.umroh', inverse_name='paket_umroh_id', string='Sesi Umroh')     
    perlengkapan_ids = fields.One2many('cdn_perlengkapan', 'paket_umroh_id', string='Perlengkapan')
    maskapai_id = fields.Many2one(comodel_name='res.company', string='Maskapai')
    hotel_id = fields.Many2many(comodel_name='res.company', string='Hotel')
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)
    currency_id = fields.Many2one('res.currency', related='company_id.currency_id')
    product_ids = fields.Many2many(comodel_name='product.product', string='')


class Perlengkapan(models.Model):
    _name = 'cdn_perlengkapan'
    _description = 'Perlengkapan'

    product_id = fields.Many2one('product.product', required=True, String='Perlengkapan')
    harga = fields.Float(related='product_id.list_price')
    jumlah = fields.Integer(string='Jumlah', default="1")
    paket_umroh_id = fields.Many2one(comodel_name='cdn.paket.umroh', string='Paket Umroh')
    currency_id = fields.Many2one('res.currency', related='paket_umroh_id.currency_id')
    harga_subtotal = fields.Monetary(string='Subtotal', compute="_compute_harga_subtotal", currency_field="currency_id")

    @api.depends('harga', 'jumlah')
    def _compute_harga_subtotal(self):
        for rec in self:
            rec.harga_subtotal = rec.harga * rec.jumlah
