# -*- coding: utf-8 -*-
# from odoo import http


# class JodhaInvoiceTemplate(http.Controller):
#     @http.route('/jodha_invoice_template/jodha_invoice_template/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/jodha_invoice_template/jodha_invoice_template/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('jodha_invoice_template.listing', {
#             'root': '/jodha_invoice_template/jodha_invoice_template',
#             'objects': http.request.env['jodha_invoice_template.jodha_invoice_template'].search([]),
#         })

#     @http.route('/jodha_invoice_template/jodha_invoice_template/objects/<model("jodha_invoice_template.jodha_invoice_template"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('jodha_invoice_template.object', {
#             'object': obj
#         })
