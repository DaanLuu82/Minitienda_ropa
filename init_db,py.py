from app import app, db
from models import Producto

with app.app_context():
    db.create_all()
    if not Producto.query.first():
        db.session.add_all([
            Producto(nombre='Polo Casual', precio=45.0, imagen='img/polo.jpeg'),
            Producto(nombre='Jeans Skinny Mujer', precio=120.0, imagen='img/jeans.jpeg'),
            Producto(nombre='Casaca Deportiva', precio=180.0, imagen='img/casaca.jpeg')
        ])
        db.session.commit()
