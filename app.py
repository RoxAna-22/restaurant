import sqlite3  

# Conexión a la base de datos
conn = sqlite3.connect("restaurante.db")


conn.execute(
    """ 
    CREATE TABLE IF NOT EXISTS platos(
        id INTEGER PRIMARY KEY, 
        nombre TEXT NOT NULL,
        precio REAL NOT NULL
    )
    """
)


conn.execute(
    """ 
    CREATE TABLE IF NOT EXISTS mesas(
        id INTEGER PRIMARY KEY,
        numero INTEGER NOT NULL
    )
    """
)


conn.execute(
    """ 
    CREATE TABLE IF NOT EXISTS pedidos(
        id INTEGER PRIMARY KEY, 
        plato_id INTEGER NOT NULL,
        mesa_id INTEGER NOT NULL,
        cantidad INTEGER NOT NULL,
        fecha DATE NOT NULL,
        FOREIGN KEY (plato_id) REFERENCES platos(id),
        FOREIGN KEY (mesa_id) REFERENCES mesas(id)
    )
    """
)

# Insertar datos en la tabla de platos
conn.execute("INSERT INTO platos (nombre, precio) VALUES ('Pizza', 12.50)")
conn.execute("INSERT INTO platos (nombre, precio) VALUES ('Pasta', 8.99)")
conn.execute("INSERT INTO platos (nombre, precio) VALUES ('Ensalada', 6.50)")
conn.execute("INSERT INTO platos (nombre, precio) VALUES ('Sopa', 5.00)")
conn.execute("INSERT INTO platos (nombre, precio) VALUES ('Hamburguesa', 10.00)")

# Insertar datos en la tabla de mesas
conn.execute("INSERT INTO mesas (numero) VALUES (1)")
conn.execute("INSERT INTO mesas (numero) VALUES (2)")
conn.execute("INSERT INTO mesas (numero) VALUES (3)")
conn.execute("INSERT INTO mesas (numero) VALUES (4)")
conn.execute("INSERT INTO mesas (numero) VALUES (5)")

# Insertar datos en la tabla de pedidos
conn.execute("INSERT INTO pedidos (plato_id, mesa_id, cantidad, fecha) VALUES (1, 1, 2, '2024-10-31')")
conn.execute("INSERT INTO pedidos (plato_id, mesa_id, cantidad, fecha) VALUES (2, 2, 1, '2024-11-01')")
conn.execute("INSERT INTO pedidos (plato_id, mesa_id, cantidad, fecha) VALUES (3, 3, 3, '2024-11-02')")
conn.execute("INSERT INTO pedidos (plato_id, mesa_id, cantidad, fecha) VALUES (4, 4, 1, '2024-11-03')")
conn.execute("INSERT INTO pedidos (plato_id, mesa_id, cantidad, fecha) VALUES (5, 5, 2, '2024-11-04')")

# Confirmar los cambios en la base de datos
conn.commit()

# Consultar y mostrar los datos de cada tabla
print("\nPLATOS")
cursor = conn.execute("SELECT * FROM platos")
for row in cursor:
    print(row)

print("\nMESAS")
cursor = conn.execute("SELECT * FROM mesas")
for row in cursor:
    print(row)

print("\nPEDIDOS")
cursor = conn.execute("SELECT * FROM pedidos")
for row in cursor:
    print(row)

# Cerrar la conexión
conn.close()
