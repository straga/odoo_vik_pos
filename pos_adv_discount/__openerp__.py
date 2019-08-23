# -*- coding: utf-8 -*-
{
    "name": """POS Advance Discount""",
    "summary": """POS Advance Discount for the Point of Sale""",
    "category": "Point of Sale",
    "images": ['static/description/icon.png'],
    "version": "2.0.0",

    "description": """
    UPDATE: add discount manual

    =======================

    This module adds POS Advance Discount features to the Point of Sale:

    """,

    "author": "Viktor Vorobjov",
    "license": "LGPL-3",
    "website": "https://straga.github.io",
    "support": "vostraga@gmail.com",

    "depends": [
        "point_of_sale",

    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        'views/templates.xml',
        'pos_adv_discount_views.xml',
        'pos_order_in_views.xml',
        'security/ir.model.access.csv',
    ],
    "qweb": [

        'static/src/xml/adv_discount.xml',
    ],
    "demo": [],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "installable": True,
    "auto_install": False,
    "application": False,
}



