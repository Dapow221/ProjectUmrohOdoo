from odoo import http
from odoo.http import request

class SesiUmrohController(http.Controller):
    
    @http.route('/sesi_umroh', auth='public', website=True)
    def sesi_umroh(self, **kwargs):
            sesi_umroh_records = request.env['cdn.sesi.umroh'].sudo().search([])
            return request.render('cdn_arrosyid.sesi_umroh_template', {
                'sesi_umroh_records': sesi_umroh_records
            })


class PendaftaranController(http.Controller):
    
    @http.route('/pendaftaran_umroh', auth='public', website=True)
    def pendaftaran_umroh(self, **kwargs):
            pendaftaran_umroh_records = request.env['cdn.pendaftaran'].sudo().search([])
            return request.render('cdn_arrosyid.pendaftaran_umroh_template', {
                'pendaftaran_umroh_records': pendaftaran_umroh_records
            })
            