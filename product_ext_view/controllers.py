# -*- coding: utf-8 -*-
from openerp import http

# class ProductExtView(http.Controller):
#     @http.route('/product_ext_view/product_ext_view/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_ext_view/product_ext_view/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_ext_view.listing', {
#             'root': '/product_ext_view/product_ext_view',
#             'objects': http.request.env['product_ext_view.product_ext_view'].search([]),
#         })

#     @http.route('/product_ext_view/product_ext_view/objects/<model("product_ext_view.product_ext_view"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_ext_view.object', {
#             'object': obj
#         })