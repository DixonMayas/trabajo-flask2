import sqlite3
import os

DB = 'tienda.db'

def ensure_db():
    exists = os.path.exists(DB)
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    if not exists:
        c.execute("CREATE TABLE IF NOT EXISTS animales (id INTEGER PRIMARY KEY, nombre TEXT, especie TEXT)")
        c.execute("CREATE TABLE IF NOT EXISTS controles (id INTEGER PRIMARY KEY, animal_id INTEGER, fecha TEXT, tipo TEXT)")
        conn.commit()
        c.execute("INSERT INTO animales (nombre, especie) VALUES (?, ?)", ("Firulais", "Perro"))
        c.execute("INSERT INTO animales (nombre, especie) VALUES (?, ?)", ("Misu", "Gato"))
        c.execute("INSERT INTO animales (nombre, especie) VALUES (?, ?)", ("Piolín", "Ave"))
        conn.commit()
        c.execute("INSERT INTO controles (animal_id, fecha, tipo) VALUES (?,?,?)", (1, "2025-10-01", "Vacunación"))
        c.execute("INSERT INTO controles (animal_id, fecha, tipo) VALUES (?,?,?)", (2, "2025-09-20", "Desparasitación"))
        c.execute("INSERT INTO controles (animal_id, fecha, tipo) VALUES (?,?,?)", (3, "2025-08-15", "Chequeo"))
        conn.commit()
        print("Base de datos creada con ejemplos.")

    c.execute("PRAGMA table_info(animales)")
    cols = [row[1] for row in c.fetchall()]
    if 'imagen' not in cols:
        try:
            c.execute("ALTER TABLE animales ADD COLUMN imagen TEXT")
            conn.commit()
            print("Columna 'imagen' añadida a 'animales'.")
        except Exception as e:
            print("No se pudo agregar la columna (quizá ya existe):", e)
    else:
        print("La columna 'imagen' ya existe.")

    try:
        c.execute("UPDATE animales SET imagen = 'perro.jpg' WHERE especie = 'Perro'")
        c.execute("UPDATE animales SET imagen = 'gato.jpg' WHERE especie = 'Gato'")
        c.execute("UPDATE animales SET imagen = 'ave.jpg' WHERE especie = 'Ave'")
        conn.commit()
        print("Registros de ejemplo actualizados con nombres de imagen.")
    except Exception as e:
        print("Error al actualizar nombres de imagen:", e)

    conn.close()

if __name__ == '__main__':
    ensure_db()