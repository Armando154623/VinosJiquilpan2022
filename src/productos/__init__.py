# El archivo __init__ es constructor del módulo productos
from flask import Blueprint

# Definir el blueprint
producto = Blueprint('productos', __name__, url_prefix='/productos')

from . import route
