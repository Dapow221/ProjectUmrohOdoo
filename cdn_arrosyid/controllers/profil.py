import json

from odoo import http
from odoo.http import request

class MainController(http.Controller):
    @http.route('/my/home', type='http', auth='public', website=True)
    def get_data(self):
        data_jamaah_umroh = request.env['cdn.identitas.jamaah'].search([])
        data_pendaftaran = request.env['cdn.pendaftaran'].search([])
        data_sesi_rencana_perjalanan = request.env['cdn.rencana.perjalanan'].search([])

        return request.render('cdn_arrosyid.profil', {
            'data_sesi': data_sesi_rencana_perjalanan,
            'data_pendaftaran': data_pendaftaran,
            'data_jamaah_umroh': data_jamaah_umroh,
        })
