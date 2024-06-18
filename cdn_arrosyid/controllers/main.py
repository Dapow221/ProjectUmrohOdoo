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
            user_id = request.env.user.partner_id.id
            data_login = request.env['cdn.identitas.jamaah'].search([('partner_id', '=', user_id)])
            data_semua_jamaah_umroh = request.env['cdn.identitas.jamaah'].sudo().search([])
            data_paket_umroh = request.env['cdn.paket.umroh'].search([])

            return request.render('cdn_arrosyid.pendaftaran_web', {
                'data_login': data_login,
                'data_paket_umroh': data_paket_umroh,
                'data_semua_jamaah_umroh': data_semua_jamaah_umroh,
                # 'tes': user_id,
            })

    # @http.route('/pendaftaran_sesi/<string:sesi_id>', type='http', auth="user", website=True, csrf=True, methods=['POST', 'GET'])
    # def get_pendaftaran_sesi(self,sesi_id, **post):
    #         data_jamaah_umroh_all = request.env['cdn.identitas.jamaah'].search([])
    #         data_jamaah_umroh = request.env['cdn.identitas.jamaah'].search([('id', '=', user_id)])
    #         data_sesi_umroh = request.env['cdn.sesi.umroh'].search([('id', '=', sesi_id)])
    #         paket_id = data_sesi_umroh.mapped('paket_umroh_id.id')
    #         data_paket_umroh = request.env['cdn.paket.umroh'].search([('id', '=', paket_id)])
    #         user_id = request.env.user.partner_id
    #         data_login = request.env['cdn.partner'].search([('id', '=', user_id)])

    #         return request.render('cdn_arrosyid.pendaftaran_web_from_sesi', {
    #             'data_paket_umroh': data_paket_umroh,
    #             'data_sesi_umroh': data_sesi_umroh,
    #             'data_jamaah_umroh': data_jamaah_umroh,
    #             'data_jamaah_umroh_all': data_jamaah_umroh_all,
    #             'data_login': data_login,
    #         })
    #         # return paket_id

    @http.route('/tambah_jamaah_baru', csrf=True, type="http", methods=['POST'], auth="public", website=True)
    def tambah_jamaah_baru(self, **post):
        try:
            nama = post.get('nama')
            jenis_kelamin = post.get('jenis_kelamin')
            tgl_lahir = post.get('tgl_lahir')
            # csrf_token = post.get('csrf_token')

            m_partner = request.env['res.partner']
            partner = m_partner.create({
                'name': nama,
            })

            m_identitas = request.env['cdn.identitas.jamaah']
            identitas = m_identitas.create({
                'partner_id': partner.id,
                'jenis_kel': jenis_kelamin,
                'tgl_lahir': tgl_lahir,
            })
            
            # Kembalikan respons JSON dengan ID partner yang baru dibuat
            return json.dumps({'result': True, 'identitas_id': identitas.id})
        
        except Exception as e:
            # Tangani kesalahan dan kembalikan pesan kesalahan
            return json.dumps({'result': False, 'error': str(e)})
   
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

    @http.route('/buat_pendaftaran_banyak', csrf=True, type="http", methods=['POST'], auth="public", website=True)
    def buat_pendaftaran_banyak(self, **post):
        try:
            # print("Data POST:", post)

            jamaah = []
            for key, value in post.items():
                if key.startswith('jamaah_id['):
                    jamaah_id = value
                    jamaah.append({'id': jamaah_id})
            sesi_id = post.get('sesi_id')
            data_login_id = post.get('data_login_id')
            # csrf_token = post.get('csrf_token')  # Ambil CSRF token dari permintaan
    
            for jamaah_id in jamaah:
                pendaftaran = request.env['cdn.pendaftaran']
                pendaftaran.create({
                    'jamaah_id': int(jamaah_id.get('id')),
                    'sesi_id': int(sesi_id),
                    'pendaftar_id': int(data_login_id),
                })
            
            # Kembalikan respons JSON berhasil
            return json.dumps({'result': True, 'message': 'Pendaftaran berhasil', 'jamaah_id': jamaah})
        
        except Exception as e:
            # Tangani kesalahan dan kembalikan pesan kesalahan
            return json.dumps({'result': False, 'error': str(e)})
    
    @http.route('/pendaftaran_berhasil', type='http',
                auth="public", website=True)
    def thank_you(self, **post):
        return request.render('cdn_arrosyid.pendaftaran_berhasil', {})
