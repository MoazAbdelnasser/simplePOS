# -*- coding: utf-8 -*-
from odoo import models, fields


class Partner(models.Model):
    _inherit = 'res.partner'
    _name = 'res.partner'
    ss = fields.Selection([
        ('customer', 'Customer'),
        ('vendor', 'Vendor'),
        ('owner', 'Owner')
    ], string="Type")

    # Where will will set defaults of the fields using defualt_get function
    def default_get(self, vals):
        result = super(Partner, self).default_get(vals)
        result['ss'] = 'customer'
        result['city'] = 'Riyadh'
        result['country_id'] = 192
        result['state_id'] = 1411
        result['company_type'] = 'person'
        return result

    def write(self, val):
        res = super(Partner, self).write(val)
        print(val)
        return res
