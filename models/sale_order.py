# -*- coding: utf-8 -*-
from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _name = 'sale.order'

    @api.onchange('partner_id')
    def onchange_partner(self):
        return {'domain': {'partner_id': [('ss', '=', 'customer')]}}
