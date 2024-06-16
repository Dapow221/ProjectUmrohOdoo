import json

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
    def get_pendaftaran(self, **kwargs):            
            data_paket_umroh = request.env['cdn.paket.umroh'].search([])
            data_jamaah_umroh = request.env['cdn.identitas.jamaah'].search([])
            data_login = request.env.user

            return request.render('cdn_arrosyid.pendaftaran_web', {
                'data_paket_umroh': data_paket_umroh,
                'data_jamaah_umroh': data_jamaah_umroh,
                'data_login': data_login,
            })

    @http.route('/pendaftaran_sesi', type='http', auth="user", website=True, csrf=True, methods=['POST', 'GET'])
    def get_pendaftaran_sesi(self, **post):
            try:
                sesi_id = post.get('sesi')
                tes = 'hello world'
                return json.dumps({'result': True, 'sesi id': sesi_id, 'tes': tes})
                # return sesi_id
            except Exception as e:
                # Handle errors and return error message
                return json.dumps({'result': False, 'error': str(e)})

            # sesi_id = post.get('sesi_id')
            # data_paket_umroh = request.env['cdn.paket.umroh'].search([('sesi_umroh', 'in', [data_sesi_umroh])])
            # data_jamaah_umroh = request.env['cdn.identitas.jamaah'].search([])
            # data_sesi_umroh = request.env['cdn.sesi.umroh'].search(['sesi', '=', sesi_id])
            # data_login = request.env.user

            # return request.render('cdn_arrosyid.pendaftaran_web_from_sesi', {
            #     'data_paket_umroh': data_paket_umroh,
            #     'data_sesi_umroh': data_sesi_umroh,
            #     'data_jamaah_umroh': data_jamaah_umroh,
            #     'data_login': data_login,
            # })
            # return sesi_id


    @http.route('/buat_pendaftaran', csrf=True, type="http", methods=['POST'], auth="public", website=True)
    def buat_pendaftaran(self, **post):
        try:
            # Ambil data dari permintaan POST
            jamaah_id = post.get('jamaah_id')
            sesi_id = post.get('sesi_id')
            # csrf_token = post.get('csrf_token')  # Ambil CSRF token dari permintaan
            
            # Verifikasi CSRF token
            # if request.csrf_token() != csrf_token:
                # raise ValueError("Invalid CSRF token")

            # Buat pendaftaran baru
            pendaftaran = request.env['cdn.pendaftaran']
            pendaftaran.create({
                'jamaah_id': jamaah_id,    
                'sesi_id': sesi_id,
            })
            
            # Kembalikan respons JSON
            return json.dumps({'result': True})
        except Exception as e:
            # Tangani kesalahan dan kembalikan pesan kesalahan
            return json.dumps({'result': False, 'error': str(e)})
    
    @http.route('/pendaftaran_berhasil', type='http',
                auth="public", website=True)
    def thank_you(self, **post):
        return request.render('cdn_arrosyid.pendaftaran_berhasil', {})
