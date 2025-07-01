from app import app, db
from models import Producto

with app.app_context():
    db.create_all()

    # Elimina datos previos si ya existen
    Producto.query.delete()

    # Agrega productos de ejemplo
    productos = [
        Producto(nombre='Polo Casual', precio=45.0, imagen='img/polo.jpeg'),
        Producto(nombre='Jeans Skinny Mujer', precio=120.0, imagen='img/jeans.jpeg'),
        Producto(nombre='Casaca Deportiva', precio=180.0, imagen='img/casaca.jpeg'),
        Producto(nombre='Blusa Elegante', precio=70.0, imagen='img/blusa.jpeg'),
        Producto(nombre='Short Verano', precio=55.0, imagen='img/short.jpeg'),
        Producto(nombre='Zapatillas Urbanas', precio=150.0, imagen='img/zapatillas.jpeg')
    ]

    db.session.add_all(productos)
    db.session.commit()

    print(" Base de datos inicializada correctamente.")
