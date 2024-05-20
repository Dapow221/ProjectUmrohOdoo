from odoo import models, fields, api

class SesiUmroh(models.Model):
    _name = 'cdn.sesi.umroh'
    _description = 'Sesi Umroh'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
    paket_umroh_id = fields.Many2one(comodel_name='cdn.paket.umroh', string='Paket Umroh')
    pembimbing_id = fields.Many2one(comodel_name='res.users', string='Pembimbing')
    petugas_lapangan = fields.Many2many(comodel_name='res.users', string='Petugas Lapangan')
    jammaah_ids = fields.Many2many(comodel_name='res.partner', string='Jamaah')
    jumlah_jamaah = fields.Integer(string='Jumlah Jamaah')
    state = fields.Selection(string='Status', selection=[('akan_datang', 'Akan Datang'),('prosess', 'Sedang Berjalan'),('selesai', 'Selesai'),('batal_perjalanan', 'Perjalanan Batal')], default='akan_datang',required=True)
    rencana_perjalanan_ids = fields.One2many('cdn.rencana.perjalanan', 'sesi_umroh_id', string='rencana_perjalanan')

    def write(self, values):
        res = super(SesiUmroh, self).write(values)
        if 'state' in values:
            for rec in self.rencana_perjalanan_ids:
                rec._compute_state()
        return res
        
    def action_akan_datang(self):
        for rec in self:
            rec.state = 'akan_datang'
    
    def action_selesai(self):
        for rec in self:
            rec.state = 'selesai'
    
    def action_prosess(self):
        for rec in self:
            if rec.state == 'akan_datang':
                rec.state = 'prosess'
    
    def action_batal_perjalanan(self):
        for rec in self:
            rec.state = 'batal_perjalanan'

    
    

    
