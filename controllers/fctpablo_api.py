from odoo import http


# Para comprobar el funcionamiento de la api-rest
# Lo que hace este metodo es recorrer toda la lista de alumnos que tenemos y sacar por pantalla sus nombres
class Fctpablo_Api(http.Controller):

    @http.route('/api/nombres', auth='public', method=['GET'], csrf=False)
    def __index__(self, **kw):
        alumnos = http.request.env['fctpablo.alumnos'].search([])
        output = "<h1>Alumnos</h1><ul>"
        for alumno in alumnos:
            output += '<li>' + alumno['name'] + '</li>'
        output += "</ul>"
        return "HELLO, API IS WORKING" + output

