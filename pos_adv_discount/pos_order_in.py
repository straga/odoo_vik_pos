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

import logging

import openerp
from openerp import tools
from openerp.osv import fields, osv
from openerp.tools.translate import _
import openerp.addons.decimal_precision as dp
import openerp.addons.product.product

import openerp.addons.point_of_sale


_logger = logging.getLogger(__name__)



class pos_order(osv.osv):
    _name = 'pos.order'
    _inherit = 'pos.order'


    def _create_account_move_line(self, cr, uid, ids, session=None, move_id=None, context=None):

        result = super(pos_order, self)._create_account_move_line(cr, uid, ids, session, move_id, context)

        #_logger.warning("result %s", result )

        account_move_obj = self.pool.get('account.move')
        account_period_obj = self.pool.get('account.period')


        for order in self.browse(cr, uid, ids, context=context):

            amount_dis_sub = sum((line.qty * line.price_unit)-line.price_subtotal for line in order.lines)

            if amount_dis_sub != 0:

                current_company = order.sale_journal.company_id


                d_journal_ids = self.pool['account.journal'].search(cr, uid, [
                    ('code', '=', 'DISAL'),
                    ('company_id', '=', current_company.id)
                ], context=context)

                #_logger.warning("d_journal_ids %s", d_journal_ids )

                if not d_journal_ids:

                    raise osv.except_osv(_('Error!'), _("Add first journal for Discount: journal code = DISAL ."))


                #_logger.warning("d_journal_ids %s", d_journal_ids[0] )

                d_debit_n = "default_debit_account_id"
                d_credit_n = "default_credit_account_id"

                results = self.pool['account.journal'].read(cr, uid, [d_journal_ids[0]], [d_debit_n, d_credit_n])

                d_debit_id = results[0][d_debit_n]
                d_credit_id = results[0][d_credit_n]

                #_logger.warning("results %s", results )
                #_logger.warning("d_debit %s", d_debit_id[0] )
                #_logger.warning("d_credit %s", d_credit_id[0] )

                move_id2 = account_move_obj.create(cr, uid, {
                    'ref' : order.name,
                    'journal_id': d_journal_ids[0]
                }, context=context)


                #_logger.warning("amount_sub %s", amount_dis_sub )

                period = account_period_obj.find(cr, uid, context=dict(context or {}, company_id=current_company.id))[0]

                all_lines = []
                all_lines.append((0, 0,

                        {
                            'name': 'Discount Credit',
                            'ref': order.name,
                            'journal_id': d_journal_ids[0],
                            'company_id': current_company.id,
                            'credit': amount_dis_sub,
                            'period_id': period,
                            'debit': 0.0,
                            'date': order.date_order[:10],
                            'partner_id': False,
                            'move_id': move_id2,
                            'account_id':  d_credit_id[0]
                        }))


                all_lines.append((0, 0,

                        {
                            'name': 'Discount Debit',
                            'ref': order.name,
                            'journal_id': d_journal_ids[0],
                            'company_id': current_company.id,
                            'credit': 0.0,
                            'period_id': period,
                            'debit': amount_dis_sub,
                            'date': order.date_order[:10],
                            'partner_id': False,
                            'move_id': move_id2,
                            'account_id':  d_debit_id[0]
                        }))


                if move_id2:
                    self.pool.get("account.move").write(cr, uid, [move_id2], {'line_id':all_lines}, context=context)

        return result

