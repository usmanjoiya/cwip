# -*- coding: utf-8 -*-
from flectra import http

# class FixA(http.Controller):
#     @http.route('/fix_a/fix_a/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fix_a/fix_a/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fix_a.listing', {
#             'root': '/fix_a/fix_a',
#             'objects': http.request.env['fix_a.fix_a'].search([]),
#         })

#     @http.route('/fix_a/fix_a/objects/<model("fix_a.fix_a"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fix_a.object', {
#             'object': obj
#         })