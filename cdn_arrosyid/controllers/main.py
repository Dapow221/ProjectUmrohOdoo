from odoo import http
from odoo.http import request

class HomeController(http.Controller):
    @http.route('/home', type='http', auth="public", website=True)
    def get_home(self, **kw):
        return request.render('cdn_arrosyid.homepage')
        # return "Ini adalah halaman sesi umroh"

    @http.route('/sesi', type='http', auth="public", website=True)
    def get_sesi(self, **kw):        
        return request.render('cdn_arrosyid.sesi_umroh')
        # return "Ini adalah halaman sesi umroh"

    @http.route('/ketentuan', type='http', auth="public", website=True)
    def get_ketentuan(self, **kw):
        return request.render('cdn_arrosyid.ketentuan_umum')

    @http.route('/pendaftaran', type='http', auth="public", website=True)
    def get_pendaftaran(self, **kw):
        return request.render('cdn_arrosyid.pendaftaran_web')

    @http.route('/profil', type='http', auth="public", website=True)
    def get_profil(self, **kw):        
        return request.render('cdn_arrosyid.profil_web')