odoo.define('cdn_arrosyid.signup', function (require) {
    'use strict';

    var ajax = require('web.ajax');

    $(document).ready(function () {

        $(document).on('click', "#submit_signup", function () {
            var email = $("#email").val();
            var name = $("#name").val();
            var password = $("#password").val();
            var confirm_password = $("#confirm_password").val();
            var csrf_token = $("input[name='csrf_token']").val();
            
            // Validasi bahwa email tidak boleh kosong
            if (email === "") {
                alert('Email tidak boleh kosong.');
                return; // Menghentikan proses jika email kosong
            }

            if (password !== confirm_password) {
                alert('Konfirmasi password tidak cocok dengan password. Silakan coba lagi.');
                return; // Berhenti jika tidak valid
            }

            // Pengecekan email ke dalam database sebelum pengiriman data
            ajax.jsonRpc('/check_email_exists', 'call', {'email': email})
            .then(function (result) {
                if (result.exists) {
                    alert('Email sudah terdaftar. Gunakan email lain.');
                } else {

                    // Validasi password
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
                        console.log('Data Jamaah:', data_pendaftaran);

                        $.ajax({
                            url: "/create_signup",
                            type: "POST",
                            data: data_pendaftaran,
                            dataType: "json",
                            success: function (data) {
                                console.log("Pendaftaran banyak berhasil:", data);
                                alert('Data berhasil disimpan');
                                // window.location.href = "/register_berhasil";
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
});
