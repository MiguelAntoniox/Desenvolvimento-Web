from flask import render_template
from controllers.base_controller import Basecontroller

class HTMLBasicoController(Basecontroller):
    
    def __init__(self, app):
        self.rotas = [
            ("/", "main", self.pagina_inicial),
            ("/PI", "PI", self.pagina_PI),
            ("/Sobre", "Sobre", self.pagina_Sobre),
            ("/Curso", "Curso", self.pagina_Curso),
        ]
        super().__init__(app)
        
        
    def pagina_inicial(self):
        return render_template("index.html")   
    
    def pagina_PI(self):
        return render_template("PI.html") 
      
    def pagina_Sobre(self):
        return render_template("Sobre.html")
       
    def pagina_Curso(self):
        return render_template("Curso.html")    
    
    
    
    
    