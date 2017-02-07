# -*- coding: utf-8 -*-
{
    'name': "product_ext_view",

    'summary': """
        Extended Product Tree View.
        Add:  "POS category" and "Price".
        Remove:  "status" and "product type".
        """,

    'description': """
         Extended Product Tree View
    """,

    'author': "Viktor Vorobjov",
    'license': 'LGPL-3',s
    'website': 'https://straga.github.io',
    'support': 'vostraga@gmail.com',

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product', 'point_of_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}