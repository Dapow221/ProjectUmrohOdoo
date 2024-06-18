/** @odoo-module **/

import {Component, useState, onWillStart} from "@odoo/owl"
import {useService} from "@web/core/utils/hooks"
import {standardViewProps} from "@web/views/standard_view_props"
import {LeafletMapRenderer} from"./lmap_renderer"
import {Layout} from "@web/search/layout"
import {LeafletMapModel} from "./lmap_model"

export class LeafletMapController extends Component {
    static template = 'cdn_arrosyid.MapView'
    static components = {LeafletMapRenderer, Layout}
    static props = {
        ...standardViewProps,
    }

    setup() {
        console.log(this);
        this.orm = useService("orm")
        this.model = useState(new LeafletMapModel(
            {orm: this.orm },
            this.props.resModel,
        ))

        onWillStart(async ()=>{
            await this.model.load()
        })
    }
}