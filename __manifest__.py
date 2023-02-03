# -*- coding: utf-8 -*-
{
    'name': "Simple Sale Buy Inventory Management",

    'summary': """Simple Sales Purchages and Inventory Management Software""",
    'sequence': 1,
    'description': """Simple Sales Purchages and Inventory Management Software
     Based on latest Technologies specially odoo """,
    'author': "Moaz Abdelnasser",
    'website': "http://www.Simple_Tech.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'sale', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/simple_pos_action_custom.xml',
        'views/simple_pos_Menu_custom.xml',
        'views/res_partner.xml',
        'views/sale_order.xml',
        'views/purchage_order.xml',
        'views/account_move.xml',

    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False
}
