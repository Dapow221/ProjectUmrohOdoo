from odoo import http
from odoo.http import request

class HomeController(http.Controller):
    @http.route('/home', type='http', auth="public", website=True)
    def get_home(self, **kw):

        pendaftarans = request.env['cdn.pendaftaran'].sudo().search([])

        data = {
            'pendaftarans' : pendaftarans 
        }
        
        return request.render('cdn_arrosyid.homepage', data)

    @http.route('/sesi', type='http', auth="public", website=True)
    def get_sesi(self, **kw):

        pendaftarans = request.env['cdn.pendaftaran'].sudo().search([])

        data = {
            'pendaftarans' : pendaftarans 
        }
        
        return request.render('cdn_arrosyid.sesi_umroh', data)

    @http.route('/ketentuan', type='http', auth="public", website=True)
    def get_ketentuan(self, **kw):

        pendaftarans = request.env['cdn.pendaftaran'].sudo().search([])

        data = {
            'pendaftarans' : pendaftarans 
        }
        
        return request.render('cdn_arrosyid.ketentuan_umum', data)

    @http.route('/pendaftaran', type='http', auth="public", website=True)
    def get_pendaftaran(self, **kw):

        pendaftarans = request.env['cdn.pendaftaran'].sudo().search([])

        data = {
            'pendaftarans' : pendaftarans 
        }
        
        return request.render('cdn_arrosyid.pendaftaran_web', data)

    @http.route('/profil', type='http', auth="public", website=True)
    def get_profil(self, **kw):

        pendaftarans = request.env['cdn.pendaftaran'].sudo().search([])

        data = {
            'pendaftarans' : pendaftarans 
        }
        
        return request.render('cdn_arrosyid.profil_web', data)