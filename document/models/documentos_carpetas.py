#
#from odoo import fields, models, api
#
#class Carpetas(models.Model):
#    _name = 'documentos.carpetas'
#    _order = 'nombre_completo'
#    
#    name = fields.Char(string="Nombre de la carpeta")
#    carpeta_padre = fields.Many2one('documentos.carpetas', string="Carpeta Padre")
#    nombre_completo = fields.Char("Nombre Completo", compute='_compute_nombre', recursive=True, store=True)
#    
#    @api.depends('name', 'carpeta_padre.nombre_completo')
#    def _compute_nombre(self):
#        for documentos_carpetas in self:
#            if documentos_carpetas.carpeta_padre:
#                documentos_carpetas.nombre_completo = '%s / %s' % (documentos_carpetas.carpeta_padre.nombre_completo, documentos_carpetas.name)
#            else:
#                documentos_carpetas.nombre_completo = documentos_carpetas.name


from odoo import fields, models, api

class Carpetas(models.Model):
    _name = 'documentos.carpetas'
    _order = 'name'
    
    name = fields.Char("Nombre Completo", compute='_compute_nombre', recursive=True, store=True)
    nombre_completo = fields.Char(string="Nombre de la carpeta")
    carpeta_padre = fields.Many2one('documentos.carpetas', string="Carpeta Padre")
    
    
    @api.depends('nombre_completo', 'carpeta_padre.name')
    def _compute_nombre(self):
        for documentos_carpetas in self:
            if documentos_carpetas.carpeta_padre:
                documentos_carpetas.name = '%s / %s' % (documentos_carpetas.carpeta_padre.name, documentos_carpetas.nombre_completo)
            else:
                documentos_carpetas.name = documentos_carpetas.nombre_completo
