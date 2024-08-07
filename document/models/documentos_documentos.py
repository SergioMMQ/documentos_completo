from odoo import fields, models

class Documentos(models.Model):
    _name = 'documentos.documentos'
    _description = 'Document'
    
    name = fields.Char(string="Nombre", required=True)
    description = fields.Text(string='Descripción del documento')
    type = fields.Selection([
        ('file','Archivo'),
        ('url','Enlace'),
        ('note','Nota')
        ], string='Tipo', required=True, default='file')
    content = fields.Text(string='Contenido')
    file_name = fields.Char(string='Nombre del archivo adjunto')
    file = fields.Binary(string='Archivo')
    url = fields.Char(string='Enlace')
    folder_id = fields.Many2one('documents.folder',string='Carpeta')
    tag_ids = fields.Many2many('document.tag',string='Etiquetas')
    res_model = fields.Char(string='Modelo relacionado')
    date = fields.Datetime(string='Fecha de creación', default=fields.Datetime.now)
    author_id = fields.Many2one('res.users', string='Autor', default=lambda self: self.env.user)

