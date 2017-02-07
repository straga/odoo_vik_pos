# -*- coding: utf-8 -*-

{
    'name': 'Internal Reference Product',
    'version': '1.0',
    'category': 'Point of Sale',
    'sequence': 6,
    'summary': 'Internal Reference for the Point of Sale ',
    'description': """

=======================

This module adds Internal Reference marker for product features to the Point of Sale:


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

        'static/src/xml/ref_product.xml',
    ],
    'installable': True,
    'auto_install': False,
}

