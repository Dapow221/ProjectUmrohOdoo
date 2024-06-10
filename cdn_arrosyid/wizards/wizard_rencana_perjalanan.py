from odoo import models, fields, api, _

class WizardRencanaPerjalanan(models.TransientModel):
    _name = 'wizard.rencana.perjalanan'
    _description = 'Wizard Rencana Perjalanan'

    sesi_id = fields.Many2one('cdn.sesi.umroh', string='Sesi Umroh')
    # rencana_perjalanan_ids = fields.Many2many('cdn.rencana.perjalanan', string='rencana perjalanan')

    def action_lihat_perjalanan(self):
        action = {
            'name': _('Perjalanan Umroh'),
            'type': 'ir.actions.act_window',
            'res_model': 'cdn.rencana.perjalanan',
            'view_mode': 'tree',
            'target': 'new',
            'view_id': self.env.ref('cdn_arrosyid.wizard_rencana_perjalanan_view_tree').id,
            'domain': [('sesi_umroh_id', '=', self.sesi_id.id)],
        }
        return action