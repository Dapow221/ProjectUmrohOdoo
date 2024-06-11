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
    'category': 'Travel',
    'version': '1.0.0',
    'depends': ['base', 'product', 'account', 'l10n_id_efaktur', 'mail', 'website'],

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
        'views/menu_website.xml',
        'views/homepage_templates.xml',
        'views/sesi_umroh_templates.xml',
        'views/ketentuan_umum_templates.xml',
        'views/pendaftaran_umroh_templates.xml',
        'views/profil_templates.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'cdn_arrosyid/static/src/js/pendaftaran.js',
            'cdn_arrosyid/static/src/css/layout.css',
        ],
    },
}