"""essa brincadeira aqui a baixo que vai controlar os logins e validar se as informaçoes batem para logar no sitema
pq ainda nao temos banco de dados"""


from flask import render_template, session, request, redirect, url_for
from controllers.base_controller import Basecontroller


"""definindo as rotas de login """
class Logincontroller(Basecontroller):
    def __init__(self,app):
        self.rotas[
            ('/login', 'login', self.login),
            ('/entrar', 'entrar', self.entrar, ['POST']),  
            ('/logout', 'logout', self.logout),
        ]


        

    


