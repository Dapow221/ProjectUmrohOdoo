from odoo import models, fields

class IrUiViewInherit(models.Model):
    _inherit = 'ir.ui.view'

    type     = fields.Selection(selection_add=[('lmap', 'Leaflet Map')])
    