# -*- coding: utf-8 -*-

import logging

import openerp
from openerp import tools
from openerp.osv import fields, osv
from openerp.tools.translate import _

import time
import datetime

from dateutil import rrule


_logger = logging.getLogger(__name__)


class pos_adv_discount(osv.osv):
    _name = 'pos.adv_discount'
    _description = "POS advance discount info"



    def _get_available_pfilters(self, cr, uid, context=None):
        """
           This function will return the list of filter allowed according
           :pres_filter: list of tuple
        """
        #default available choices
        pres_filter = [
            ('all', _('All products')),
            ('category', _('Specific product categories')),
            ('product', _('Specific products')) ]

        return pres_filter

    def _get_available_cfilters(self, cr, uid, context=None):
        """
           This function will return the list of filter allowed according
           :pres_filter: list of tuple
        """
        #default available choices
        pres_filter = [
            ('all', _('All customer')),
            ('customer', _('Specific customers'))]

        return pres_filter

    def _get_special_rule(self, cr, uid, context=None):
        """
           This function will return the list of filter allowed according
           :pres_filter: list of tuple
        """
        #default available choices
        pres_filter = [
            ('b1gdisc', _('Buy one and get another Discount')),
            ('b1gfree', _('Buy one and get another Free'))]

        return pres_filter

    def _get_value_method(self, cr, uid, context=None):
        """
           This function will return the list of filter allowed according
           :pres_filter: list of tuple
        """
        #default available choices
        pres_filter = [
            ('percent', _('Percentage off')),
            ('amount', _('Amount off'))]

        return pres_filter


    def _get_discount_type(self, cr, uid, context=None):
        """
           This function will return the list of filter allowed according
           :pres_filter: list of tuple
        """
        #default available choices
        pres_filter = [
            ('simple_dsc', _('Simple Discount')),
            ('min_purchase_dsc', _('Minimum Purchase Discount')),
            ('buygetfree', _('Buy N Get one Free')),
            ('BuyXforpriceY', _('Buy X for the price of Y')),
            ('paired_dsc', _('Paired Discount')),
            ('paired_set_dsc', _('Paired set Discount')),
            ('BuyXforFixedpriceY', _('Buy X for Fixed price Y')),

            ]

        return pres_filter


    def on_change_amount(self, cr, uid, ids, amount=False, context=None):

        res = {}

        if amount > 100:
            res['amount'] = 0

            warning = {
                'title': _('Ammount off!'),
                'message' : _('Amount - is above > 100%')
            }
            return {'warning': warning, 'value': res}


    def on_change_value_method(self, cr, uid, ids, value_method=False, context=None):

        res = {}

        if value_method == "" or value_method == "none" or value_method is False:

            res['value_method'] = 'percent'
            return {'value': res}

        if value_method == "amount":

            res['value_method'] = 'percent'

            warning = {
                'title': _('Ammount off!'),
                'message' : _('If you require this feature please contact your system administrator.')
            }
            return {'warning': warning, 'value': res}


    def on_change_discount_type(self, cr, uid, ids, discount_type=False, context=None):

        res = {}

        if discount_type == "" or discount_type == "none" or discount_type is False:

            res['discount_type'] = 'simple_dsc'
            return {'value': res}

        if discount_type == "BuyXforpriceY":

            res['discount_type'] = 'BuyXforpriceY'
            return {'value': res}

        if discount_type == "BuyXforFixedpriceY":

            res['discount_type'] = 'BuyXforFixedpriceY'
            return {'value': res}

        if discount_type == "buygetfree":

            res['discount_type'] = 'buygetfree'
            warning = {
                'title': _('Discount type!'),
                'message' : _('If you require this feature please contact your system administrator.')
            }
            return {'warning': warning, 'value': res}

        if discount_type == "min_purchase_dsc":

            res['discount_type'] = 'simple_dsc'
            warning = {
                'title': _('Discount type!'),
                'message' : _('If you require this feature please contact your system administrator.')
            }
            return {'warning': warning, 'value': res}

        if discount_type == "paired_dsc":

            res['discount_type'] = 'simple_dsc'
            warning = {
                'title': _('Discount type!'),
                'message' : _('If you require this feature please contact your system administrator.')
            }
            return {'warning': warning, 'value': res}

        if discount_type == "paired_set_dsc":

            res['discount_type'] = 'simple_dsc'
            warning = {
                'title': _('Discount type!'),
                'message' : _('If you require this feature please contact your system administrator.')
            }
            return {'warning': warning, 'value': res}



    def on_change_date(self, cr, uid, ids, start_date=False, end_date=False, context=None):

        context = dict(context or {})
        res = {}

        if end_date != False:
            if end_date < start_date or start_date > end_date:
                res['end_date'] = ''
                warning = {
                    'title': _('Date incorect!'),
                    'message' : _('Error: End date is earlier than Start Date')
                }
                return {'warning': warning, 'value': res}
        else:
            return


    _columns = {

        'name': fields.char('Name', size=50, required=True),
        'code': fields.char('Code', size=50, required=True),
        'default_debt_account': fields.char('Default debt account', size=20),
        'default_credit_account': fields.char('Default credit account', size=20),

        'journal_id': fields.many2one('account.journal', 'Available Journal'),

        'start_date': fields.datetime('Start Date'),
        'end_date': fields.datetime('End Date'),

        'value_method': fields.selection(_get_value_method, 'Value Method', required=True),
        'amount': fields.integer('Amount', required=True),


        'cfilter': fields.selection(_get_available_cfilters, 'Selection Customer Filter', required=True),



        'discount_type': fields.selection(_get_discount_type, 'Selection Discount', required=True),


        'partner': fields.many2many('res.partner', 'pos_adv_disc_partner_rel', 'pos_ad_dic_id', 'partner_id', 'Customer'),
        'product': fields.many2many('product.product', 'pos_adv_disc_product_rel', 'pos_ad_dic_id', 'product_id', 'Product'),
        'pcategory': fields.many2many('pos.category', 'pos_adv_disc_pcategory_rel', 'pos_ad_dic_id', 'category_id', 'POS category'),



        'pfilter': fields.selection(_get_available_pfilters, 'Selection Product Filter', required=True),

        'special_rule': fields.selection(_get_special_rule, 'Selection Discount Rule', required=False),

        'active': fields.boolean('Active Discount', default=True),

        'product_1': fields.many2one('product.product', 'Product 1', change_default=True, select=True),
        'pro_val_1': fields.integer('val 1'),

        'product_2': fields.many2one('product.product', 'Product 2', change_default=True, select=True),
        'pro_val_2': fields.integer('val 2'),

        }

    _defaults = {
        'cfilter': 'all',
        'pfilter': 'all',
        'start_date': datetime.datetime.today(),
    }

    def create(self, cr, uid, vals, context=None):
        context = dict(context or {})

        result = super(pos_adv_discount, self).create(cr, uid, vals, context)
        self.validate(cr, uid, [result], context=context)
        self.validate_amount(cr, uid, [result], context=context)

        return result

    def write(self, cr, uid, ids, vals, context=None):

        if context is None:
            context = {}
        #_logger.warning("vals %s", vals )

        result = super(pos_adv_discount, self).write(cr, uid, ids, vals, context=context)
        self.validate(cr, uid, ids, context=context)
        self.validate_amount(cr, uid, ids, context=context)
        return result

    def _get_date_range(self, cr, uid, ids, date_from=None, date_to=None ,  context=None):

        date_list = []

        for dd in rrule.rrule(rrule.DAILY,
                    dtstart=datetime.datetime.strptime(date_from, "%Y-%m-%d %H:%M:%S"),
                    until=datetime.datetime.strptime(date_to, "%Y-%m-%d %H:%M:%S")):

            date_list.append(dd)

        return date_list


    def validate_amount(self, cr, uid, ids, context=None):


        for discount in self.browse(cr, uid, ids, context):

            start_date = discount.start_date
            end_date = discount.end_date

        #_logger.warning("date_data %s", date_data )

        #_logger.warning("start_date %s", start_date )
        #_logger.warning("end_date %s", end_date )

        adv_discount_ids = self.pool['pos.adv_discount'].search(cr, uid, [

            ('active', '=', True),
            ('start_date', '<=', start_date),'|',
            ('end_date', '<=', end_date),
            ('end_date', '=', False)

                ], context=context)


        #_logger.warning("adv_discount_ids %s", adv_discount_ids )



    def validate(self, cr, uid, ids, context=None):


        for discount in self.browse(cr, uid, ids, context):

            cfilter = discount.cfilter
            partners = discount.partner

            pfilter = discount.pfilter

            products = discount.product
            categories = discount.pcategory


            if cfilter in 'customer' and len(partners.ids) == 0:

                raise osv.except_osv(_('Error!'), _("Cannot save! You must select customers."))

            if pfilter in 'product' and len(products.ids) == 0:

                raise osv.except_osv(_('Error!'), _("Cannot save! You must need select products."))

            if pfilter in 'category' and len(categories.ids) == 0:

                raise osv.except_osv(_('Error!'), _("Cannot save! You must need select categories."))



pos_adv_discount()








