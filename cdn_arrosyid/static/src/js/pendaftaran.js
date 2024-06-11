odoo.define('cdn_arrosyid.pendafatran', function (require) {
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
   
})