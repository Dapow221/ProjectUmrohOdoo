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
        data_tagihan = request.env['account.move'].sudo().search([('partner_id', '=', user_id),('state', '=', 'posted')])
        data_identitas_jamaah = request.env['cdn.identitas.jamaah'].sudo().search([('partner_id', '=', user_id)])
        
        return request.render('cdn_arrosyid.profil', {
            'data_sesi': data_sesi_umroh,
            'data_pendaftaran': data_pendaftaran,
            'data_tagihan': data_tagihan,
            'data_identitas_jamaah': data_identitas_jamaah,
        })

    @http.route('/buat_pembayaran', csrf=True, type="http", methods=['POST'], auth="public", website=True)
    def buat_pembayaran(self, **post):
        try:
            print('print', post)

            metode_bayar = post.get('metode_bayar')
            jml_pembayaran = post.get('jml_pembayaran')
            tagihan_id = post.get('tagihan_id')
            tgl_pembayaran = post.get('tgl_pembayaran')
            # dt_partner_id = post.get('dt_partner_id')
            # csrf_token = post.get('csrf_token')
            
            # Buat pembayaran baru    
            invoice = request.env['account.move'].sudo().browse(int(tagihan_id))
            btn_reg_patment = invoice.action_register_payment()
            pembayaran = Form(request.env['account.payment.register'].sudo().with_context(btn_reg_patment['context'])).save()
            pembayaran.write({
                'amount': float(jml_pembayaran),
                'journal_id': int(metode_bayar),
                'payment_date': tgl_pembayaran,
                # 'partner_id': dt_partner_id
            })
            pembayaran.action_create_payments()
            return json.dumps({'result': True})
            
        except Exception as e:
            # Tangani kesalahan dan kembalikan pesan kesalahan
            return json.dumps({'result': False, 'error': str(e)})

