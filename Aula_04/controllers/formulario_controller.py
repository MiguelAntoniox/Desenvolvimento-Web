from flask import render_template, request
from controllers.base_controller import BaseController

class FormularioController(BaseController):
    def __init__(self, app):
        self.rotas = [
            ('/formulario', 'formulario', self.formulario),
            ('/formulario', 'formulario', self.formulario),
            ('/resultado', 'resultado', self.resultado, ['POST']),
            ('/formulario_extra', 'formulario_extra', self.formulario_extra),
            ('/resultado_extra', 'resultado_extra', self.resultado_extra, ['POST']),
        ]
        super().__init__(app)


    def formulario_extra(self):
        return render_template("formulario_extra.html")

    def formulario(self):
        return render_template("formulario.html")

    def resultado(self):
        nome = request.form['nome']
        email = request.form['email']
        return render_template("resultado.html", nome=nome, email=email)

    def resultado_avancado(self):
        nome = request.form.get('nome')
        email = request.form.get('email')
        sexo = request.form.get('sexo')
        hobbies = request.form.getlist('hobbies')

        if not nome or not email or not sexo or not hobbies:
            return "Por favor, preencha todos os campos obrigatórios!"

   
        mensagem = request.form.get('mensagem', '')
        curso = request.form.get('curso', '')
        return render_template("resultado.html",
                            nome=nome,
                            email=email,
                            mensagem=mensagem,
                            curso=curso,
                            sexo=sexo,
                            hobbies=hobbies)
    
    def resultado_extra(self):
        nome = request.form.get('nome')
        email = request.form.get('email')
        nascimento = request.form.get('nascimento')
        horario = request.form.get('horario')
        cor = request.form.get('cor')
        quantidade = request.form.get('quantidade')
        nota = request.form.get('nota')
        site = request.form.get('site')
        cidade = request.form.get('cidade')
        sexo = request.form.get('sexo')

       
        if not nome or not email or not sexo:
            return "Por favor, preencha os campos obrigatórios: nome, email e sexo."

       
        return render_template("resultado_avancado.html",
                               nome=nome,
                               email=email,
                               nascimento=nascimento,
                               horario=horario,
                               cor=cor,
                               quantidade=quantidade,
                               nota=nota,
                               site=site,
                               cidade=cidade,
                               sexo=sexo)
