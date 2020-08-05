# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Accountmove(models.Model):
    _inherit = 'account.move'

    cpo_number = fields.Char(string='PO Number')

class stock_picking(models.Model):
    _inherit = 'stock.picking'

    cpo_number = fields.Char(string='PO Number')


# class Respartner(models.Model):
#     _inherit='res.partner'
#
#     arabic_name = fields.Char("Name In Arabic")
