# -*- coding: utf-8 -*-
from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _name = "purchase.order"
    _inherit = "purchase.order"

    state = fields.Selection([
        ('draft', 'Draft'),
        ('purchase', 'Final'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled')
    ], string='Status', readonly=True, index=True, copy=False, default='draft', tracking=True)

    @api.onchange('partner_id')
    def onchange_partner(self):
        return {'domain': {'partner_id': [('ss', '=', 'vendor')]}}
