#Instalacion de libreria: pip install tinydb (Entorno Virtual)

from tinydb import TinyDB, Query

# Crear o abrir la base de datos
db = TinyDB('empresa.json')

# Insertar un registro
db.insert({
            'cedula': '123456789',
            'nombres': 'Juan',
            'apellidos': 'Perez',
            'cargo': 'Dba',
            'telefono': '654321',
            'edad': '30',
            'fecha_nac': '2021-10-01',
            'correo': 'j@j.com',
            'direccion': 'Cra 1 34 34',
            'ciudad': 'Bogotá',
            'pais':  'Colombia'
            })

usuario = Query()
resultado = db.search(usuario.nombres == 'Juan')
print(resultado)

db.close()