odoo.define('cdn_arrosyid.custom', function (require) {
    'use strict';

    var core = require('web.core');
    var rpc = require('web.rpc');
    var ajax = require('web.ajax');

	$(document).ready(function() {
        $(document).on('click', '.btn_detail_tagihan', function() {
            var dt = $(this).data('dt_tagihan_id');
            console.log('Tagihan ID:', dt);
        });
    });

    $('#btn_submit_pembayaran').click(function() {
        var csrf_token = $("input[name='csrf_token']").val();
        var metode_bayar = $("#metode_bayar").val();
        var jml_pembayaran = $("#jml_pembayaran").val();
        var tagihan_id = $("#tagihan_id").val();
        var tgl_pembayaran = $("#tgl_pembayaran").val();
        var dt_partner_id = $("#dt_partner_id").val();

        var data_pembayaran = {
            'metode_bayar': metode_bayar,
            'jml_pembayaran': jml_pembayaran,
            'tagihan_id': tagihan_id,
            'tgl_pembayaran': tgl_pembayaran,
            'dt_partner_id': dt_partner_id,
            'csrf_token': csrf_token
        };
        console.log('data : ', data_pembayaran);

        $.ajax({
            url: "/buat_pembayaran",
            type: "POST",
            data: data_pembayaran,
            dataType: "json",
            success: function (data) {
                console.log("Rekaman baru dibuat dengan ID:", data);
                alert('Pembayaran berhasil');
            },
            error: function (xhr, status, error) {
                console.error("Kesalahan dalam panggilan AJAX:", error);
                alert('Kesalahan: ' + error);
            }
        });

    });
})