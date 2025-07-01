from flask import Flask, render_template, redirect, url_for
from models import db, Producto, CarritoItem

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tienda.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'clave-secreta'
db.init_app(app)

@app.route('/')
@app.route('/catalogo')
def catalogo():
    productos = Producto.query.all()
    return render_template('catalogo.html', productos=productos)

@app.route('/agregar/<int:id>')
def agregar(id):
    item = CarritoItem.query.filter_by(producto_id=id).first()
    if item:
        item.cantidad += 1
    else:
        nuevo = CarritoItem(producto_id=id, cantidad=1)
        db.session.add(nuevo)
    db.session.commit()
    return redirect(url_for('ver_carrito'))

@app.route('/carrito')
def ver_carrito():
    items = CarritoItem.query.all()
    total = sum(i.producto.precio * i.cantidad for i in items)
    return render_template('carrito.html', carrito=items, total=total)

@app.route('/vaciar')
def vaciar():
    CarritoItem.query.delete()
    db.session.commit()
    return redirect(url_for('catalogo'))

if __name__ == '__main__':
    app.run(debug=True)
