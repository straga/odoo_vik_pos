# -*- coding: utf-8 -*-
{
    "name": """POS Access Code""",
    "summary": """Access extended - Discount and Price for the Point of Sale""",
    "category": "Point of Sale",
    "images": ['static/description/icon.png'],
    "version": "1.0.0",

    "description": """

    =======================

    This module adds constol access to Discount and Price features to the Point of Sale:

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
        'views/views.xml',
    ],
    "qweb": [

        'static/src/xml/access_ext.xml',
    ],
    "demo": [],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "installable": True,
    "auto_install": False,
    "application": False,
}






