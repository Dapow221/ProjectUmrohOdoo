odoo.define('cdn_arrosiyd.peta', function (require) {
    'use strict';

    var Widget = require('web.Widget');

    var PetaWidget = Widget.extend({
        template: 'peta',

        start: function () {
            this._super.apply(this, arguments);
            this.renderMap();
        },

        renderMap: function () {
            // Kode untuk membuat peta Leaflet
            var map = L.map('map').setView([51.505, -0.09], 13);
            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: '© OpenStreetMap contributors'
            }).addTo(map);
        },
    });

    return PetaWidget;
});