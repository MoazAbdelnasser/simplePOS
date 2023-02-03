# -*- coding: utf-8 -*-
from odoo import models, fields, api


class AccountMove(models.Model):
    _name = "account.move"
    _inherit = ['account.move']

    # Where will will set defaults of the fields using defualt_get function
    @api.onchange('partner_id')
    def onchange_partner(self):
        if self.move_type == 'out_invoice':
            return {'domain': {'partner_id': [('ss', '=', 'customer')]}}
        else:
            return {'domain': {'partner_id': [('ss', '=', 'vendor')]}}
    
    # def action_view_picking(self):
    #     return self._get_action_view_picking(self.picking_ids)

    # def _get_action_view_picking(self, pickings):
    #     """ This function returns an action that display existing picking orders of given purchase order ids. When only one found, show the picking immediately.
    #     """
    #     self.ensure_one()
    #     result = self.env["ir.actions.actions"]._for_xml_id('stock.action_picking_tree_all')
    #     # override the context to get rid of the default filtering on operation type
    #     result['context'] = {'default_partner_id': self.partner_id.id, 'default_origin': self.name,
    #                          'default_picking_type_id': self.picking_type_id.id}
    #     # choose the view_mode accordingly
    #     if not pickings or len(pickings) > 1:
    #         result['domain'] = [('id', 'in', pickings.ids)]
    #     elif len(pickings) == 1:
    #         res = self.env.ref('stock.view_picking_form', False)
    #         form_view = [(res and res.id or False, 'form')]
    #         result['views'] = form_view + [(state, view) for state, view in result.get('views', []) if view != 'form']
    #         result['res_id'] = pickings.id
    #     return result

# def default_get(self, vals):
#    result = super(AccountMove, self).default_get(vals)
#   if result['move_type'] == 'out_invoice':
#      return {'domain': {'partner_id': [('ss', '=', 'customer')]}}
# else:
#    print(result)
# return result
