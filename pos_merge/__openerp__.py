# -*- coding: utf-8 -*-
{
    'name': 'POS merge',
    'version': '1.0',
    'category': 'Point of Sale',
    'sequence': 6,
    'summary': 'POS merge for the Point of Sale ',
    'description': """

=======================

This module adds POS  features to the Point of Sale:


""",
    'author': 'Viktor Vorobjov',
    'depends': ['point_of_sale'],
    
    'license': 'LGPL-3',
    'website': 'https://straga.github.io',
    'support': 'vostraga@gmail.com',

    'data': [
        'views/templates.xml',
    ],
    'qweb':[

        'static/src/xml/merge.xml',
    ],
    'installable': True,
    'auto_install': False,
}

