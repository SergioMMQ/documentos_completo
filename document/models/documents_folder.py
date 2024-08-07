from odoo import models, fields

class Folder(models.Model):
    _name = 'documents.folder'
    _description = 'Carpeta de documentos'

    name = fields.Char(string='Nombre', required=True)
    description =fields.Text(string='Descripcion de la carpeta')
    parent_id = fields.Many2one('documents.folder', string='Carpeta padre')
    child_ids = fields.One2many('documents.folder', 'parent_id', string='Carpeta hija')
    document_ids = fields.One2many('documentos.documentos', 'folder_id', string='Documentos')


    create_date = fields.Datetime(string='Fecha de creación')
    write_date = fields.Datetime(string='Fecha de actualización')

