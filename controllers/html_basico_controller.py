from flask import render_template
from controllers.base_controller import Basecontroller

class HTMLBasicoController(Basecontroller):
    
    def __init__(self, app):
        self.rotas = [
           ("/", "home", self.pagina_login),
            ("/index", "main", self.pagina_inicial),
            ("/PI", "PI", self.pagina_PI),
            ("/Sobre", "Sobre", self.pagina_Sobre),
            ("/Curso", "Curso", self.pagina_Curso),
            #("/cadastro", "cadastro", self.pagina_cadastro)
        ]
        super().__init__(app)
        
    
    def pagina_login(self):
        return render_template("login.html") 
        
    def pagina_inicial(self):
        return render_template("index.html")   

    def pagina_PI(self):
        return render_template("PI.html") 
      
    def pagina_Sobre(self):
        return render_template("Sobre.html")
       
    def pagina_Curso(self):
        return render_template("Curso.html")  
      
    def pagina_cadastro(self):
        return render_template("cadastro.html")
    
    
    
    
    