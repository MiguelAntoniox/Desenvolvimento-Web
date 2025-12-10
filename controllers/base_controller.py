class Basecontroller: 
    def __init__(self, app):
        self.app = app 
        if hasattr(self, 'rotas'):
            self.registrar_rotas()
            
            
    """metodo que registra as rotas"""        
    def registrar_rotas(self):
        for endereco_url, nome_rota, funcao_resposta in self.rotas: 
            self.app.add_url_rule(endereco_url, nome_rota, funcao_resposta)
                    