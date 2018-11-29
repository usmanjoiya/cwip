# -*- coding: utf-8 -*-

from flectra import models, fields, api
import re


class cwip_category(models.Model):
    _name = 'cwip.asset.category_custom'

    name = fields.Char(required=True, index=True, string="CWIP Category")

    account_cwip_id = fields.Many2one('account.account', string='CWIP Account', required=True,
                                      domain=[('internal_type', '=', 'other'), ('deprecated', '=', False)],
                                      help="Account used to acmulate CWIP.")
    journal_id = fields.Many2one('account.journal', string='Journal', required=True)


class cwip_asset_in_vender_bill(models.Model):
    # vender bill

    _inherit = 'account.invoice.line'

    cwip_asset__id = fields.Many2one('cwip.assets', string='CWIP Asset')

    account_cwip_id = fields.Many2one('account.account', string='CWIP Account',
                                      domain=[('internal_type', '=', 'other'), ('deprecated', '=', False)])

    @api.onchange('cwip_asset__id')
    def Data_from_account_invoice_line(self):
        assets_obj = self.env['cwip.assets'].search([('cwip_category_id', '=', self.cwip_asset__id.cwip_category_id.id)] ,  limit=1)
        print(self.cwip_asset__id.cwip_category_id.id)
        print(assets_obj)
        # for record in assets_obj:
        #     if assets_obj:
        # 
        #         print(record.id)
        #         invoices_obj2 = self.env['cwip.asset.category_custom'].search([('id', '=', record.id)])
        #         print(record.id)
        #         print(record.id)
        #         print(record.id)
        #         # print(invoices_obj2)
        #         # print(invoices_obj2)
        #         for record2 in invoices_obj2:
        #             if invoices_obj2:
        #                 print(record2.id)
        # #             else:
        # #                return


class cwip_assets(models.Model):
    _name = 'cwip.assets'

    name = fields.Char("CWIP Asset", required=True)

    cwip_category_id = fields.Many2one('cwip.asset.category_custom', string='CWIP Category', required=True
                                       # ,default=lambda self: self.env['cwip.asset.category_custom'].search([] , limit=1)
                                       )

    # @api.onchange('cwip_category_id')
    # def Data_from_account_invoice_line(self):
    #     abc = ['account.invoice.line']
    #     invoices_obj = self.env['account.invoice.line'].search([('cwip_asset__id', '=', self.cwip_category_id.id)])
    #     print(invoices_obj)
    #
    #     l = []
    #     for record in invoices_obj:
    #         if invoices_obj:
    #
    #             # print(record.id)
    #             # print(invoices_obj)
    #
    #             l.append(record.id)
    #         else:
    #             return
    #     print(l)
    #     self.list_cwip_asset = [(6, 0, l)]
    #

    # list_cwip_asset = fields.One2many('account.invoice.line' ,'cwip_asset__id', string = "Invoices")
    # list_cwip_asset1 = fields.One2many('account.invoice' , 'id' , string = "Invoices2")

    # @api.onchange('cwip_category_id')
    # def Data_from_account_invoice_line(self):
    #     abc = ['account.invoice.line']
    #     invoices_obj = self.env['account.invoice.line'].search([('cwip_asset__id', '=', self.cwip_category_id.id)])
    #     print(invoices_obj)
    #
    #     l = []
    #     for record in invoices_obj:
    #         if invoices_obj:
    #
    #             # print(record.id)
    #             # print(invoices_obj)
    #
    #             l.append(record.id)
    #         else:
    #             return
    #     print(l)
    #     self.list_cwip_asset = [(6, 0, l)]
    #
    #
    # @api.onchange('cwip_category_id')
    # def Data_from_account_invoice(self):
    #     invoices_obj = self.env['account.invoice.line'].search([('cwip_asset__id', '=', self.cwip_category_id.id)])
    #     # invoices_obj2 = self.env['account.invoice'].search([('id', '=', )])
    #     # abc = str(invoices_obj)
    #     # xyz = re.findall('\d+', abc)
    #     # print(xyz)
    #     # print(xyz)
    #     # print(xyz)
    #     # print(xyz)
    #     l1 = []
    #     for record in invoices_obj:
    #         if invoices_obj:
    #             # print(record.invoice_id.id , "this is it")
    #             invoices_obj2 = self.env['account.invoice'].search([('id', '=', record.invoice_id.id)])
    #
    #             for record2 in invoices_obj2:
    #                 if invoices_obj2:
    #                     l1.append(record2.id)
    #
    #                 else:
    #                     return
    #
    #     print(l1 , "first")
    #     print(l1 , "second")
    #     self.list_cwip_asset1 = [(6, 0, l1)]