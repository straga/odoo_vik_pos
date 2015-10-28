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
    'website': "http://www.prolv.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
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