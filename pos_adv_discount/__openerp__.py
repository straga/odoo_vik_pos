# -*- coding: utf-8 -*-


{
    'name': 'POS Advance Discount',
    'version': '1.0',
    'category': 'Point of Sale',
    'sequence': 6,
    'summary': 'POS Advance Discount for the Point of Sale ',
    'description': """

=======================

This module adds POS Advance Discount features to the Point of Sale:


""",
    'author': 'Viktor Vorobjov',
    'depends': ['point_of_sale'],

    'license': 'LGPL-3',
    'website': 'https://straga.github.io',
    'support': 'vostraga@gmail.com',

    'data': [
        'views/templates.xml',
        'pos_adv_discount_views.xml',
        'pos_order_in_views.xml',
        'security/ir.model.access.csv',
    ],
    'qweb':[

        'static/src/xml/adv_discount.xml',
    ],
    'installable': True,
    'auto_install': False,
}

