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

from openerp import models, fields, api, osv
from openerp.tools.translate import _

_logger = logging.getLogger(__name__)



class ProductTemplate(models.Model):
    _inherit = 'product.template'

    wic_ok = fields.Boolean(string='WIC', help='Determine if the it WIC product. If set WIC , automaticly set EBT too.')
    ebt_ok = fields.Boolean(string='EBT', help='Determine if the it EBT product')


    @api.onchange('wic_ok')
    def _onchange_wic_ok(self):
        if self.wic_ok:
            self.ebt_ok = True



    @api.model
    def create(self, vals):

        try:
            if vals['wic_ok']:
                vals['ebt_ok'] = True
        except Exception:
            pass

        return super(ProductTemplate, self).create(vals)

    @api.multi
    def write(self, vals):

        vals = vals or {}

        try:
            if vals['wic_ok']:
                vals['ebt_ok'] = True
        except Exception:
            pass

        return super(ProductTemplate, self).write(vals)


    @api.one
    def copy(self, default=None):
        if default is None:
            default = {}
        if self.default_code:
            default.update({
                'ebt_ok': self.ebt_ok,
                'wic_ok': self.wic_ok,
            })

        return super(ProductTemplate, self).copy(default)


