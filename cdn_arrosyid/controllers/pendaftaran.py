from odoo import http
import traceback
from odoo.http import Response, request
from odoo.loglevels import ustr
import sys
import json

class pembayaran(http.Controller):
    @http.route('/pendaftaran/invoice', type='http', auth='public', website=False, methods=['POST','GET'], csrf=False, cors='*')
    def tes(self, **kwargs):
      try:
         i_param   = request.get_json_data()
         i_va      = i_param['virtual_account']
         i_amount  = i_param['amount']
         i_date    = i_param['date']
         i_kp      = i_param['kode_pengesahan']
         datarow             = {
            'is_success'    : True,
            'code'          : 200,
            'va'            : i_va,
            'amount'        : i_amount,
            'date'          : i_date,
            'kode_p'        : i_kp,
         }
         print(datarow)

      except Exception as e:
         traceback.print_exception(*sys.exc_info()) 
         datarow['is_success']   = ustr(e)
         datarow['code']         = 201
      finally:
         body = json.dumps(datarow)
         return Response(
               body, 
               status  = 200, 
               headers = [
                  ('Content-Type', 'application/json'), 
                  ('Content-Length', len(body))
               ]
         )


