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
    'depends': ['base', 'product', 'account', 'l10n_id_efaktur', 'mail', 'website'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'data/sequence_data.xml',
        'views/menu.xml',
        'record/cetak_identitas_jamaah.xml',
        'record/cetak_manifes_jamaah.xml',
        'views/transaksi_sesiumroh.xml',
        'views/rencana_perjalanan.xml',
        'views/paket_umroh.xml',
        'views/maskapai.xml',
        'views/identitas_peserta_umroh.xml',
        'views/identitas_petugas_lapangan.xml',
        'views/identitas_ustadz_pembimbing.xml',
        'views/hotel.xml',
        'views/perlengkapan.xml',
        'wizards/wizard_pembayaran.xml',
        'wizards/wizard_pendaftaran.xml',
        'wizards/wizard_proses_perjalanan.xml',
        'wizards/wizard_list_perjalanan.xml',
        'views/invoice_inherit.xml',
        'views/pendaftaran.xml',
        'views/penagihan.xml',
        'views/homepage_templates.xml',
        'views/sesi_umroh_templates.xml',
        'views/ketentuan_umum_templates.xml',
        'views/pendaftaran_umroh_templates.xml',
        'views/profil_templates.xml',
        'views/menu_website.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
        
    ],
    'css': ['static/src/css/custom.css'],
}
