from odoo import models, fields, api
import requests
import json
from datetime import date

class AccountMove(models.Model):
    _inherit       = 'account.move'

    sesi_umroh     = fields.Boolean(string='sesi_umroh')
    paket_umroh    = fields.Boolean(string='Paket_umroh')
    pendaftaran_id = fields.Integer(string='Pendaftaran Id')

    def action_post(self):
        moves_with_payments = self.filtered('payment_id')
        other_moves = self - moves_with_payments
        if moves_with_payments:
            moves_with_payments.payment_id.action_post()
        if other_moves:
            other_moves._post(soft=False)

        url = 'http://localhost:8015/virtual_account/create'
        data_bayar = {
            "virtual_account" : self.name,
            "amount" : self.amount_total,
            "exp_date" : fields.Date.to_string(self.invoice_date_due),
            "description" : "Pembayaran Invoice",
        }

        response = requests.post(url, headers={'Content-Type': 'application/json'}, data=json.dumps(data_bayar))
        
        return False  