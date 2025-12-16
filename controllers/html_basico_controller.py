from flask import render_template
from controllers.base_controller import Basecontroller

class HTMLBasicoController(Basecontroller):
    
    def __init__(self, app):
        self.rotas = [
           ("/", "home", self.pagina_login), # controle de rotas para as paginas
           ("/index", "main", self.pagina_inicial),
           ("/cadastro", "novocadastro", self.pagina_cadastro), # nome da rota nao pode ser igual ao controller do formulari
           ("/projetos", "projetos", self.pagina_projetos),
           ("/Sobre", "Sobre", self.pagina_Sobre),
           ("/Curso", "Curso", self.pagina_Curso),
            
        ]
        super().__init__(app)
        
    
    def pagina_login(self):
        return render_template("login.html")
     
    def pagina_cadastro(self):
        return render_template("cadastro.html")
        
    def pagina_inicial(self):
        return render_template("index.html")   

    def pagina_projetos(self):
        return render_template("projetos.html") 
      
    def pagina_Sobre(self):
        return render_template("Sobre.html")
       
    def pagina_Curso(self):
        return render_template("Curso.html")  
      
    
    
    
    
    
    