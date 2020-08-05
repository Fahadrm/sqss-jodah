# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class jodha_invoice_template(models.Model):
#     _name = 'jodha_invoice_template.jodha_invoice_template'
#     _description = 'jodha_invoice_template.jodha_invoice_template'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
