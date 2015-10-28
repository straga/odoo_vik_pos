# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2014-Today OpenERP SA (<http://www.openerp.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import osv
from openerp.tools.translate import _
from openerp.report import report_sxw
import logging
_logger = logging.getLogger(__name__)


class PosInvoiceReport(osv.AbstractModel):

    _name = 'report.point_of_sale.report_invoice'
    _inherit = 'report.point_of_sale.report_invoice'



    def render_html(self, cr, uid, ids, data=None, context=None):
        report_obj = self.pool['report']
        posorder_obj = self.pool['pos.order']
        #report = report_obj._get_report_from_name(cr, uid, 'account.report_invoice')  #pos_receipt_format.report_invoice_pos point_of_sale.report_invoice_pos
        selected_orders = posorder_obj.browse(cr, uid, ids, context=context)

        ids_to_print = []
        invoiced_posorders_ids = []
        for order in selected_orders:
            if order.invoice_id:
                ids_to_print.append(order.invoice_id.id)
                invoiced_posorders_ids.append(order.id)

        not_invoiced_orders_ids = list(set(ids) - set(invoiced_posorders_ids))
        if not_invoiced_orders_ids:
            not_invoiced_posorders = posorder_obj.browse(cr, uid, not_invoiced_orders_ids, context=context)
            not_invoiced_orders_names = list(map(lambda a: a.name, not_invoiced_posorders))
            raise osv.except_osv(_('Error!'), _('No link to an invoice for %s.' % ', '.join(not_invoiced_orders_names)))

        docargs = {
            'doc_ids': ids_to_print,
            'doc_model': "account.invoice",
            'docs': selected_orders,
            #'get_unit_amount': self.__unit_amount__,
            'get_ext_amount': self.__ext_amount__,
            'get_ext_cost': self.__ext_cost__,
            'get_ext_promo': self.__ext_promo__,
            'get_retail_ext': self.__retail_ext__,
            'get_quant_total': self.__quant_total__,
            'get_item_total': self.__item_total__,

            'get_lot_qty': self.__lot_qty__,
            'get_lot_retail_price': self.__lot_retail_price__,

            'get_lot_cost_unit': self.__lot_cost_unit__,
            'get_lot_promo_unit': self.__lot_promo_unit__,
            'get_lot_amount_unit': self.__lot_amount_unit__,


        }
        return report_obj.render(cr, uid, ids, 'pos_receipt_format.report_invoice_pos', docargs, context=context) #pos_receipt_format.report_invoice_pos

#RETAIL
    def __lot_qty__(self, line):  #qty if product have option LOT=True/False

        is_lot = line.product_id.is_lot

        if is_lot:
            lot_qty = line.product_id.lot_qty
            line_qty = line.quantity
            qty = lot_qty*line_qty
        else:
            qty = line.quantity

        return qty


    def __lot_retail_price__(self, line):  #retail_price if product have option LOT=True/False

        is_lot = line.product_id.is_lot
        qty = self.__lot_qty__(line)

        if is_lot:
            retail_price = line.product_id.retail_price
            retail_price_u = retail_price / qty

        else:
            retail_price_u = line.product_id.retail_price

        return retail_price_u



#UNIT


    def __lot_cost_unit__(self, line):  #price_unit if product have option LOT=True/False

        is_lot = line.product_id.is_lot
        qty = self.__lot_qty__(line)

        if is_lot:
            price_unit = line.price_unit
            cost_unit_u = price_unit / qty

        else:
            cost_unit_u = line.price_unit

        return cost_unit_u



    #l.price_unit-get_unit_amount(l.price_subtotal,l.quantity,l)


    def __lot_amount_unit__(self, price_subtotal, unit, line):

        is_lot = line.product_id.is_lot
        qty = self.__lot_qty__(line)

        if is_lot:
            unit_amount_u = (price_subtotal / unit) / qty
        else:
            unit_amount_u = price_subtotal / unit

        return unit_amount_u


    def __lot_promo_unit__(self, price_subtotal, unit, line):

        price_unit = self.__lot_cost_unit__(line)
        unit_amount = self.__lot_amount_unit__(price_subtotal, unit, line)

        promo_unit = price_unit - unit_amount

        return promo_unit












    def __item_total__(self, invoice_line):

        i = 0
        for line in invoice_line:
           i += 1

        return i



    def __quant_total__(self, invoice_line):

        #amoi = sum(line.quantity for line in invoice_line)

        qty_total = 0

        for line in invoice_line:

            qty_total = qty_total + self.__lot_qty__(line)


        return qty_total




    def __retail_ext__(self, invoice_line):

        amoi = sum(line.product_id.retail_price*line.quantity for line in invoice_line)

        return amoi




    def __ext_amount__(self, invoice_line):



        amoi = sum(line.price_subtotal for line in invoice_line)

        #_logger.warning("__item_amount__ %s", amoi)

        return amoi

    def __ext_cost__(self, invoice_line):


        uamo = sum(line.quantity*line.price_unit for line in invoice_line)

        #_logger.warning("__units_amount__ %s", uamo)

        return uamo

    def __ext_promo__(self, invoice_line):


        uamo = sum(line.price_subtotal-(line.quantity*line.price_unit) for line in invoice_line)

        #_logger.warning("__units_amount__ %s", uamo)

        return uamo



 #           def _compute_amount(self):
  #      self.amount_untaxed = sum(line.price_subtotal for line in self.invoice_line)
#        self.amount_tax = sum(line.amount for line in self.tax_line)
  #      self.amount_total = self.amount_untaxed + self.amount_tax





