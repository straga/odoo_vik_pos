# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2011 Zikzakmedia S.L. (http://zikzakmedia.com)
#    All Rights Reserved.
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
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
    'name' : 'Extend POS report details',
    'version' : '8.0.0.2',
    'author' : 'Viktor Vorobjov',
    'category': 'POS',
    'description' : """

    	Posible Select Pos category in the report: POS report - Sales Details
    
    """,
    'website' : 'http://www.prolv.net',
    'depends' : ['base_setup','product','point_of_sale'],
    'data': [
        'wizard/pos_details_wzd.xml',
        'point_of_sale_report.xml',
        'views/report_detailsofsales.xml',

    ],
    'auto_install': False,
    'installable': True,
}
