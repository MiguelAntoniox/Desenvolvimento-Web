from flask import render_template, request
from controllers.base_controller import Basecontroller


class Formulario_controller(Basecontroller):
    
    def __init__(self, app):
        self.rotas = [
            ("/login", "login", self.pagina_login, ['POST']),
            ("/cadastro", "cadastro", self.pagina_cadastro, ['POST']),
        ]
    
        super().__init__(app)
        
    def pagina_login(self):
       
    
        email = request.form.get("email")
        senha = request.form.get("senha")
        
        if not email or not senha:
            return "prencha todos os dados"
        
        return render_template("index.html") 
    
    def pagina_cadastro(self):
        
        email = request.form.get("email")
        senha = request.form.get("senha")
        
        if not email or not senha:
            return "prencha todos os dados"

        
        return render_template("login.html") 
        
        
       