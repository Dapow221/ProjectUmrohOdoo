import json
from odoo import http
from odoo.http import request

class SignupController(http.Controller):
    @http.route('/signup', type='http', auth='public', website=True)
    def get_signup(self, **kw):  
        return request.render('cdn_arrosyid.signup')

    @http.route('/create_signup', csrf=True, type='http', auth='public', methods=['POST'], website=True)
    def get_create_signup(self, **post):
        try:
            email = post.get('email')
            name = post.get('name')
            password = post.get('password')
            confirm_password = post.get('confirm_password')


            # Cek apakah email sudah terdaftar
            partner_exists = request.env['res.partner'].sudo().search([('email', '=', email)])
            if partner_exists:
                return json.dumps({'result': False, 'error': 'Email sudah terdaftar. Silakan gunakan email lain.'})

            # Membuat partner baru jika belum terdaftar
            partner = request.env['res.partner']
            partner_id = False
            if not partner_exists:
                partner_id = partner.create({
                    'email': email,    
                    'name': name,      
                })

            # Membuat user jika partner berhasil dibuat atau sudah ada
            if partner_id or partner_exists:
                user = request.env['res.users']
                user.create({
                    'partner_id': partner_id.id if partner_id else partner_exists.id,
                    'login': email,
                    'name': name,
                    'password': password,
                })

                # Membuat objek cdn.identitas.jamaah jika partner berhasil dibuat atau sudah ada
                request.env['cdn.identitas.jamaah'].create({
                    'partner_id': partner_id.id if partner_id else partner_exists.id,
                    # Tambahkan atribut lain jika diperlukan
                })

                request.env.cr.commit()

            # Kembalikan respons JSON
            return json.dumps({'result': True})
        except Exception as e:
            # Tangani kesalahan dan kembalikan pesan kesalahan
            return json.dumps({'result': False, 'error': str(e)})