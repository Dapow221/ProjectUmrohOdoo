/** @odoo-module **/

export class LeafletMapModel {
    constructor(services, resModel){
        this.orm = services.orm
        this.resModel = resModel
    }

    async load() {
        const data = await this.orm.searchRead(this.resModel, [], ["translated_display_name","latitude","longitude"])

        this.records = data
    }
} 