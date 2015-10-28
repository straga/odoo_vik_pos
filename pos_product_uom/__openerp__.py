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


{
    'name': 'POS product uom',
    'version': '1.0',
    'category': 'Point of Sale',
    'sequence': 6,
    'summary': 'Kg to lbs product for the Point of Sale ',
    'description': """

=======================

This module change product screen UOM from kg to lbs,  features to the Point of Sale:


""",
    'author': 'Viktor Vorobjov',
    'depends': ['point_of_sale'],
    'website': 'https://straga.github.io',
    'data': [

    ],
    'qweb':[

        'static/src/xml/uom_product.xml',
    ],
    'installable': True,
    'auto_install': False,
}

