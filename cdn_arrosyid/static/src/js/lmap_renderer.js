/** @odoo-module **/

import { Component, onWillStart, useRef, onMounted } from "@odoo/owl";
import {loadCSS, loadJS} from "@web/core/assets"
import {useService} from "@web/core/utils/hooks"

export class LeafletMapRenderer extends Component {
    static template = 'cdn_arrosyid.MapRenderer';
    static props = {
        model: Object,
    }

    setup(){
        this.root = useRef('map')
        this.action = useService('action')

        onWillStart(async ()=>{
            await loadCSS ("https://unpkg.com/leaflet@1.7.1/dist/leaflet.css");
            await loadJS("https://unpkg.com/leaflet@1.7.1/dist/leaflet.js");
        })

        onMounted (() =>{
            this.map = L.map(this.root.el).setView([51.505, -0.09], 2);

            L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
                maxZoom: 19,
                attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
            }).addTo(this.map);

            this.props.model.records.forEach(record =>{
                this.createMarker(record)
            })

            this.map.on('popupopen', ()=>{
                this.openResPartner()
            })
        })
    }

    createMarker(record){
        const marker = L.marker([record.latitude, record.longitude]).addTo(this.map);
        marker.bindPopup(`<h3>${record.translated_display_name}</hr><br></br><button id='leafletMapPopupOpenBtn' data-res-id='${record.id}' class='btn btn-primary'>Open</button>`);
    }

    openResPartner(){
        const buttons = document.querySelectorAll("#leafletMapPopupOpenBtn")
        buttons.forEach(button=>{
            button.addEventListener('click', ()=>{
                console.log("open button was clicked------------------------------");
                this.action.switchView("form", {resId: parseInt(button.dataset.resId)})
            })
        })
    }
}