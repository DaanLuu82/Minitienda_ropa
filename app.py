from flask import Flask, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'

# Productos locales
productos = [
    {"id": 1, "nombre": "Polo Casual",        "precio": 45.00,  "imagen": "polo.jpeg"},
    {"id": 2, "nombre": "Jeans Skinny Mujer", "precio": 120.00, "imagen": "jeans.jpeg"},
    {"id": 3, "nombre": "Casaca Deportiva",   "precio": 180.00, "imagen": "casaca.jpeg"},
]

@app.route('/')
@app.route('/catalogo')
def catalogo():
    return render_template('catalogo.html', productos=productos)

@app.route('/agregar/<int:id>')
def agregar(id):
    # Inicializa carrito como dict
    if 'carrito' not in session or isinstance(session['carrito'], list):
        session['carrito'] = {}
    carrito = session['carrito']
    key = str(id)
    carrito[key] = carrito.get(key, 0) + 1
    session.modified = True
    return redirect(url_for('ver_carrito'))

@app.route('/carrito')
def ver_carrito():
    carrito_data = session.get('carrito', {})
    productos_carrito = []
    total = 0.0

    for id_str, cantidad in carrito_data.items():
        prod = next((p for p in productos if p['id']==int(id_str)), None)
        if prod:
            subtotal = prod['precio'] * cantidad
            total += subtotal
            productos_carrito.append({
                **prod,
                'cantidad': cantidad,
                'subtotal': round(subtotal,2)
            })

    return render_template('carrito.html', carrito=productos_carrito, total=round(total,2))

@app.route('/vaciar')
def vaciar():
    session.pop('carrito', None)
    session.modified = True
    return redirect(url_for('ver_carrito'))

if __name__ == '__main__':
    app.run(debug=True)
