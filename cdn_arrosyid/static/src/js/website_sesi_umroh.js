odoo.define('cdn_arrosyid.website_sesi_umroh', function (require) {
    'use strict';
    
    var ajax = require('web.ajax');
    var core = require('web.core');
    var _t = core._t;
    var rpc = require('web.rpc');
    var QWeb = core.qweb;

    $(document).on('click', "#submit_button_sesi_umroh", function () {
        var sesiName = $(this).closest('tr').find('td:first').text().trim();
        sessionStorage.setItem('chosenSesiName', sesiName);
        window.location.href = '/pendaftaran';
    });

    $(document).on('click', "#action_ketentuan_umroh", function () {
        window.location.href = '/ketentuan';
    });

    $(document).on('click', "#action_contactus", function () {
        window.location.href = '/contactus';
    });

});
