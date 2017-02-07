# -*- coding: utf-8 -*-
{
    'name': 'POS subtotal',
    'version': '1.0',
    'category': 'Point of Sale',
    'sequence': 6,
    'summary': 'POS  for the Point of Sale ',
    'description': """

=======================

This module adds POS features to the Point of Sale:


""",
    'author': 'Viktor Vorobjov',
    'license': 'LGPL-3',
    'website': 'https://straga.github.io',
    'support': 'vostraga@gmail.com',

    'depends': ['point_of_sale'],
    
    'data': [
        'views/templates.xml',
        'views/views.xml',
    ],
    'qweb':[

        'static/src/xml/subtotal.xml',
    ],
    'installable': True,
    'auto_install': False,
}

