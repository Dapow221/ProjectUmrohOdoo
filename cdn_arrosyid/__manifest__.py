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
    'depends': ['base', 'product', 'account', 'l10n_id_efaktur', 'mail', 'website', 'portal', 'web', 'auth_signup'],

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
        'views/signup_templates.xml',

        'views/snippets/s_banner.xml',
        'views/snippets/s_picture.xml',
        'views/snippets/s_image_text.xml',
        'views/snippets/s_text_image.xml',
        'views/snippets/s_three_columns.xml',
        'views/snippets/s_quotes_carousel.xml',
        'views/snippets/s_text_block.xml',
        'views/snippets/s_masonry_block.xml',
        'views/snippets/s_numbers.xml',
        'views/snippets/s_title.xml',
        'views/snippets/s_image_gallery.xml',
        'views/snippets/s_call_to_action.xml',
    ],
    'images': [
        'static/description/real_estate_description.png',
        'static/description/real_estate_screenshot.jpg',
    ],
    'images_preview_theme': {
        'website.s_banner_default_image': '/cdn_arrosyid/static/src/img/snippets/s_banner.jpg',
        'website.s_text_image_default_image': '/cdn_arrosyid/static/src/img/snippets/s_text_image.jpg',
        'website.s_image_text_default_image': '/cdn_arrosyid/static/src/img/snippets/s_image_text.jpg',
        'website.s_three_columns_default_image_1': '/cdn_arrosyid/static/src/img/snippets/library_image_11.jpg',
        'website.s_three_columns_default_image_2': '/cdn_arrosyid/static/src/img/snippets/library_image_13.jpg',
        'website.s_three_columns_default_image_3': '/cdn_arrosyid/static/src/img/snippets/library_image_07.jpg',
        'website.s_masonry_block_default_image_1': '/cdn_arrosyid/static/src/img/snippets/s_masonry_block.jpg',
        'website.s_quotes_carousel_demo_image_1': '/cdn_arrosyid/static/src/img/snippets/s_quotes_carousel_1.jpg',
    },
    'demo': [
        'demo/demo.xml',
    ],
    'snippet_lists': {
        'homepage': ['s_banner', 's_text_block', 's_text_image', 's_image_text', 's_title', 's_three_columns',
                     's_title', 's_masonry_block', 's_numbers', 's_quotes_carousel'],
    },
    'assets': {
        'web.assets_frontend': [
            'cdn_arrosyid/static/src/js/pendaftaran.js',
            'cdn_arrosyid/static/src/css/layout.css',
            'cdn_arrosyid/static/src/js/layout.js',
        ],
        'website.assets_editor': [
            'cdn_arrosyid/static/src/js/tour.js',
        ],
    },
}