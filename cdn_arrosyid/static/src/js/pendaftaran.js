odoo.define('cdn_arrosyid.pendaftaran', function (require) {
    'use strict';

    var core = require('web.core');
    var rpc = require('web.rpc');
    var ajax = require('web.ajax');

    


    $('input[name="radio_dftr"]').change(function() {
        var selectedValue = $(this).val();

        if (selectedValue === "sendiri") {
            $('#paket_sendiri').fadeIn();
            $('#paket_jamaah').prop('hidden', false).fadeOut();
        } else if (selectedValue === "jamaah") {
            $('#paket_sendiri').fadeOut();
            $('#paket_jamaah').prop('hidden', false).fadeIn();
        }
    });

    // pendaftaran form
    function updateTotalCount() {
        var totalCount = $(".table tbody tr").length;
        $("#ttl_dft_jamaah").text("(" + totalCount + ")");
    }
    updateTotalCount();

    function removeRow() {
        $(".dlt_jamaah").click(function(){
            $(this).closest("tr").remove();
            updateTotalCount(); // Update total count after removal
        });
    }
    removeRow();

    function toggleTanggalUmrohField() {
        var isUmrohChecked = $('#sudah_umroh').is(':checked');
        if (isUmrohChecked) {
            $('#tanggal_umroh_field').show();
        } else {
            $('#tanggal_umroh_field').hide();
        }
    }

    function toggleNamaPasanganField() {
        var isMenikahChecked = $('#sudah_menikah').is(':checked');
        if (isMenikahChecked) {
            $('#nama_pasangan_field').show();
        } else {
            $('#nama_pasangan_field').hide();
        }
    }

    $(document).ready(function() {
        toggleTanggalUmrohField();
        toggleNamaPasanganField();

        var pendidikanDefault     = $('#pendidikan').data('default');
        var golongan_darahDefault = $('#golongan_darah_dropdown').data('default');
        var pekerjaanDefault      = $('#pekerjaan_dropdown').data('default');
        var vaksin_covid19Default = $('#vaksin_covid19_dropdown').data('default');
        if (pendidikanDefault) {
            $('#pendidikan option').each(function() {
                if ($(this).val() === pendidikanDefault) {
                    $(this).prop('selected', true);
                }
            });
        }

        if (golongan_darahDefault) {
            $('#golongan_darah_dropdown option').each(function() {
                if ($(this).val() === golongan_darahDefault) {  
                    $(this).prop('selected', true);
                }
            });
        }

        if (pekerjaanDefault) {
            $('#pekerjaan_dropdown option').each(function() {
                if ($(this).val() === pekerjaanDefault) {
                    $(this).prop('selected', true);
                }
            });
        }

        if (vaksin_covid19Default) {
            $('#vaksin_covid19_dropdown option').each(function() {
                if ($(this).val() === vaksin_covid19Default) {
                    $(this).prop('selected', true);
                }
            });
        }
    });

    $('#sudah_umroh').change(function() {
        toggleTanggalUmrohField();
    });

    $('#sudah_menikah').change(function() {
        toggleNamaPasanganField();
    });

    $('#toggle_tambah').click(function() {
        $('#tambah_jamaah').prop('hidden', false).toggle(); 
        $('#pilih_jamaah').hide();
    });

    $('#toggle_pilih').click(function() {
        $('#pilih_jamaah').prop('hidden', false).toggle(); 
        $('#tambah_jamaah').hide(); 
    });

    $("#tambah_jamaah_table").on('click', function(e){
        e.preventDefault();
        
        // Validation
        var nama = $("input[name=nama_jamaah]").val();
        var jenis_kelamin = $("input[name=jenis_kelamin_jamaah]").val();
        var tgl_lahir = $("input[name=tgl_lahir_jamaah]").val();
        var jenis_kelamin = $("input[name=jenis_kelamin_jamaah]").val();
            if (jenis_kelamin == 'l') {
                var jenis_kelamin_str = 'Laki-laki'
            } else {
                var jenis_kelamin_str = 'Perempuan'
            }
        var b_email = $("#b_email").val();
        var b_telepon = $("#b_telepon").val();
        var b_is_menikah = $("#b_is_menikah").val();
        var b_tgl_lahir = $("#b_tgl_lahir").val();
        var b_alamat = $("#b_alamat").val();
        var b_paspor = $("#b_paspor").val();
        var b_masa_paspor = $("#b_masa_paspor").val();
        var b_riwayat_penyakit = $("#b_riwayat_penyakit").val();
        var b_golongan_darah = $("#b_golongan_darah").val();
        var b_pendidikan = $("#b_pendidikan").val();
        
        if (nama === "" || tgl_lahir === "" || b_email === "" || b_telepon === "" || b_tgl_lahir === "" || b_alamat === "" || b_paspor === "") {
            alert('data tidak lengkap');
        } else {
            var csrf_token = $("input[name='csrf_token']").val();
            var data_jamaah_baru = {
                'b_email': b_email,
                'b_telepon': b_telepon,
                'b_is_menikah': b_is_menikah,
                'b_tgl_lahir': b_tgl_lahir,
                'b_alamat': b_alamat,
                'b_paspor': b_paspor,
                'b_masa_paspor': b_masa_paspor,
                'b_riwayat_penyakit': b_riwayat_penyakit,
                'b_golongan_darah': b_golongan_darah,
                'b_pendidikan': b_pendidikan,

                'nama': nama,
                'jenis_kelamin': jenis_kelamin,
                'tgl_lahir': tgl_lahir,
                'csrf_token': csrf_token
            }

            $.ajax({
                url: "/tambah_jamaah_baru",
                type: "POST",
                data: data_jamaah_baru,
                dataType: "json",
                success: function (data) {
                    console.log("Rekaman baru dibuat dengan ID:", data);
                    alert('Jamaah baru berhasil ditambahkan');
                    var identitas_id = data.identitas_id;
                    $("#dt_jamaah").append('<tr><td hidden="1">'+identitas_id+'</td><td>'+nama+'</td><td>'+jenis_kelamin_str+'</td><td>'+tgl_lahir+'</td><td>'+b_paspor+'</td><td class="static"><span class="btn btn-outline-danger dlt_jamaah"><i class="fa fa-trash"></i></span></td></tr>'); 
                    removeRow();
                    $("input[name=nama_jamaah], input[name=jenis_kelamin_jamaah], input[name=tgl_lahir_jamaah]").val("");
                    $("#b_email").val("");
                    $("#b_telepon").val("");
                    $("#b_tgl_lahir").val("");
                    $("#b_alamat").val("");
                    $("#b_paspor").val("");
                    $("#b_masa_paspor").val("");
                    $("#b_riwayat_penyakit").val("");
                    updateTotalCount();
                },
                error: function (xhr, status, error) {
                    console.error("Kesalahan dalam panggilan AJAX:", error);
                    alert('Kesalahan: ' + error);
                }
            });
        }
    });

    var existingIds = {};
    $('#dt_jamaah tr').each(function() {
        var id = $(this).find('td:first').text().trim();
        existingIds[id] = true;
    });

    $("#dftr_jamaah_umroh").on('change', function() {
        var selectedJamaah = $(this).val();
        if (selectedJamaah) {
            var data_select_jamaah = $(this).find('option:selected');
            var id = data_select_jamaah.data('id');
            var nama = data_select_jamaah.data('nama');
            var jenis_kelamin = data_select_jamaah.data('jenis-kelamin');
            if (jenis_kelamin == 'l') {
                jenis_kelamin = 'Laki-laki'
            } else {
                jenis_kelamin = 'Perempuan'
            }
            var tgl_lahir = data_select_jamaah.data('tgl-lahir');
            var paspor = data_select_jamaah.data('paspor');

           // Periksa apakah ID sudah ada dalam objek existingIds
            if (existingIds[id]) {
                alert('Jamaah dengan ID yang sama sudah terdaftar.');
            } else {
                // Tambahkan ID ke objek existingIds
                existingIds[id] = true;

                // Tambahkan baris baru ke dalam tabel
                $("#dt_jamaah").append('<tr><td hidden="1">'+id+'</td><td>'+nama+'</td><td>'+jenis_kelamin+'</td><td>'+tgl_lahir+'</td><td>'+paspor+'</td><td class="static"><span class="btn btn-outline-danger dlt_jamaah"><i class="fa fa-trash"></i></span></td></tr>');
                
                // Panggil fungsi untuk menghapus baris
                removeRow();

                // Kosongkan nilai terpilih dari dropdown
                $(this).val("");

                // Panggil fungsi untuk memperbarui jumlah total
                updateTotalCount();
            }
        }
    });

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
        var radio_dftr =  $("input[name='radio_dftr']:checked").val();
        var data_login_id =  $("input[name='data_login_id']").val();
        var sesi = $("#sesi_umroh").val();
        var csrf_token = $("input[name='csrf_token']").val();
        

        // console.log('data_pendaftaran : ', radio_dftr);
        if (radio_dftr == 'sendiri') {
            
            var jamaah = $("#jamaah_umroh").val();
            var s_nama = $("#s_nama").val();
            var s_jenis_kelamin = $("#s_jenis_kelamin").val();
            var s_email = $("#s_email").val();
            var s_telepon = $("#s_telepon").val();
            var s_is_menikah = $("#s_is_menikah").val();
            var s_pendidikan = $("#s_pendidikan").val();
            var s_paspor = $("#s_paspor").val();
            var s_masa_paspor = $("#s_masa_paspor").val();
            var s_riwayat_penyakit = $("#s_riwayat_penyakit").val();
            var s_alamat = $("#s_alamat").val();
            var s_golongan_darah = $("#s_golongan_darah").val();


            if (!sesi) {
                alert('Pilih paket terlebih dahulu');
            } else if (s_nama === '' || s_email === '' || s_telepon === '' || s_alamat === '' || s_paspor === '' || s_masa_paspor === '') {
                alert('Mohon lengkapi data');
            } else {
                var data_pendaftaran = {
                    's_nama': s_nama,
                    's_jenis_kelamin': s_jenis_kelamin,
                    's_email': s_email,
                    's_telepon': s_telepon,
                    's_is_menikah': s_is_menikah,
                    's_pendidikan': s_pendidikan,
                    's_paspor': s_paspor,
                    's_masa_paspor': s_masa_paspor,
                    's_riwayat_penyakit': s_riwayat_penyakit,
                    's_alamat': s_alamat,
                    's_golongan_darah': s_golongan_darah,

                    'jamaah_id': parseInt(jamaah),
                    'sesi_id': parseInt(sesi),
                    'csrf_token': csrf_token
                };

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
            }

        } else {
            var get_id_jamaah = [];
            $("#tabel_jamaah tbody tr").each(function () {
                var jamaah_id_tabel = $(this).find("td:first").text().trim();
                var jamaah_data = {
                    'id': jamaah_id_tabel,
                };
                get_id_jamaah.push(jamaah_data);
            });
            var data_pendaftaran_banyak = {
                'data_login_id': data_login_id,
                'jamaah_id': get_id_jamaah,
                'sesi_id': parseInt(sesi),
                'csrf_token': csrf_token
            };
            console.log('Data Jamaah:', data_pendaftaran_banyak);

            $.ajax({
                url: "/buat_pendaftaran_banyak",
                type: "POST",
                data: data_pendaftaran_banyak,
                dataType: "json",
                success: function (res) {
                    console.log("Pendaftaran banyak berhasil:", res);
                    // alert('Data berhasil disimpan');
                    window.location.href = "/pendaftaran_berhasil";
                },
                error: function (xhr, status, error) {
                    console.error("Kesalahan dalam panggilan AJAX:", error);
                    alert('Kesalahan: ' + error);
                }
            });
        }
    
    }); 
    
    $(document).on('click', "#submit_pendaftaran_sesi", function () {
        var jamaah = $("#jamaah_umroh").val();
        var sesi = $("#sesi_umroh_sesi").val();
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