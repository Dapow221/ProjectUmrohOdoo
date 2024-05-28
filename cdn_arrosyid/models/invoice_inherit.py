from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    sesi_umroh = fields.Boolean(string='sesi_umroh')
    paket_umroh = fields.Boolean(string='Paket_umroh')
    pendaftaran_id = fields.Integer(string='Pendaftaran Id')
    