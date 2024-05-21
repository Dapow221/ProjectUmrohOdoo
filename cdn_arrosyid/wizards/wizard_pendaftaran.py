from odoo import models, fields, api, _

class WizardPendaftaran(models.TransientModel):
    _name = 'wizard.pendaftaran'
    _description = 'Wizard Pembayaran / invoicing'

    paket_umroh_id = fields.Many2one('cdn.paket.umroh', string='paket')
    jamaah_ids = fields.Many2many('res.partner', string='jamaah')

    def action_pendaftaran(self):
        get_paket = self.paket_umroh_id.id
        sesi = []
        for get_sesi in self:
            sesi.append(get_sesi.paket_umroh_id.sesi_umroh)
            tes = get_sesi.paket_umroh_id.sesi_umroh.description

        print("************************", tes)