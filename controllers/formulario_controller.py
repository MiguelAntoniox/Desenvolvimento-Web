from flask import render_template, request
from controllers.base_controller import Basecontroller


class Formulario_controller(Basecontroller):
    
    def __init__(self, app):
        self.rotas = [
            ("/login", "login", self.pagina_login),
            ("/cadastro", "cadastro", self.pagina_cadastro)
        ]
    
    
    def pagina_login(self):
        return render_template("login.html") 
    
    def pagina_cadastro(self):
        return render_template("cadastro.html")