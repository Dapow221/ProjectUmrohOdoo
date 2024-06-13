# -*- coding: utf-8 -*-

from odoo import http
from odoo.addons.web.controllers.main import content_disposition
from odoo.http import request
import base64

class commonController(http.Controller):
    @http.route('/web/binary/download_document', type='http', auth="public")
    def download_document(self, model, field, id, file_name, **kw):
        Models = http.request.env[model]
        fields = [field]
        res = Models.search([('id', '=', id)]).read(fields)[0]
        filecontent = base64.b64decode(res['file_export'] or '')

        if not filecontent:
            return request.not_found()

        if not file_name:
            file_name = '%s_%s' % (model.replace('.', '_'), id)
        return request.make_response(filecontent, [
            ('Content-Type', 'application/octet-stream'),
            ('Content-Disposition', content_disposition(file_name))
        ])