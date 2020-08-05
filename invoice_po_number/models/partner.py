# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Respartner(models.Model):
    _inherit='res.partner'

    partner_arabic_name = fields.Char("Name In Arabic")
