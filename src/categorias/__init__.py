# El archivo __init__ es constructor del módulo categorias
from flask import Blueprint

# Definir el blueprint
categoria = Blueprint('categorias', __name__, url_prefix='/categorias')

from . import route
