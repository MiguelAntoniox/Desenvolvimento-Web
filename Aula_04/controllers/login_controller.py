from flask import render_template, request, redirect, url_for, session
from controllers.base_controller import BaseController

class LoginController(BaseController):
    def __init__(self, app):
        self.rotas = [
            ('/login', 'login', self.login),
            ('/entrar', 'entrar', self.entrar, ['POST']),
            ('/logout', 'logout', self.logout),
        ]
        super().__init__(app)

        
        self.usuario_correto = "senac"  
        self.senha_correta = "12345"     

    def login(self):
        if session.get("usuario_logado"): # verifica se o usuario esta em uma sessao
            return redirect(url_for("home"))  # entra na home se sim
        return render_template("login.html") # volta pro login
        

    def entrar(self):
        usuario = request.form.get("usuario")
        senha = request.form.get("senha")

        if usuario == self.usuario_correto and senha == self.senha_correta:
            session["usuario_logado"] = True
            return redirect(url_for("home"))
        else:
            erro = "Usuário ou senha incorretos!"
            return render_template("login.html", erro=erro)

    def logout(self):
        session.clear()
        return redirect(url_for("login"))