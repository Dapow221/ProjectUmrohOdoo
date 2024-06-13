import odoo.http as http

class SignupController(http.Controller):
    @http.route('/signup', type='http', auth='public', website=True)
    def get_signup(self, **kw):
        partner = http.request.env['res.partner'].search([])
    
        return http.request.render('cdn_arrosyid.signup', partner)