import json
from odoo import http
from odoo.http import request
from odoo.exceptions import ValidationError

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

            partner_exists = request.env['res.partner'].sudo().search([('email', '=', email)])
            if partner_exists:
                return json.dumps({'result': False, 'error': 'Email sudah terdaftar. Silakan gunakan email lain.'})

            partner = request.env['res.partner']
            partner_id = partner.sudo().create({
                'email': email,    
                'name': name,      
            })

            request.env['res.users'].sudo().create({
                'partner_id': partner_id.id,
                'login': email,
                'name': name,
                'password': password,
            })

            request.env['cdn.identitas.jamaah'].sudo().create({
                'partner_id': partner_id.id,
                })

            return json.dumps({'result': True})
        except Exception as e:
            return json.dumps({'result': False, 'error': str(e)})

    @http.route('/check_email_exists', type='json', auth='public', methods=['POST'])
    def check_email_exists(self, **kw):
        email = kw.get('email')
        if email:
            existing_user = request.env['res.users'].sudo().search([('email', '=', email)])
            return {'exists': True if existing_user else False}
        return {'exists': False}