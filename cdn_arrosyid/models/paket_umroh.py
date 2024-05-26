from odoo import models, fields, api

class PaketUmroh(models.Model):
    _name               = 'cdn.paket.umroh'
    _description        = 'Master Data Paket Umroh'

    name                = fields.Char(string='Nama', required=True)  
    keterangan          = fields.Text(string='Keterangan')
    lst_price           = fields.Float(string='Harga Paket', required=True)
    image               = fields.Image('image')
    sesi_umroh          = fields.One2many(comodel_name='cdn.sesi.umroh', inverse_name='paket_umroh_id', string='Sesi Umroh')
    maskapai_id         = fields.Many2one(comodel_name='res.partner', string='Maskapai', required=True)
    hotel_id            = fields.Many2many(comodel_name='res.partner', string='Hotel', required=True)
    company_id          = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)
    currency_id         = fields.Many2one('res.currency', related='company_id.currency_id', required=True)
    product_ids         = fields.Many2many(comodel_name='product.product', string='Consumable', domain=[('detailed_type', '=', 'consu')], required=True)
    durasi              = fields.Integer(string='Durasi Umroh (Hari)', required=True)
    product_id          = fields.Many2one('product.product')
    harga_subtotal      = fields.Monetary(string='Harga Total', compute="_compute_harga_subtotal", currency_field="currency_id")

    @api.depends('product_ids', 'product_ids.lst_price')
    def _compute_harga_subtotal(self):
        for rec in self:
            total_price = sum(product.lst_price for product in rec.product_ids)
            rec.harga_subtotal = total_price
        return total_price

    @api.model
    def create(self, vals):      
        paket_baru = super(PaketUmroh, self).create(vals)

        paket_baru_umroh = self.env['product.product']
        paket_baru_umroh.create({
            'name': paket_baru.name,
            'lst_price': paket_baru.lst_price,
            'detailed_type': 'service',
            'paket_umroh_id': paket_baru.id
        })

        return paket_baru

    def write(self, vals):      
        paket_baru = super(PaketUmroh, self).write(vals)

        paket_baru_umroh = self.env['product.product'].search([('paket_umroh_id','=', self.id)])
        paket_baru_umroh.write({
            'name': self.name,
            'lst_price': self.lst_price,
        })
        return paket_baru

    # def action_create_invoice(self):
    #     invoice_lines = []
    #     for item in self.perlengkapan_ids:
    #         invoice_lines.append((0, 0, {
    #             'product_id': item.product_id.id,
    #             'quantity': item.jumlah,
    #             'price_unit': item.harga,
    #             'name': item.product_id.name,
    #         }))

    #     invoice = self.env['account.move'].create({
    #         'move_type': 'out_invoice',
    #         'partner_id': self.sesi_umroh.jammaah_ids,  
    #         'invoice_date': fields.Date.today(),
    #         'invoice_line_ids': invoice_lines,
    #         'currency_id': self.currency_id.id,
    #     })

    #     return {
    #         'type': 'ir.actions.act_window',
    #         'name': 'Invoice',
    #         'view_mode': 'form',
    #         'res_model': 'account.move',
    #         'res_id': invoice.id,
    #     }