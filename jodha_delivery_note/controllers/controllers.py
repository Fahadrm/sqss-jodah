# -*- coding: utf-8 -*-
# from odoo import http


# class JodhaDeliveryNote(http.Controller):
#     @http.route('/jodha_delivery_note/jodha_delivery_note/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/jodha_delivery_note/jodha_delivery_note/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('jodha_delivery_note.listing', {
#             'root': '/jodha_delivery_note/jodha_delivery_note',
#             'objects': http.request.env['jodha_delivery_note.jodha_delivery_note'].search([]),
#         })

#     @http.route('/jodha_delivery_note/jodha_delivery_note/objects/<model("jodha_delivery_note.jodha_delivery_note"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('jodha_delivery_note.object', {
#             'object': obj
#         })
