# -*- coding: utf-8 -*-
{
    'name' : 'Extend POS report session summary',
    'version' : '8.0.0.2',
    'author' : 'Viktor Vorobjov',
    'category': 'POS',
    'description' : """

    	Possible print in small printer: POS session - Session Summary
    
    """,

    'license': 'AGPL-3',
    'website': 'https://straga.github.io',
    'support': 'vostraga@gmail.com',

    'depends' : ['base_setup','product','point_of_sale', 'qweb_usertime'],
    'data': [
        'data/report_paperformat.xml',
        'point_of_sale_report.xml',
        'views/report_session_summary.xml',

    ],
    'auto_install': False,
    'installable': True,
}
