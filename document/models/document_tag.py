from odoo import models, fields

class DocumentTag(models.Model):
    _name = 'document.tag'
    _description = 'Etiqueta de documento'

    name = fields.Char(string='Nombre de la etiqueta', required=True)
    color = fields.Integer(string='Color de la etiqueta')
#    document_ids = fields.Many2many('document.document', string='Documentos')
