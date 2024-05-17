# -*- coding: utf-8 -*-
# from odoo import http


# class CdnArrosyid(http.Controller):
#     @http.route('/cdn_arrosyid/cdn_arrosyid', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cdn_arrosyid/cdn_arrosyid/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('cdn_arrosyid.listing', {
#             'root': '/cdn_arrosyid/cdn_arrosyid',
#             'objects': http.request.env['cdn_arrosyid.cdn_arrosyid'].search([]),
#         })

#     @http.route('/cdn_arrosyid/cdn_arrosyid/objects/<model("cdn_arrosyid.cdn_arrosyid"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cdn_arrosyid.object', {
#             'object': obj
#         })
