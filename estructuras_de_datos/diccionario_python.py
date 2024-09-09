'''
Diccionario en Python
'''
# Creacion
diccionario_estudiantes = {
    'nombres': ['Juan', 'Pedro', 'Maria'],

    'edad': [30, 25, 25 ],
    'Ciudad': ['Bogotá','Sopo','Leticia'],
    'Hermanos': ['Mateo'],
    'Parientes':{
        'Mamá': 'Maria Lopez',
        'Papá': 'Juan Perez',
        'Esposa':'Jenifer Tolosa'
        }
    }
print(diccionario_estudiantes)
#Acceso a valores
print(diccionario_estudiantes['nombres'])
# Modificar
diccionario_estudiantes['Ciudad'] = 'Madrid'
# print(diccionario_estudiantes)
# # Eliminar
# del  diccionario_estudiantes['edad']
# print(diccionario_estudiantes)
