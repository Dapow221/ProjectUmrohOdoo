from odoo import models, api

class WebsiteMenu(models.Model):
    _inherit = 'website.menu'

    @api.model
    def deactivate_contactus_menu(self):
        contactus_menu = self.env.ref('website.contactus_menu', raise_if_not_found=False)
        if contactus_menu:
            contactus_menu.sudo().write({'active': False})
