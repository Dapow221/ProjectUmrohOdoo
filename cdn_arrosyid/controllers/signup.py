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

            partner = request.env['res.partner']
            partner_id = partner.sudo().create({
                'email': email,    
                'name': name,      
            })

            user = request.env['res.users'].sudo().create({
                'partner_id': partner_id.id,
                'login': email,
                'name': name,
                'password': password,
                'groups_id': [(6, 0, [10])],
            })

            request.env['cdn.identitas.jamaah'].sudo().create({
                'partner_id': partner_id.id,
                })

            return json.dumps({'result': True,'data : ': user})
        except Exception as e:
            return json.dumps({'result': False, 'error': str(e)})

    @http.route('/check_email_exists', type='json', auth='public', methods=['POST'])
    def check_email_exists(self, **kw):
        email = kw.get('email')
        if email:
            existing_user = request.env['res.users'].sudo().search([('login', '=', email)])
            return {'exists': True if existing_user else False}
        return {'exists': False}

    @http.route('/register_berhasil', type='http',
                auth="public", website=True)
    def pendaftaran_berhasil(self, **post):
        return request.render('cdn_arrosyid.register_berhasil', {})