# -*- coding: utf-8 -*-
{
    'name': "odoo_technical_test_sb",
    'version': '1.0',
    'category': 'Test',

    'summary': 'Technical Test for Odoo Developer',
    'description': 'Módulo creado para el Technical Test for Odoo Developer, parte del proceso de selección para el puesto de Desarrollador en Smart Bamboo',
    
    'author': "Argenis Isaí López Robles",
    'website': "https://github.com/argenisailo",
    'license': 'AGPL-3',

    'depends': ['base'],

    'data': [
        'views/to_do_list_view.xml',
    ],

    'installable': True,
    'application': False,
    'auto_install': False,
}