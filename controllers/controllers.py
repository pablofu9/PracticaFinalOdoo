# -*- coding: utf-8 -*-
# from odoo import http


# class Fctpablo(http.Controller):
#     @http.route('/fctpablo/fctpablo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fctpablo/fctpablo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('fctpablo.listing', {
#             'root': '/fctpablo/fctpablo',
#             'objects': http.request.env['fctpablo.fctpablo'].search([]),
#         })

#     @http.route('/fctpablo/fctpablo/objects/<model("fctpablo.fctpablo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fctpablo.object', {
#             'object': obj
#         })
