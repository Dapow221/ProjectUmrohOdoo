import odoo

from odoo import http, models, fields, _
from odoo.http import request
import json

class PendaftaranController(http.Controller):

    @http.route('/pendaftaran', type='http', auth="public", website=True)
    def get_pendaftaran_list(self, **kwargs):

        pendaftarans = request.env['cdn.pendaftaran'].sudo().search([])

        data = {
            'pendaftarans' : pendaftarans 
        }
        
        return request.render('cdn_arrosyid.pendaftaran_list', data)