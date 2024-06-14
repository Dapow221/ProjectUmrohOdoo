odoo.define('cdn_arrosyid.website_sesi_umroh', function (require) {
    'use strict';
    
    var ajax = require('web.ajax');
    var core = require('web.core');
    var _t = core._t;
    var rpc = require('web.rpc');
    var QWeb = core.qweb;

    $(document).on('click', "#submit_button_sesi_umroh", function () {
        var sesiName = $(this).closest('tr').find('td:eq(1)').text().trim();
        var sesi_id = $(this).closest('tr').find('td:first').text().trim();
        sessionStorage.setItem('chosenSesiName', sesiName);
        var csrf_token = $("input[name='csrf_token']").val();
        window.location.href = '/pendaftaran_sesi/'+ sesi_id;

        // var sesi = {
        //     'sesi': sesi_id,
        //     'csrf_token': csrf_token
        // };

        // $.ajax({
        //     url: "/pendaftaran_sesi",
        //     type: "POST",
        //     data: sesi,
        //     dataType: "json",
        //     success: function (data) {
        //         console.log("data :", data);
        //         // alert('Data berhasil disimpan');
        //         // window.location.href = '/pendaftaran_sesi';
        //     },
        //     error: function (xhr, status, error) {
        //         console.error("Kesalahan dalam panggilan AJAX:", error);
        //         alert('Kesalahan: ' + error);
        //     }
        // });
        // console.log('________ : ', sesi);


    });

    $(document).on('click', "#action_ketentuan_umroh", function () {
        window.location.href = '/ketentuan';
    });

    $(document).on('click', "#action_contactus", function () {
        window.location.href = '/contactus';
    });

});
