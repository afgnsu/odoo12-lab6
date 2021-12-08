# -*- coding: utf-8 -*-
{
    'name': "Lab6(Todo待辦事項)",

    'summary': "Odoo12_Todo",

    'description': "介吾測試",

    'author': "蘇介吾",
    'website': "http://afgn.cc",

    'category': 'Uncategorized',
    'version': '12.0.1',

    'depends': ['base', 'web'],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
