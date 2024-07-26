from odoo import fields, models

class Documentos(models.Model):
    _name = 'documentos.documentos'
    
    name = fields.Char(string="Nombre del documento")
    documento = fields.Binary("Documento")
    carpeta = fields.Many2one('documentos.carpetas',string="Carpetas", tracking=True)
    