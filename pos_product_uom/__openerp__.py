# -*- coding: utf-8 -*-

{
    'name': 'POS product uom',
    'version': '1.0',
    'category': 'Point of Sale',
    'sequence': 6,
    'summary': 'Kg to lbs product for the Point of Sale ',
    'description': """

=======================

This module change product screen UOM from kg to lbs,  features to the Point of Sale:


""",
    'author': 'Viktor Vorobjov',
    'depends': ['point_of_sale'],
    'license': 'LGPL-3',
    'website': 'https://straga.github.io',
    'support': 'vostraga@gmail.com',
    'data': [

    ],
    'qweb':[

        'static/src/xml/uom_product.xml',
    ],
    'installable': True,
    'auto_install': False,
}

