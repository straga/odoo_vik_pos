# -*- coding: utf-8 -*-
{
    'name': 'POS items counter',
    'version': '1.0',
    'category': 'Point of Sale',
    'sequence': 6,
    'summary': 'Items couting in categories for the Point of Sale ',
    'description': """

=======================

This module adds show Items couting in categories features to the Point of Sale:


""",
    'author': 'Viktor Vorobjov',
    'depends': ['point_of_sale'],

    'license': 'LGPL-3',
    'website': 'https://straga.github.io',
    'support': 'vostraga@gmail.com',

    'data': [
        'views/templates.xml',
        'views/views.xml',
    ],
    'qweb':[

        'static/src/xml/items_counter.xml',
    ],
    'installable': True,
    'auto_install': False,
}
