import json

from odoo import http
from odoo.http import request
from odoo.tests import Form

class ProfilController(http.Controller):
    @http.route('/my/home', type='http', auth='public', website=True)
    def get_data(self):
        user_id = request.env.user.partner_id.id
        data_sesi_umroh = request.env['cdn.sesi.umroh'].sudo().search([])
        data_pendaftaran = request.env['cdn.pendaftaran'].sudo().search([])
        data_jamaah_umroh = request.env['cdn.pendaftaran'].sudo().search(['|', ('partner_id', '=', user_id), ('pendaftar_id', '=', user_id)])
        data_tagihan = request.env['account.move'].sudo().search([('partner_id', '=', user_id),('state', '=', 'posted')])

        return request.render('cdn_arrosyid.profil', {
            'data_sesi': data_sesi_umroh,
            'data_pendaftaran': data_pendaftaran,
            'data_tagihan': data_tagihan,
            'data_jamaah_umroh': data_jamaah_umroh
        })

    @http.route('/buat_pembayaran', csrf=True, type="http", methods=['POST'], auth="public", website=True)
    def buat_pembayaran(self, **post):
        try:
            print('print', post)

            metode_bayar = post.get('metode_bayar')
            jml_pembayaran = post.get('jml_pembayaran')
            tagihan_id = post.get('tagihan_id')
            dt_partner_id = post.get('dt_partner_id')
            tgl_pembayaran = post.get('tgl_pembayaran')
            csrf_token = post.get('csrf_token')
            
            # Buat pembayaran baru

            invoice = request.env['account.move'].sudo().browse(int(tagihan_id))
           
            print(f"tagihan_id: {tagihan_id}, type: {type(tagihan_id)}")
            print(f"invoice.journal_id.id: {invoice.journal_id.id}")
            # payment = request.env['account.payment'].sudo().create({
            #     'amount': int(jml_pembayaran),
            #     'partner_id': int(dt_partner_id),
            #     'date': tgl_pembayaran,
            #     # 'payment_type': 'inbound',
            #     # 'move_id': invoice.id,
            #     # 'journal_id': invoice.journal_id.id,
            # })
            # payment.action_post()
            action_data = invoice.action_register_payment()
            # invoice.payment_by_id = action_data['context']['default_journal_id'] = request.env.user.company_id.journal_tunai.id
            wizard = Form(request.env['account.payment.register'].sudo().with_context(action_data['context'])).save()
            action = wizard.action_create_payments()
            # invoice.write({'payment_state': 'paid'})
            # success_invoice_payment.append(invoice)
            # Kembalikan respons JSON
            return json.dumps({'result': True})
        except Exception as e:
            # Tangani kesalahan dan kembalikan pesan kesalahan
            return json.dumps({'result': False, 'error': str(e)})

