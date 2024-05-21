from odoo import models, fields, api



class AccountMove(models.Model):
    _inherit = 'account.move'

    product_travel = fields.Selection(string='Jenis', selection=[('non_status', 'Non Status'), ('konsumen', 'Konsumen'), ('pelayanan', 'Pelayanan'),], default='non_status')

