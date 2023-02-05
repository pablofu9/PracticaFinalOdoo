from odoo import models, fields

class Empresa(models.Model):
    _name = "fctpablo.empresa"
    _description="gestion de empresas"
    name = fields.Char("Name", required=True)  # Nombre
    contact = fields.Char("Contact", required=False)  # Persona de contacto
    phone = fields.Char("Phone", required=False)  # Telefono de contacto
    email = fields.Char("Email", required=False)  # Email
    direction = fields.Char("Direction", required=False)  # Direccion
    location = fields.Char("Location", required=False)  # Localidad
    dual = fields.Selection([('0', 'Si'), ('1', 'No')], "Dual", required=True)  # Dual
    erasmus = fields.Selection([('0', 'Si'), ('1', 'No')], "Erasmus", required=True)  # Erasmus
    vacancies = fields.Char("Vacancies")  # Plazas ofertadas
    agreement = fields.Selection([('0', 'Si'), ('1', 'No')], "Agreement", required=True)  # Convenio
    task = fields.Char("Task")  # Tareas
    observations = fields.Char("Observations")  # Observaciones

    alumnos_id = fields.One2many("fctpablo.alumnos", "empresa_id", "Alumnos") #Relacion entre modelos