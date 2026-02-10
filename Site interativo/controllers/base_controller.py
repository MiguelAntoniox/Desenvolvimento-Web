from flask import session, redirect, url_for # session vai armazenar informaçoes especificas do usuario ---  redirection serve para levar para outra pagina --- 
from functools import wraps # isso que vai garantir que o usuario vai estar logado 


def login_required(f): # essa funcao recebe uma funcao f como parametro
    @wraps(f) # pelo jeito salva as informacoes da funcao f
    def decorated_function(*args, **kwargs): # funcao com args para argmentos (vir tupla) e kwargs para argumentos nomeados (vira dicionario)
        if not session.get("usuario_logado"):  # caso a sessao nao esteja logada
            return redirect(url_for("login")) # retorna para a pagina de login
        
        
        
