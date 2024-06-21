odoo.define('cdn_arrosyid.custom', function (require) {
    'use strict';

    var core = require('web.core');
    var rpc = require('web.rpc');
    var ajax = require('web.ajax');

    // Redirect dari /my ke /my/home
    if (window.location.pathname === '/my') {
        window.location.href = '/my/home';
    }

    // if (window.location.pathname !== '/my') {
    //     $('#myTabContent').append(`
    //         <div class="tab-pane fade show active" id="identitas" role="tabpanel">
    //             <div class="card user-card-full shadow">
    //                 <div class="row m-l-0 m-r-0">                     
    //                     <div class="col-sm-12"> <!-- Fixed: Changed col-sm-16 to col-sm-12 -->
    //                         <div class="card-block" style="padding: 20px">
    //                             <h6 class="m-b-20 p-b-5 b-b-default f-w-600">INFORMASI JAMAAH</h6>
    //                             <t t-if="data_identitas_jamaah.image">
    //                                 <img t-attf-src="data:image;base64,{{data_identitas_jamaah.image}}" alt="avatar" class="rounded-circle img-fluid" style="width:150px;" />
    //                             </t>
    //                             <t t-else="">
    //                                 <img src="https://img.icons8.com/bubbles/100/000000/user.png" class="img-radius" alt="User-Profile-Image"/>
    //                             </t>
    //                             <h4><t t-esc="data_identitas_jamaah.referensi"/></h4>
    //                             <div class="row">
    //                                 <div class="col-sm-6">
    //                                     <p class="m-b-10 f-w-600">
    //                                         Nama : <b> <t t-esc="data_identitas_jamaah.name"/> </b>
    //                                     </p>
    //                                     <p class="m-b-10 f-w-600">
    //                                         Email : <b> <t t-esc="data_identitas_jamaah.email"/> </b>
    //                                     </p>
    //                                     <p class="m-b-10 f-w-600">
    //                                         Tanggal Lahir : <b> <t t-esc="data_identitas_jamaah.tgl_lahir"/> </b>
    //                                     </p>
    //                                     <p class="m-b-10 f-w-600">
    //                                         Umur : <b> <t t-esc="data_identitas_jamaah.umur"/> Tahun</b>
    //                                     </p>
    //                                     <p class="m-b-10 f-w-600">
    //                                         Jenis Kelamin : <b>
    //                                             <t t-if="data_identitas_jamaah.jenis_kel == 'l'">
    //                                                 Laki-laki
    //                                             </t>
    //                                             <t t-elif="data_identitas_jamaah.jenis_kel == 'p'">
    //                                                 Perempuan
    //                                             </t>
    //                                             <t t-else="">
    //                                                 <t t-esc="data_identitas_jamaah.jenis_kel"/>
    //                                             </t>
    //                                         </b>
    //                                     </p>
    //                                     <p class="m-b-10 f-w-600">
    //                                         No. Paspor : <b> <t t-esc="data_identitas_jamaah.paspor"/> </b>
    //                                     </p>
    //                                     <p class="m-b-10 f-w-600">
    //                                         Masa Berlaku Paspor : <b> <t t-esc="data_identitas_jamaah.masa_paspor"/> </b>
    //                                     </p>
    //                                     <p class="m-b-10 f-w-600">
    //                                         <b>
    //                                         <t t-set="pekerjaans">
    //                                             <t t-raw="{
    //                                                 'pns': 'PNS',
    //                                                 'irt': 'Ibu Rumah Tangga',
    //                                                 'tni': 'TNI',
    //                                                 'dagang': 'Pedagang',
    //                                                 'tani': 'Petani',
    //                                                 'swasta': 'Swasta',
    //                                                 'pelajar': 'Pelajar',
    //                                                 'bumn': 'BUMN',
    //                                             }.get(data_identitas_jamaah.pekerjaan, '')"/>
    //                                         </t>
    //                                         <t t-esc="pekerjaans"/>
    //                                         </b>
    //                                     </p>
    //                                     <p class="m-b-10 f-w-600">Pernah Umroh :
    //                                         <t t-if="data_identitas_jamaah.is_umroh">
    //                                             <input type="checkbox" checked="checked" disabled="disabled"/>
    //                                         </t>
    //                                         <t t-else="">
    //                                             <input type="checkbox" disabled="disabled"/>
    //                                         </t>
    //                                     </p>
    //                                     <p class="m-b-10 f-w-600">Status Nikah :
    //                                         <t t-if="data_identitas_jamaah.is_menikah">
    //                                             <input type="checkbox" checked="checked" disabled="disabled"/>
    //                                         </t>
    //                                         <t t-else="">
    //                                             <input type="checkbox" disabled="disabled"/>
    //                                         </t>
    //                                     </p>
    //                                     <p class="m-b-10 f-w-600">
    //                                         Nama Pasangan : <b> <t t-esc="data_identitas_jamaah.nama_pasangan"/> </b>
    //                                     </p>
    //                                 </div>
    //                                 <div class="col-sm-6" style="border-left: 1px solid #ccc;">
    //                                     <p class="m-b-10 f-w-600">
    //                                         No. Hp : <b> <t t-esc="data_identitas_jamaah.mobile"/> </b>
    //                                     </p>
    //                                     <p class="m-b-10 f-w-600">
    //                                         Alamat : <b> <t t-esc="data_identitas_jamaah.street"/> </b>
    //                                     </p>
    //                                     <p class="m-b-10 f-w-600">
    //                                         Pendidikan : <b>
    //                                         <t t-set="pendidikans">
    //                                             <t t-raw="{
    //                                                 'sd': 'SD',
    //                                                 'smp': 'SMP',
    //                                                 'sma': 'SMA',
    //                                                 'kuliah': 'Perguruan Tinggi'
    //                                             }.get(data_identitas_jamaah.pendidikan, '')"/>
    //                                         </t>
    //                                         <t t-esc="pendidikans"/>
    //                                         </b>
    //                                     </p>
    //                                     <p class="m-b-10 f-w-600">
    //                                         Riwayat Penyakit : <b> <t t-esc="data_identitas_jamaah.riwayat_penyakit"/> </b>
    //                                     </p>
    //                                     <p class="m-b-10 f-w-600">Vaksin Meningitis :
    //                                         <t t-if="data_identitas_jamaah.vaksin_meningitis">
    //                                             <input type="checkbox" checked="checked" disabled="disabled"/>
    //                                         </t>
    //                                         <t t-else="">
    //                                             <input type="checkbox" disabled="disabled"/>
    //                                         </t>
    //                                     </p>
    //                                     <p class="m-b-10 f-w-600">
    //                                         Vaksin Covid19:
    //                                         <b> 
    //                                             <t t-set="vaksins">
    //                                                 <t t-raw="{
    //                                                 'belum': 'Belum Vaksin',
    //                                                 'vaksin1': 'Vaksinasi Pertama',
    //                                                 'vaksin2': 'Vaksinasi Kedua',
    //                                                 'booster': 'Vaksin Booster'
    //                                                 }.get(data_identitas_jamaah.vaksin_covid19, '')"/>
    //                                             </t>
    //                                             <t t-esc="vaksins"/>
    //                                         </b>
    //                                     </p>
    //                                     <p class="m-b-10 f-w-600">
    //                                         Golongan Darah : <b>
    //                                             <t t-if="data_identitas_jamaah.golongan_darah == 'oplus'">O+</t>
    //                                             <t t-elif="data_identitas_jamaah.golongan_darah == 'ominus'">O-</t>
    //                                             <t t-elif="data_identitas_jamaah.golongan_darah == 'aplus'">A+</t>
    //                                             <t t-elif="data_identitas_jamaah.golongan_darah == 'aminus'">A-</t>
    //                                             <t t-elif="data_identitas_jamaah.golongan_darah == 'bplus'">B+</t>
    //                                             <t t-elif="data_identitas_jamaah.golongan_darah == 'bminus'">B-</t>
    //                                             <t t-elif="data_identitas_jamaah.golongan_darah == 'abplus'">AB+</t>
    //                                             <t t-elif="data_identitas_jamaah.golongan_darah == 'abminus'">AB-</t>
    //                                             <t t-else=""><t t-esc="data_identitas_jamaah.golongan_darah"/></t>
    //                                         </b>
    //                                     </p>
    //                                 </div>
    //                             </div>                                 
    //                         </div>
    //                     </div>
    //                 </div>
    //             </div>
    //         </div>
    //     `);
    // };
    

    $('div.container.mb64').removeClass('container').addClass('container-fluid');
    $('div[class="col-12 col-md col-lg-6"]').removeClass('col-lg-6').addClass('col-lg-9');

	$(document).ready(function() {
        $(document).on('click', '.btn_detail_tagihan', function() {
            var dt_id = $(this).data('dt_tagihan_id');
            var nm_user = $(this).data('dt_nm_user');
            console.log('Tagihan ID:', dt_id);

            $('#detailTagihanModal').remove();
    
            rpc.query({
                model: 'account.move',
                method: 'search_read',
                args: [[['id', '=', dt_id]]],
                kwargs: {
                    fields: ['id', 'name', 'payment_state', 'amount_total', 'amount_residual', 'invoice_line_ids'],
                },
            }).then(function(data) {

                // console.log('Data Tagihan:', data);    
                var invoiceLineIds = data[0].invoice_line_ids;

                var statusPembayaran = '';
                if (data[0].payment_state === 'not_paid') {
                    statusPembayaran = 'Belum Lunas';
                } else if (data[0].payment_state === 'partial') {
                    statusPembayaran = 'Sebagian Lunas';
                } else {
                    statusPembayaran = 'Lunas';
                }
    
                rpc.query({
                    model: 'account.move.line',
                    method: 'search_read',
                    args: [[['id', 'in', invoiceLineIds]]],
                    kwargs: {
                        fields: ['id', 'name', 'quantity', 'price_unit', 'tax_ids'],
                    },
                }).then(function(productData) {

                    // console.log('Data Produk:', productData);    
                    var productsTable = `
                        <table class="table">
                            <thead>
                                <tr>
                                    <th>Nama Produk</th>
                                    <th>jumlah</th>
                                    <th>Harga Satuan (Rp)</th>
                                    <th>Total (Rp)</th>
                                </tr>
                            </thead>
                            <tbody>
                    `;
                    productData.forEach(function(product) {
                        var total = product.quantity * product.price_unit;
                        productsTable += `
                            <tr>
                                <td>${product.name}</td>
                                <td>${product.quantity}</td>
                                <td>${product.price_unit.toLocaleString()}</td>
                                <td>${total.toLocaleString()}</td>
                            </tr>
                        `;
                    });
                    productsTable += `
                            </tbody>
                        </table>
                    `;
    
                    var modalContent = `
                        <div class="modal fade" id="detailTagihanModal" tabindex="-1" aria-labelledby="detailTagihanModalLabel" aria-hidden="true">
                            <div class="modal-dialog modal-lg">
                                <div class="modal-content">
                                    <div class="modal-header">
                                        <h5 class="modal-title" id="detailTagihanModalLabel">Detail Tagihan ${data[0].name}</h5>
                                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                    </div>
                                    <div class="modal-body">
                                        <!-- <p><strong>ID:</strong> ${data[0].id}</p> -->
                                        <p><strong>Nama:</strong> ${nm_user}</p>
                                        <p><strong>Status:</strong> ${statusPembayaran}</p>
                                        <p><strong>Jumlah Tagihan:</strong> Rp ${data[0].amount_total.toLocaleString()}</p>
                                        <p><strong>Sisa Tagihan:</strong> Rp ${data[0].amount_residual.toLocaleString()}</p>
                                        <hr>
                                        <h6>Produk dalam Tagihan:</h6>
                                        ${productsTable}
                                    </div>
                                    <div class="modal-footer">
                                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Tutup</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    `;
    
                    // Menambahkan modal ke dalam body
                    $('body').append(modalContent);
    
                    // Menampilkan modal
                    $('#detailTagihanModal').modal('show');
                }).catch(function(error) {
                    console.error("Error saat memuat produk:", error);
                });
    
            }).catch(function(error) {
                console.error("Error saat memuat data tagihan:", error);
            });
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
        // console.log('data : ', data_pembayaran);

        $('#btn_submit_pembayaran').addClass('btn-disabled').prop('disabled', true);
        $('#loading_pembayaran').show();

        $.ajax({
            url: "/buat_pembayaran",
            type: "POST",
            data: data_pembayaran,
            dataType: "json",
            success: function (data) {
                console.log("Rekaman baru dibuat dengan ID:", data);
                alert('Pembayaran berhasil');
                $("#metode_bayar").val('');
                $("#jml_pembayaran").val('');
                $("#tgl_pembayaran").val('');    
                $('#crt_payment').modal('hide');
                location.reload();
                $('a[data-bs-toggle="tab"][href="#tagihan"]').tab('show');
            },
            error: function (xhr, status, error) {
                console.error("Kesalahan dalam panggilan AJAX:", error);
                alert('Kesalahan: ' + error);
            },
            complete: function() {
                $('#btn_submit_pembayaran').removeClass('btn-disabled').prop('disabled', false);
                $('#loading_pembayaran').hide();
            }
        });

    });
})