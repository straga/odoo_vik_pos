# -*- coding: utf-8 -*-

{
    'name': 'POS Receipt Format',
    'version': '1.0',
    'category': 'Point of Sale',
    'sequence': 6,
    'summary': 'POS  for the Point of Sale ',
    'description': """

=======================

This module adds POS receipt format features to the Point of Sale:


""",
    'author': 'Viktor Vorobjov',
    'depends': ['point_of_sale'],
   
    'license': 'LGPL-3',
    'website': 'https://straga.github.io',
    'support': 'vostraga@gmail.com',


    'data': [
        'views/templates.xml',
        'views/views.xml',
        'views/report_invoice_pos.xml',
        'pos_receipt_format_view.xml'
    ],
    'qweb':[

        'static/src/xml/receipt_format.xml',
    ],
    'installable': True,
    'auto_install': False,
}

