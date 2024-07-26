# -*- coding: utf-8 -*-

{
    'name': 'Documentos',
    'summary':"""    Aplicacion para Documentos    """,
    'author': 'Sergio Martinez Meneses',
    'category': 'Human Resources/Employees',
    'version': '1.0.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/document_view.xml',
        'views/document_carpetas.xml',
        'views/document_menu.xml',
        'views/carpetas.xml',
        ],
    'assets': {
        'web.assets_backend': [
            'document/static/src/*.js',
            'document/static/src/*.xml',
            'document/static/src/*.scss',
        ],
    },
    'installable': True,
    'application': True,
}