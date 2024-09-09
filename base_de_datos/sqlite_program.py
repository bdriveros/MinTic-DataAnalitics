#Import (Importar paquetes)
import sqlite3

# Conectar a la base de datos (se crea si no existe) 
conn = sqlite3.connect('empresa.db')

""" type : Verificar tipo de dato
print(type(conn))
a=1
nombre= "Juan"
print(type(a))
print(type(nombre))
"""

# Crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()

# Crear una tabla
cursor.execute ('''
                CREATE TABLE IF NOT EXISTS usuarios
                    (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cedula INTEGER,
                    nombres VARCHAR(25),
                    apellidos VARCHAR(25),
                    cargo  TEXT,
                    telefono TEXT, 
                    edad INTEGER,
                    fecha_nac DATE,
                    correo TEXT,
                    direccion TEXT,
                    ciudad TEXT,
                    pais TEXT 
                    )'''
                )

# Insertar un registro
"""
cursor.execute('''
               INSERT INTO usuarios (cedula, nombres, apellidos, cargo, telefono,
                                    edad, fecha_nac, correo, direccion, ciudad, pais) 
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
               ''',
                (100033346, 'Ana Cecilia', 'Brito Perez', 'Dba', '3216549876',
                        35, '1996-11-01','ana@correo.co','Cr 34 23 34','Bogotá','Colombia')
                    
                )
"""
# Borrando un registro
"""
cursor.execute('''
               DELETE FROM usuarios
               WHERE id = ?
               ''',
               (2,)
                )
"""
# Actualizando un registro
cursor.execute('''
                    UPDATE usuarios
                    SET apellidos = ?, nombres = ?
                    WHERE id = ?
               ''',
                    ('Jimenez','Jose', 3)
                )

# Consultar un registro
cursor.execute('SELECT * FROM usuarios')
Filas = cursor.fetchall()

for Fila in Filas:
    print(Fila)

#Guardar (commit) los cambios
conn.commit()
#Cerrar la conexión
conn.close()