# -*- coding: utf-8 -*-
# from odoo import http


# class InvoicePoNumber(http.Controller):
#     @http.route('/invoice_po_number/invoice_po_number/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/invoice_po_number/invoice_po_number/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('invoice_po_number.listing', {
#             'root': '/invoice_po_number/invoice_po_number',
#             'objects': http.request.env['invoice_po_number.invoice_po_number'].search([]),
#         })

#     @http.route('/invoice_po_number/invoice_po_number/objects/<model("invoice_po_number.invoice_po_number"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('invoice_po_number.object', {
#             'object': obj
#         })
