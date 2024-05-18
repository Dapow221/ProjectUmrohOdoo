# -*- coding: utf-8 -*-
{
    'name': "cdn_arrosyid",

    'summary': """
        Aplikasi Pengelolaan Travel Umroh AR ROSYID TOUR""",

    'description': """
        Travel Umroh AR ROSYID TOUR
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Travel',
    'version': '1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/menu.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/transaksi_sesiumroh.xml',
        'views/rencana_perjalanan.xml',
        'views/paket_umroh.xml',
        'views/maskapai.xml',
        'views/identitas_jamaah.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
