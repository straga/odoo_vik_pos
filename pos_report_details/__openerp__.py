# -*- coding: utf-8 -*-

{
    'name' : 'Extend POS report details',
    'version' : '8.0.0.2',
    'author' : 'Viktor Vorobjov',
    'category': 'POS',
    'description' : """

    	Posible Select Pos category in the report: POS report - Sales Details
    
    """,

    'license': 'LGPL-3',
    'website': 'https://straga.github.io',
    'support': 'vostraga@gmail.com',

    'depends' : ['base_setup','product','point_of_sale'],
    'data': [
        'wizard/pos_details_wzd.xml',
        'point_of_sale_report.xml',
        'views/report_detailsofsales.xml',

    ],
    'auto_install': False,
    'installable': True,
}
