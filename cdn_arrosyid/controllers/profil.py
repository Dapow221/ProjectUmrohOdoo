import json

from odoo import http
from odoo.http import request

class MainController(http.Controller):
    @http.route('/my/home', type='http', auth='public', website=True)
    def get_data(self):
        data_sesi_umroh = request.env['cdn.sesi.umroh'].search([])
        data_pendaftaran = request.env['cdn.pendaftaran'].search([])
        
        return request.render('cdn_arrosyid.profil', {
            'data_sesi': data_sesi_umroh,
            'data_pendaftaran': data_pendaftaran,
        })
