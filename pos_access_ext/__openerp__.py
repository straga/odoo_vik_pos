# -*- coding: utf-8 -*-


{
    'name': 'POS access extended',
    'version': '1.0',
    'category': 'Point of Sale',
    'sequence': 6,
    'summary': 'Access extended Discount and Price for the Point of Sale ',
    'description': """

=======================

This module adds constol access to Discount and Price features to the Point of Sale:


""",
    'author': 'Viktor Vorobjov',
    'depends': ['point_of_sale'],
    'website': 'https://straga.github.io',
    'data': [
        'views/templates.xml',
        'views/views.xml',
    ],
    'qweb':[

        'static/src/xml/access_ext.xml',
    ],
    'installable': True,
    'auto_install': False,
}
