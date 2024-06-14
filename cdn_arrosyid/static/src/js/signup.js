odoo.define('cdn_arrosyid.signup', function (require) {
    'use strict';

    var core = require('web.core');
    var rpc = require('web.rpc');
    var ajax = require('web.ajax');

    $(document).on('click', "#submit_signup", function () {
        var email = $("#email").val();
        var name = $("#name").val();
        var password = $("#password").val();
        var confirm_password = $("#confirm_password").val();
        var csrf_token = $("input[name='csrf_token']").val();
        var data_pendaftaran = {
            'email': email,
            'name': name,
            'password': password,
            'confirm_password': confirm_password,
            'csrf_token': csrf_token
        };

        // console.log('data_pendaftaran : ', data_pendaftaran);
    
        $.ajax({
            url: "/create_signup",
            type: "POST",
            data: data_pendaftaran,
            dataType: "json",
            success: function (data) {
                console.log("Rekaman baru dibuat dengan ID:", data);
                // alert('Data berhasil disimpan');
                window.location.href = "/web/login";
            },
            error: function (xhr, status, error) {
                console.error("Kesalahan dalam panggilan AJAX:", error);
                alert('Kesalahan: ' + error);
            }
        });

    });    
})