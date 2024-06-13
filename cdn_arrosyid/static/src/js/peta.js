/** @odoo-module **/
import { registry } from '@web/core/registry';
// import { useState } from '@odoo/owl/hooks';

const {
    Component,
    onMounted,
    onWillUnmount,
    useRef,
    useState
} = owl;


export class Peta extends Component {
    /** @type {String} */
    static template = 'PetaHotel';

    /** @type {HTMLElement} */
    #map_container;
    #map;

    setup() {
      super.setup();
      this.state = useState({ 
        lat: this.props.record.data.lokasi_hotel || 24.47312970118572,
        lng: this.props.record.data.long_penjemputan || 39.606477722138365, 
      });
      this.#map_container = useRef('map_container');

      onMounted(this.#onMounted);
      onWillUnmount(this.#onWillUnmount);

    }

    #onMounted() {
      this.#map = L.map(this.#map_container.el, {
         center: [24.47312970118572, 39.606477722138365],
         zoom: 13
      });
      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '© OpenStreetMap contributors'
      }).addTo(this.#map);
      
      var marker;
      console.log(this.state.lat, this.state.lng);
      marker = L.marker([this.state.lat, this.state.lng]).addTo(this.#map);
      marker.setLatLng([this.state.lat, this.state.lng]);
      this.#map.on('click', (e) => {
          var lat = e.latlng.lat;
          var lng = e.latlng.lng;
          this.state.lat = lat;
          this.state.lng = lng;
          // if (marker) {
          marker.setLatLng(e.latlng);
          this.props.record.data.lokasi_hotel = this.state.lat
          this.props.record.data.long_penjemputan = this.state.lng
              // this.trigger('field-changed', { latitude: lat, longitude: lng });
          // } else {
          //     marker = L.marker(e.latlng).addTo(this.#map);
          // }
      });
      
    }

    #onWillUnmount() {
      this.#map.remove();
    }
}

// Peta.template = 'module_name.Peta';
registry.category('fields').add('peta_widget', Peta);
// core.form_widget_registry.add('peta_widget',Peta);
