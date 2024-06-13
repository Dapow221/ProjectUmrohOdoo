odoo.define('cdn_arrosyid.pendaftaran', function (require) {
    'use strict';

    var core = require('web.core');
    var Widget = require('web.Widget');
    var ajax = require('web.ajax');
    var _t = core._t;
    var rpc = require('web.rpc');
    var QWeb = core.qweb;

    $(document).on('change', "#paket_umroh", function () {
        var data = $("#paket_umroh").val();
        console.log('data :', data);
        
    });
    $(document).ready(function () {
        // Retrieve the chosen session name from sessionStorage
        const chosenSesiName = sessionStorage.getItem('chosenSesiName');
        if (chosenSesiName) {
            const sesiOptions = $('#sesi_umroh option');
            sesiOptions.each(function () {
                if ($(this).text().trim() === chosenSesiName) {
                    $(this).prop('selected', true);
                }
            });
        }

        // Handle change event on the paket_umroh select element
        $('#paket_umroh').on('change', function () {
            var data = $(this).val();
            console.log('Selected Paket Umroh:', data);
            // Add any additional logic based on selected paket_umroh
        });

        

        // Handle form submission
        // $('#submit_pendaftaran').on('click', function () {
        //     const selectedSesi = $('#sesi_umroh').val();
        //     if (!selectedSesi) {
        //         alert('Please select a session');
        //         return;
        //     }
        //     // Add further validation or form submission logic here
        //     alert('Form submitted successfully!');
        // });
    });

    
   
})