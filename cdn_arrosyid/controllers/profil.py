import json

from odoo import http
from odoo.http import request

class MainController(http.Controller):
    @http.route('/my/home', type='http', auth='public', website=True)
    def get_data(self):
        user_id = request.env.user.partner_id.id
        data_sesi_umroh = request.env['cdn.sesi.umroh'].search([])
        data_pendaftaran = request.env['cdn.pendaftaran'].search([])
        data_jamaah_umroh = request.env['cdn.pendaftaran'].search(['|', ('partner_id', '=', user_id), ('pendaftar_id', '=', user_id)])
        data_tagihan = request.env['account.move'].sudo().search([('partner_id', '=', user_id),('state', '=', 'posted')])

        return request.render('cdn_arrosyid.profil', {
            'data_sesi': data_sesi_umroh,
            'data_pendaftaran': data_pendaftaran,
            'data_tagihan': data_tagihan,
            'data_jamaah_umroh': data_jamaah_umroh
        })
