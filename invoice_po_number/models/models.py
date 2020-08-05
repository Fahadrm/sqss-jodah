# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Accountmove(models.Model):
    _inherit = 'account.move'

    cpo_number = fields.Char(string='PO Number')
    transpotation_charge = fields.Float(string='Transpotation Charges',default=0.00)
    loading_charge = fields.Float(string='Loading Charges',default=0.00)
    unloading_charge = fields.Float(string='Unloading Charges',default=0.00)
    weighning_charge = fields.Float(string='Weighning Charges',default=0.00)
    equipment_rental_charge = fields.Float(string='Equipment Charges',default=0.00)
    labor_charge = fields.Float(string='Labor Charges',default=0.00)
    other_charges = fields.Float(string='Other Charges',compute='_compute_amount',default=0.00)

    @api.depends('line_ids.debit',
        'line_ids.credit',
        'line_ids.currency_id',
        'line_ids.amount_currency',
        'line_ids.amount_residual',
        'line_ids.amount_residual_currency',
        'line_ids.payment_id.state','transpotation_charge','loading_charge',
                 'unloading_charge','weighning_charge',
                 'equipment_rental_charge','labor_charge','other_charges'
                 )
    def _compute_amount(self):

        res = super(Accountmove, self)._compute_amount()
        self.other_charges = self.transpotation_charge + self.loading_charge+self.unloading_charge+self.weighning_charge+self.equipment_rental_charge+self.labor_charge

        if self.other_charges:
            self.amount_total = self.amount_untaxed + self.amount_tax +self.other_charges
        return res

class stock_picking(models.Model):
    _inherit = 'stock.picking'

    cpo_number = fields.Char(string='PO Number')

    payment_terms = fields.Many2one('account.payment.term',string="Payment Terms")

class stock_move(models.Model):
    _inherit = 'stock.move'

    item_code = fields.Char(string='Item Code')


    @api.onchange('product_id')
    def _onchange_itemcode(self):
        for i in self:
            if i.product_id:
                i.item_code= i.product_id.barcode






class SaleOrderLine(models.Model):
    _name = 'sale.order.line'
    _inherit = 'sale.order.line'

    # item_code = fields.Char(string='Item Code')


    # @api.onchange('product_id')
    # def product_id_change(self):
    #     res = super(SaleOrderLine, self).product_id_change()
    #
    #     self.item_code = self.product_id.barcode

    def _prepare_procurement_values(self, group_id=False):
        res = super(SaleOrderLine, self)._prepare_procurement_values(group_id)
        res.update({'item_code': self.product_id.barcode})
        return res

class StockRuleInherit(models.Model):
    _inherit = 'stock.rule'

    def _get_stock_move_values(self, product_id, product_qty, product_uom, location_id, name, origin,
                                   values, group_id):
        res = super(StockRuleInherit, self)._get_stock_move_values(product_id, product_qty, product_uom,
                                                                       location_id,
                                                                       name, origin, values, group_id)
        res['item_code'] = group_id.get('item_code', False)
        return res





# class PurchaseOrder(models.Model):
#     _inherit='purchase.order'
#
#     purchase_order = fields.Many2one('purchase.order',string="Purchase Order")
#     department_id = fields.Many2one('hr.department',string="Department")
#     delivery_location1 = fields.Many2one()
    # delivery_location2 = fields.Many2one()
