# -*- coding: utf-8 -*-

{
    'name': 'Documentos',
    'summary':"""    Aplicacion para Documentos    """,
    'author': 'Sergio Martinez Meneses',
    'category': 'Informes',
    'version': '1.0.0',
    'depends': ['base','base_setup','web'],
    'data': [
        'security/ir.model.access.csv',
        'views/document_view.xml',
        'views/document_menu.xml',
        'views/document_folder.xml',
        'views/document_tag.xml',
        'views/document_search.xml',
        'views/documents.xml',
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
    'license': 'LGPL-3',
}