import shelve

#Abrir o crear la base de datos
with shelve.open('empresa_shelve') as db:
    #Crear un nuevo empleado
    db['usuario1'] =   {
                        'nombres': 'Juan Jose',
                        'apellidos': 'Perez Prieto',
                        'cargo': 'Gerente',
                        'telefono': 32145679,
                        'edad': 30,
                        'fecha_nac': '1994-10-01',
                        'correo': 'jj@j.com',
                        'direccion': 'Cra 1 23 54',
                        'ciudad': 'Cali',
                        'pais': 'Colombia'
                       }
    db['usuario2'] =   {
                        'nombres': 'Ricardo Alonso',
                        'apellidos': 'Tapias Modelo',
                        'cargo': 'Conductor',
                        'telefono': '3174587965',
                        'edad': '50',
                        'fecha_nac': '1974-03-29',
                        'correo': 'tapias@correo.com',
                        'direccion': 'Diag 1sur 34 34 este',
                        'ciudad': 'Medellin',
                        'pais': 'Colombia'
                       }
    
    # Leer datos
    print(db['usuario1'])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    """
    for key in db:
    print(f("{key}, {db[key]}")
    """