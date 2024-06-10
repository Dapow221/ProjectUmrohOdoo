from odoo import http
from odoo.http import request

class HomeController(http.Controller):
    @http.route('/', type='http', auth="public", website=True)
    def get_home(self, **kw):


        
        return request.render('cdn_arrosyid.homepages')

    @http.route('/sesi', type='http', auth="public", website=True)
    def get_sesi(self, **kw):


        
        return request.render('cdn_arrosyid.sesi_umroh')

    @http.route('/ketentuan', type='http', auth="public", website=True)
    def get_ketentuan(self, **kw):


        
        return request.render('cdn_arrosyid.ketentuan_umum')

    @http.route('/pendaftaran', type='http', auth="public", website=True)
    def get_pendaftaran(self, **kw):


        
        return request.render('cdn_arrosyid.pendaftaran_web')

    @http.route('/profil', type='http', auth="public", website=True)
    def get_profil(self, **kw):


        
        return request.render('cdn_arrosyid.profil_web')