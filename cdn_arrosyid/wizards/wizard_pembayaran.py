from odoo import models, fields, api, _



class WizardPembayaran(models.TransientModel):
    _name = 'wizard.pembayaran'
    _description = 'Wizard Pembayaran / invoicing'

    product_id = fields.Many2one('product.product', string='paket umroh')
    jamaah_id = fields.Many2one('res.partner', string='jamaah')

    def action_pembayaran(self):
        data_paket = []
        for rec in self.product_id:
            data_paket.append((0, 0, {
                'product_id': rec.id,
                'price_unit': rec.lst_price,
                'name': rec.name,
            }))
            # print("******** data: ", rec.name)

        product_invoice = self.env['account.move'].create({
            'move_type': 'out_invoice',
            'partner_id': self.jamaah_id.id,
            'invoice_date': fields.Date.today(),
            'invoice_line_ids': data_paket,
        })

        return {
            'type': 'ir.actions.act_window',
            'name': 'pembayaran',
            'view_mode': 'form',
            'res_model': 'account.move',
            'res_id': product_invoice.id,
        }