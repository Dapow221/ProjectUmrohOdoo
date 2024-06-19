odoo.define('cdn_arrosyid.signup', function (require) {
    'use strict';

    var ajax = require('web.ajax');

    $(document).on('click', "#submit_signup", function () {
        var email = $("#email").val();
        var name = $("#name").val();
        var password = $("#password").val();
        var confirm_password = $("#confirm_password").val();
        var csrf_token = $("input[name='csrf_token']").val();

        // Pengecekan email ke dalam database sebelum pengiriman data
        ajax.jsonRpc('/check_email_exists', 'call', {'email': email})
        .then(function (result) {
            if (result.exists) {
                alert('Email sudah terdaftar. Gunakan email lain.');
            } else {``

                if (!isValidPassword(password)) {
                    alert('Password tidak memenuhi kriteria.');
                } else {

                    // Lanjutkan dengan pengiriman data pendaftaran
                    var data_pendaftaran = {
                        'email': email,
                        'name': name,
                        'password': password,
                        'confirm_password': confirm_password,
                        'csrf_token': csrf_token
                    };

                    // AJAX untuk membuat pendaftaran baru
                    $.ajax({
                        url: "/create_signup",
                        type: "POST",
                        data: data_pendaftaran,
                        dataType: "json",
                        success: function (data) {
                            console.log("Rekaman baru dibuat dengan ID:", data);
                            alert('Data berhasil disimpan');
                        },
                        error: function (xhr, status, error) {
                            console.error("Kesalahan dalam panggilan AJAX:", error);
                            alert('Kesalahan: ' + error);
                        }
                    });
                }
            }
        });
    });
});