from flask import Flask, render_template, url_for
import sqlite3
import os

app = Flask(__name__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, 'tienda.db')

def obtener_datos():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        SELECT animales.id, animales.nombre, animales.especie, animales.imagen,
               controles.fecha, controles.tipo
        FROM animales
        INNER JOIN controles ON animales.id = controles.animal_id
        ORDER BY animales.id, controles.fecha DESC
    """)
    filas = c.fetchall()
    conn.close()
    lista = []
    for f in filas:
        lista.append({
            'animal_id': f[0],
            'nombre': f[1],
            'especie': f[2],
            'imagen': f[3],   
            'fecha': f[4],
            'tipo': f[5]
        })
    return lista

@app.route('/')
def index():
    datos = obtener_datos()
    return render_template('index.html', lista=datos)

if __name__ == '__main__':
    app.run(debug=True)
