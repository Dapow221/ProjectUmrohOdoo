# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from datetime import datetime
from odoo.exceptions import ValidationError

import os
import xlsxwriter
import base64

class WizardLaporanBulanan(models.Model):
    _name = 'wizard.laporan.bulanan'
    _description = 'wizard.laporan.bulanan'

    start_date = fields.Date(string='Tanggal dimulai')
    end_date = fields.Date(string='Tanggal berakhir')
    jamaah_id = fields.Many2one('cdn.identitas.jamaah', string='jamaah')

    file_export             = fields.Binary(string='File Export')
    file_export_name        = fields.Char(string='File Export Name')

    def action_cetak_laporan(self):
        if self.start_date >= self.end_date: 
            raise ValidationError(_('Tanggal tidak sesuai!'))
        else:
            if self.jamaah_id:
                pembayaran          = self.env['account.move'].search([('date', '>=', self.start_date), ('date', '<=', self.end_date),('partner_id', '=', self.jamaah_id.partner_id.id)])
            else:
                pembayaran          = self.env['account.move'].search([('date', '>=', self.start_date), ('date', '<=', self.end_date),])
            names = ', '.join(set(payment.partner_id.name for payment in pembayaran if payment.partner_id))
            
            path_module         = os.path.dirname(os.path.realpath(__file__))
            file_name           = path_module + '\\temp.xlsx'
            workbook            = xlsxwriter.Workbook(file_name, {'in_memory': True})
            worksheet           = workbook.add_worksheet()

            cell_format         = workbook.add_format()
            cell_format.set_align('center')
            cell_format.set_font_size(12)
            cell_format.set_border(1)

            head_format         = workbook.add_format()
            head_format.set_align('center')
            head_format.set_font_size(12)
            head_format.set_bold()
            head_format.set_bg_color('yellow')
            head_format.set_border(1)

            head2_format         = workbook.add_format()
            head2_format.set_font_size(10)
            head2_format.set_bold()

            title_format         = workbook.add_format()
            title_format.set_align('center')
            title_format.set_bold()
            title_format.set_font_size(15)

            worksheet.merge_range('A1:E1', 'Laporan Pembayaran', title_format)
            worksheet.set_column('A:A', 15)
            worksheet.set_column('B:B', 20)
            worksheet.set_column('C:C', 30)
            worksheet.set_column('D:D', 30)
            worksheet.set_column('E:E', 30)

            worksheet.merge_range('A2:E2', '')
            worksheet.merge_range('A3:E3', f'Rentang Waktu : {self.start_date} s/d {self.end_date}', head2_format)
            worksheet.merge_range('A4:E4', f'Nama: {names}', head2_format)
            worksheet.merge_range('A5:E5', '')

            worksheet.write('A6', 'No', head_format)
            worksheet.write('B6', 'Nama', head_format)
            worksheet.write('C6', 'Tanggal Mulai', head_format)
            worksheet.write('D6', 'Tanggal Berakhir', head_format)
            worksheet.write('E6', 'Total Pembayaran', head_format)

            row = 6  # Mulai dari baris ke-6
            for index, dt_pembayaran in enumerate(pembayaran, start=1):
                date_format = "%d-%m-%Y"
                if dt_pembayaran.invoice_date == False:
                    invoice_date = ''
                else: 
                    invoice_date =  dt_pembayaran.invoice_date.strftime(date_format)
                invoice_date_due =  dt_pembayaran.invoice_date_due.strftime(date_format)            
                worksheet.write(row, 0, index, cell_format)
                worksheet.write(row, 1, dt_pembayaran.partner_id.name, cell_format)
                worksheet.write(row, 2, invoice_date, cell_format) 
                worksheet.write(row, 3, invoice_date_due, cell_format) 
                worksheet.write(row, 4, dt_pembayaran.amount_total, cell_format)
                row += 1

            worksheet.freeze_panes(6, 5)
            workbook.close()

            with open(file_name, 'rb') as file:
                file_base64 = base64.b64encode(file.read())

            self.file_export_name   = 'Lapoan_Pembayaran_{}_{}.xlsx'.format(
                self.id, 
                self.start_date.strftime('%Y-%m-%d'),
                self.end_date.strftime('%Y-%m-%d')
            )

            self.write({'file_export': file_base64})

            if os.path.exists(file_name):
                os.remove(file_name)
            
            return {
                'type'      : 'ir.actions.act_url',
                'target'    : 'self',
                'url'       : '/web/binary/download_document?model={}&field=file_export&id={}&file_name={}'.format(
                    self._name,
                    self.id, 
                    self.file_export_name
                )
            }
        