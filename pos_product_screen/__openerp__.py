# -*- coding: utf-8 -*-

{
    'name': 'POS product screen',
    'version': '1.0',
    'category': 'Point of Sale',
    'sequence': 6,
    'summary': 'POS product screen for the Point of Sale ',
    'description': """

=======================

This module adds POS product screen features to the Point of Sale:


""",
    'author': 'Viktor Vorobjov',
    'depends': ['point_of_sale'],

    'license': 'LGPL-3',
    'website': 'https://straga.github.io',
    'support': 'vostraga@gmail.com',

    'data': [
        'views/templates.xml',
        'views/screen_product_views.xml',
       
    ],
    'qweb':[

        'static/src/xml/hide.xml',
    ],
    'installable': True,
    'auto_install': False,
}

