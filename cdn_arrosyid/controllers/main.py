from odoo import http
from odoo.http import request

class MainController(http.Controller):
    @http.route('/', type='http', auth="public", website=True)
    def get_home(self, **kw):
        return request.render('cdn_arrosyid.homepages')
        # return "Ini adalah halaman sesi umroh"

    @http.route('/sesi_umroh', auth='public', website=True)
    def sesi_umroh(self, **kwargs):
            sesi_umroh_records = request.env['cdn.sesi.umroh'].sudo().search([])
            return request.render('cdn_arrosyid.sesi_umroh_template', {
                'sesi_umroh_records': sesi_umroh_records
            })
            

    @http.route('/ketentuan', type='http', auth="public", website=True)
    def get_ketentuan(self, **kw):
        
        return request.render('cdn_arrosyid.ketentuan_umum')

    @http.route('/pendaftaran', type='http', auth="user", website=True)
    def get_pendaftaran(self, **kw):
        data_paket_umroh = request.env['cdn.paket.umroh'].search([])
        # paket_id = request.params.get('paket_id')
        data_sesi_umroh = request.env['cdn.sesi.umroh'].search([])
        data_login = request.env.user
        # data_login = request.env['cdn.sesi.umroh'].search([('email', '=', login.email)])

        return request.render('cdn_arrosyid.pendaftaran_web', {
            'data_paket_umroh': data_paket_umroh,
            'data_sesi_umroh': data_sesi_umroh,
            'data_login': data_login,
        })
    
    