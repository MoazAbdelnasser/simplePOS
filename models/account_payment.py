# -*- coding: utf-8 -*-
from odoo import models, fields, api


class AccountPayment(models.Model):
    _inherit = 'account.payment'
    _name = 'account.payment'

    @api.onchange('partner_id')
    def onchange_partner(self):
        if self.partner_type == 'customer':
            return {'domain': {'partner_id': [('ss', '=', 'customer')]}}
        else:
            return {'domain': {'partner_id': [('ss', '=', 'vendor')]}}
