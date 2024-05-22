from odoo import models, fields, api

class PaketUmroh(models.Model):
    _name = 'cdn.paket.umroh'
    _description = 'Master Data Paket Umroh'
    

    name = fields.Char(string='Nama')  
    keterangan = fields.Text(string='Keterangan')
    sesi_umroh = fields.One2many(comodel_name='cdn.sesi.umroh', inverse_name='paket_umroh_id', string='Sesi Umroh')
    
    @api.model
    def create(self, vals):

        paket_umroh = super(PaketUmroh, self).create(vals)
        
        product_obj = self.env['product.product']
        product_vals = {
            'name': paket_umroh.name,
            'detailed_type': 'service',
            'paket_umroh_id': paket_umroh.id,
        }
        product_obj.create(product_vals)
        
        return paket_umroh
    
    perlengkapan_ids = fields.One2many('cdn.perlengkapan', 'paket_umroh_id', string='Perlengkapan')
    maskapai_id = fields.Many2one(comodel_name='res.partner', string='Maskapai')
    hotel_id = fields.Many2many(comodel_name='res.partner', string='Hotel')
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)
    currency_id = fields.Many2one('res.currency', related='company_id.currency_id')
    product_ids = fields.Many2many(comodel_name='product.product', string='Peralatan/Konsumsi', domain=[('detailed_type', '=', 'consu')])


    def action_create_invoice(self):
        invoice_lines = []
        for item in self.perlengkapan_ids:
            invoice_lines.append((0, 0, {
                'product_id': item.product_id.id,
                'quantity': item.jumlah,
                'price_unit': item.harga,
                'name': item.product_id.name,
            }))

        invoice = self.env['account.move'].create({
            'move_type': 'out_invoice',
            'partner_id': self.sesi_umroh.jammaah_ids,  
            'invoice_date': fields.Date.today(),
            'invoice_line_ids': invoice_lines,
            'currency_id': self.currency_id.id,
        })

        return {
            'type': 'ir.actions.act_window',
            'name': 'Invoice',
            'view_mode': 'form',
            'res_model': 'account.move',
            'res_id': invoice.id,
        }
    

class Perlengkapan(models.Model):
    _name = 'cdn.perlengkapan'
    _description = 'Perlengkapan'

    name = fields.Char(string='Nama')  
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