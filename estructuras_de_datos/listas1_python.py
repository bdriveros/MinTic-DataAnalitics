#Nomenclatura: 0=cedula, 1=Nombre, 2=apellido; 3=edad, 4=direccion, 5=téléfono(caracter)
"""
Insertar aquí comentario 
en varias lineas
"""
lista_estudiante=[1067543234,"Juanito","Pérez",30,"Carrera 50 # 45 - 80","5643245"]
print("Imprimiendo la lista completa:")
print(lista_estudiante)
print("Imprimiendo un elemento de la lista:")
print(lista_estudiante[2])
print("Imprimiendo la última posición de la lista:")
#Solución Jesús
print(lista_estudiante[5])
print(lista_estudiante[-1])
print(lista_estudiante[len(lista_estudiante)-1])
print("Imprimiendo varios valores de la lista (valores 2 a 4):")
print(lista_estudiante[2:4])
print("Imprimir la longitud de la lista")
print(len(lista_estudiante))
#Concatenar
print(f"La longitud de la lista es: {len(lista_estudiante)} ")

"""
Modificando elementos de la lista
"""
print(f"Dirección antigua del estudiante: {lista_estudiante[4]}")
lista_estudiante[4]="Calle 26 # 7 -65"
print(f"Dirección nueva del estudiante: {lista_estudiante[4]}")
#Cambiando la cédula:
print(f"Cédula antigua:{lista_estudiante[0]}")
lista_estudiante[0]=1209876543
print(f"Cédula nueva:{lista_estudiante[0]}")

"""
Agregando nuevos elementos a la lista
"""

#Insertar al final de la lista
lista_estudiante.append("M")
print(lista_estudiante)

#Insertar en una posición dada de la lista
lista_estudiante.insert(0,"Casado")
print(lista_estudiante)

lista_estudiante.append("3154446573")
lista_estudiante.append("3154446572")
print(lista_estudiante)

#ELIMINAR DATOS DE LA LISTA
lista_estudiante.pop(0)
print (lista_estudiante)
#ELIMINAR INDICE

del lista_estudiante[2]
print (lista_estudiante)

lista_estudiante.remove("3154446573")
print (lista_estudiante)
