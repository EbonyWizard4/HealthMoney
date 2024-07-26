""" Modulo Principal """
import os

from flask import Flask

def min_app():
    """ Inicializa o flask
    Retorna:
        instância do flask
    """
    app = Flask(__name__)
    return app

def create_app():
    """ Inicializa o app
    Retorna:
        Obj app
    """
    app = min_app()
    return app
