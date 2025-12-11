from flask import Flask
from controllers.html_basico_controller import HTMLBasicoController
from controllers.formulario_controller import Formulario_controller

app = Flask(__name__)

HTMLBasicoController(app)
Formulario_controller(app)


if __name__ == "__main__":
    app.run(debug=True)
    
        