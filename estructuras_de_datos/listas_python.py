# Creacion lista
"""
    Preguntas
"""
lista_estudiante = [123456789,"PEPITO", "PEREZ", 30, "Cra 59 12 43", "601001321456"]
print("Imprimiendo la lista completa")
print (lista_estudiante)
print("Imprimiendo un elemento de la lista")
print (lista_estudiante[2]) # Posicion 2 
print(lista_estudiante[2:4]) # Entre 2 campos
print(lista_estudiante[-1]) # Traer un dato del final hacia el inicio
print(len(lista_estudiante)) # contar largo
print(f"La longitud de la lista es:{len(lista_estudiante)}") # Concatenar
"""
    Modificando elementos de la lista
"""
print(f"La longitud de la lista es:{len(lista_estudiante)}") # Concatenar

lista_estudiante[4] = "Cra 50 20 40"
print(lista_estudiante)
"""
Agregando nuevos elementos
"""
lista_estudiante.append("M")
print(lista_estudiante)
lista_estudiante.insert(0,"Casado")
print(lista_estudiante)
cuadrados = [x**2 for x in range(10)]
print(cuadrados)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]