
# -*- coding: utf-8 -*-
{
    "name": "product_ext_view",

    "summary": """
        Extended Product Tree View.
        Add:  "POS category" and "Price".
        Remove:  "status" and "product type".
        """,

    "description": """
         Extended Product Tree View
    """,

    "author": "Viktor Vorobjov",
    "license": "LGPL-3",
    "website": "https://straga.github.io",
    "support": "vostraga@gmail.com",

    "depends": [
        'base', 'product', 'point_of_sale'

    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "templates.xml",
    ],
    "qweb": [

    ],
    "demo": [
        "demo.xml",
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "installable": True,
    "auto_install": False,
    "application": False,
}
