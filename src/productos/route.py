from src.productos import producto


@producto.route('/')
def get_productos():
    return 'OK en productos'
