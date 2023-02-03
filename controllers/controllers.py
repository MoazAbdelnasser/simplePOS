# -*- coding: utf-8 -*-
# from odoo import http


# class MoSimplePos(http.Controller):
#     @http.route('/mo_simple_pos/mo_simple_pos', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mo_simple_pos/mo_simple_pos/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mo_simple_pos.listing', {
#             'root': '/mo_simple_pos/mo_simple_pos',
#             'objects': http.request.env['mo_simple_pos.mo_simple_pos'].search([]),
#         })

#     @http.route('/mo_simple_pos/mo_simple_pos/objects/<model("mo_simple_pos.mo_simple_pos"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mo_simple_pos.object', {
#             'object': obj
#         })
