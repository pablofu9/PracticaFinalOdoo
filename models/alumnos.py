from odoo import models, fields, api


class Alumnos(models.Model):
    _name = "fctpablo.alumnos"
    _description="gestion de alumnos"
    name = fields.Char("Name", required=True)  # Nombre
    surname = fields.Char("Surname", required=True)  # Apellido
    date_birth = fields.Date("Birth date")  # Fecha de nacimiento
    photo = fields.Binary(string="Photo")  # Foto
    first_year = fields.Integer("Primer año de estudios", required=True)  # Primer año
    academic_year = fields.Char(string="Año academico", compute='_valueyear', store=True)  # Curso academico
    email = fields.Char("Email", required=False)  # Email
    phone = fields.Char("Phone", required=False)  # Telefono
    grade = fields.Selection([('0', 'DAM'),
                              ('1', 'DAW'), ('2', 'ASIR'), ('3', 'SMR'), ('4', 'IC'), ('5', 'IO')],
                             "Grade", required=True)  # Estudio
    period = fields.Selection([('0', 'Marzo'), ('1', 'Septiembre')], "Period", required=True)  # Periodo de practicas
    dual = fields.Selection([('0', 'Si'), ('1', 'No')], "Dual", required=True)  # Dual
    erasmus = fields.Selection([('0', 'Si'), ('1', 'No')], "Erasmus", required=True)  # Erasmus
    observations = fields.Char("Observations", required=False)  # Observaciones

    empresa_id = fields.Many2one("fctpablo.empresa", "Empresa", ondelete="cascade")


@api.depends('first_year', 'academic_year')
def _valueyear(self):
    for record in self:
        record.academic_year = str(record.first_year) + "/" + str(record.first_year + 1)


""""
class Fichas_Alumnos_Report(models.AbstractModel):
    _name = 'report.fctpablo.report_imprimir_fichas'
    _descripcion = 'modelo abstracto para imprimir las fichas de los alumnos'

    def _get_report_values(self, docids=None, data=None):
        docids = self.env["fctpablo.alumnos"].search([]).ids
        docs = self.env['fctpablo.alumnos'].search([])
        print(data)
        return {
            'doc_ids': docids,
            'doc_model': self.env['fctpablo.alumnos'],
            'docs': docs,
            'data': data,
        }
        """
