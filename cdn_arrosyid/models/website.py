from odoo import fields, models, api, _


class WebsiteInherit(models.Model):
    _inherit = 'website'
    
    custom_field = fields.Char(string='Custom Field')
    
