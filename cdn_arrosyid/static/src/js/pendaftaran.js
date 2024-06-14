odoo.define('cdn_arrosyid.pendaftaran', function (require) {
    'use strict';

    var core = require('web.core');
    var rpc = require('web.rpc');
    var ajax = require('web.ajax');

    $(document).on('change', "#paket_umroh", function () {
        var paket_id = $("#paket_umroh").val();
        var selectSesi = $("#sesi_umroh");
        var harga = $("#harga");
        // console.log('data :', paket_id);

        selectSesi.empty();
        function get_sesi(){
            rpc.query({
                model: 'cdn.sesi.umroh',
                method: 'search_read', 
                args: [[]],
                kwargs: {
                    fields: ['id', 'name', 'paket_umroh_id', 'lst_price', 'keterangan', 'tanggal_berangkat', 'tanggal_pulang', 'pembimbing_id'],
                }
            }).then(function (result) {
                result.forEach(sesi => {
                    if (sesi.paket_umroh_id[0] === parseInt(paket_id)) {
                        console.log("Data data:", sesi);
                        // Create a new option element
                        var option = $('<option>', {
                            value: sesi.id,
                            text: sesi.name
                        });
                        // Append the option to the select element
                        selectSesi.append(option);
                        harga.val(formatRupiah(sesi.lst_price));
                        // modal
                        $("#nama_sesi_modal").text(sesi.name);
                        $("#keterangan_sesi").text(sesi.keterangan);
                        $("#tgl_brk").text(sesi.tanggal_berangkat);
                        $("#tgl_plg").text(sesi.tanggal_pulang);
                        $("#hotel").text(sesi.hotel_id);
                        $("#maskapai").text(sesi.maskapai_id);
                        $("#pembimbing").text(sesi.pembimbing_id);
                        $("#petugas").text(sesi.petugas_ids);
                    }
                });
            });
        }
        get_sesi();
        function formatRupiah(angka) {
            var reverse = angka.toString().split('').reverse().join(''),
            ribuan = reverse.match(/\d{1,3}/g);
            ribuan = ribuan.join('.').split('').reverse().join('');
            return 'Rp ' + ribuan;
        }
    }); 

    $(document).on('click', "#submit_pendaftaran", function () {
        var jamaah = $("#jamaah_umroh").val();
        var sesi = $("#sesi_umroh").val();
        var csrf_token = $("input[name='csrf_token']").val();
        var data_pendaftaran = {
            'jamaah_id': parseInt(jamaah),
            'sesi_id': parseInt(sesi),
            'csrf_token': csrf_token
        };

        // console.log('data_pendaftaran : ', data_pendaftaran);
    
        $.ajax({
            url: "/buat_pendaftaran",
            type: "POST",
            data: data_pendaftaran,
            dataType: "json",
            success: function (data) {
                console.log("Rekaman baru dibuat dengan ID:", data);
                // alert('Data berhasil disimpan');
                window.location.href = "/pendaftaran_berhasil";
            },
            error: function (xhr, status, error) {
                console.error("Kesalahan dalam panggilan AJAX:", error);
                alert('Kesalahan: ' + error);
            }
        });
    });  
    
})