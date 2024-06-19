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
    'depends': ['base', 'product', 'account', 'l10n_id_efaktur', 'mail', 'website', 'portal', 'web', 'contacts',],

    'data': [
        # security
        'security/groups.xml',
        'security/ir.model.access.csv',

        # data
        'data/navbar_templates.xml',
        'data/sequence_data.xml',

        # report
        'reports/report_identitas_manifes_jamaah.xml',
        'reports/report_kartu_identitas_jamaah.xml',
        'reports/wizard_cetak_laporan_bulanan.xml',

        # wizard
        'wizards/wizard_pembayaran.xml',
        'wizards/wizard_pendaftaran.xml',
        'wizards/wizard_proses_perjalanan.xml',
        'wizards/wizard_list_perjalanan.xml',
        'wizards/wizard_laporan_bulanan.xml',

        # views backend
        'views/menu.xml',
        'views/transaksi_sesiumroh.xml',
        'views/rencana_perjalanan.xml',
        'views/paket_umroh.xml',
        'views/maskapai.xml',
        'views/identitas_peserta_umroh.xml',
        'views/identitas_petugas_lapangan.xml',
        'views/identitas_ustadz_pembimbing.xml',
        'views/hotel.xml',
        'views/perlengkapan.xml',
        'views/invoice_inherit.xml',
        'views/pendaftaran.xml',
        'views/penagihan.xml',
        # 'views/tes.xml',

        # views website
        'views/navbar_templates.xml',
        'views/footer_templates.xml',
        'views/register_templates.xml',
        'views/homepage_templates.xml',
        'views/sesi_umroh_templates.xml',
        'views/ketentuan_umum_templates.xml',
        'views/pendaftaran_umroh_templates.xml',
        'views/profil_templates.xml',
        'views/signup_templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'cdn_arrosyid/static/src/js/pendaftaran.js',
            'cdn_arrosyid/static/src/js/website_sesi_umroh.js',
            'cdn_arrosyid/static/src/css/layout.css',
            'cdn_arrosyid/static/src/js/layout.js',
            'cdn_arrosyid/static/src/js/signup.js',
            'cdn_arrosyid/static/src/js/password.js',
            'cdn_arrosyid/static/src/js/custom.js',
        ],
        'web.assets_backend': [
            'cdn_arrosyid/static/src/js/peta.js',
            'cdn_arrosyid/static/src/js/lmap_renderer.js',
            'cdn_arrosyid/static/src/js/lmap_controller.js',
            'cdn_arrosyid/static/src/js/lmap_view.js',
            'cdn_arrosyid/static/src/js/lmap_model.js',
            'https://unpkg.com/leaflet@1.7.1/dist/leaflet.css',
            'https://unpkg.com/leaflet@1.7.1/dist/leaflet.js',
            'cdn_arrosyid/static/src/xml/peta.xml',
            'cdn_arrosyid/static/src/xml/lmap_renderer.xml',
            'cdn_arrosyid/static/src/xml/lmap_controller.xml',
        ],
        'website.assets_editor': [
            'cdn_arrosyid/static/src/js/tour.js',
            'cdn_arrosyid/static/src/xml/widget_peta.xml',

        ],
    },
}