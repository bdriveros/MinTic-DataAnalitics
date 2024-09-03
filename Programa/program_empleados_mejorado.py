#Shelve 
import os # El módulo os en Python proporciona y expone los detalles y la funcionalidad del sistema operativo
import shelve # shelve implementa el almacenamiento persistente para objetos arbitrarios de Python que pueden ser serializados, usando una interfaz de programación similar a un diccionario.
import re

def limpiar_pantalla():
    # Verificar el sistema operativo
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para Unix/Linux/MacOS
        os.system('clear')
# CRUD

def crear_empleado(db): # C (Create Creación empleados)
    print("*"*18)
    print("* CREAR EMPLEADO *")
    print("*"*18)
    while True:
        cedula = (input("Introduce la cedula: "))
        if not cedula.isdigit() or cedula in db:
            print(f"La cedula debe ser número entero positivo y único")
        else:
            break

    nombres = input("Introduce los nombres del empleado: ")
    apellidos = input("Introduce los apellidos del empleado: ")
    
    while True:
        try:
            edad = int(input("Introduce la edad del empleado: "))
            if edad <= 0:
                raise ValueError("La edad debe ser positiva")
            break
        except ValueError:
            print("La edad debe ser un número entero positivo.")
    
    cargo = input("Introduce el cargo del empleado: ")
    fecha_ing = input("Introduce la fecha de ingreso del empleado: ")
    eps = input("Introduce la eps del empleado: ")
    salario = float(input("Introduce el salario: "))
    tipo_de_contrato = input("Introduce el tipo de contrato del empleado: ")
    
   

    db[cedula]  = {
        'cedula': cedula,
        'nombres': nombres,
        'apellidos': apellidos,
        'edad': edad,
        'cargo': cargo,
        'fecha_ing': fecha_ing,
        'eps': eps,
        'salario': salario,
        'tipo_contrato': tipo_de_contrato    
    }
    limpiar_pantalla() #Limpiar Pantalla
    print(f"El empleado {nombres+' '+apellidos} con cedula {cedula} fue creado exitosamente")
    
def listar_empleados(db): #R (Read Listar empleados)
    print("*"*20)
    print("* LISTADO EMPLEADOS *")
    print("*"*20)
    for fila in db:
        empleado = db[fila]
        print("*"*30)
        print(f"Cedula: {empleado['cedula']}")
        print(f"Nombres: {empleado['nombres']}")
        print(f"Apellidos: {empleado['apellidos']}")      
        print(f"Edad: {empleado['edad']}") 
        print(f"Cargo: {empleado['cargo']}")  
        print(f"Fecha Ingreso: {empleado['fecha_ing']}")
        print(f"Eps: {empleado['eps']}")
        print(f"Salario: {empleado['salario']}")
        print(f"Tipo de contrato: {empleado['tipo_contrato']}")

def actualizar_empleados(db): #U (Update Actualizar empleados)
    cedula=input("Introduce la cedula que desea actualizar: ")
    if cedula in db:
        print(f"La cedula {cedula} se encuentra registrada en la base de datos")
        print(f"Alerta: presiona enter en caso de querer continuar sin cambios")
        #cedula = (input("Introduce la cedula: "))
        new_nombres = input("Introduce los nuevos nombres del empleado: ")
        new_apellidos = input("Introduce los nuevos apellidos del empleado: ")
        new_edad = input("Introduce la nueva edad del empleado: ")
        new_cargo = input("Introduce el nuevo cargo del empleado: ")
        new_fecha_ing = input("Introduce la nueva fecha de ingreso del empleado: ")
        new_eps = input("Introduce la nueva eps del empleado: ")
        new_salario = input("Introduce el nuevo salario: ")
        new_tipo_de_contrato = input("Introduce el nuevo tipo de contrato del empleado: ")
        
        empleado=db[cedula]
        
        if new_nombres:
            empleado['nombres']=new_nombres
        if new_apellidos:
            empleado['apellidos']=new_apellidos
        if new_edad:
            empleado['edad']=int(new_edad)
        if new_cargo:
            empleado['cargo']=new_cargo
        if new_fecha_ing:
            empleado['fecha_ing']=new_fecha_ing
        if new_eps:
            empleado['eps']=new_eps
        if new_salario:
            empleado['salario']=float(new_salario)
        if new_tipo_de_contrato:
            empleado['tipo_contrato']=new_tipo_de_contrato
            
        db[empleado['cedula']]=empleado  # actualiza el empleado en la base de datos
        print(f"El empleado con la cedula {cedula} fue actualizado con exito")
    else: 
        print(f"La cedula {cedula} no se encuentra registrada en la base de datos")
  
def eliminar_empleado(db): #D (Delete Eliminación de registro)
    print("*"*20)
    print("* ELIMINAR EMPLEADO *")
    print("*"*20)
    cedula = input("Ingrese la cedula del empleado a eliminar: ")
    if cedula in db:
        del db[cedula]
        print("Empleado eliminado con exito")
    else:
        print(f"El usuario con cedula : {cedula} no fue encontrado")

if __name__ == "__main__":
    limpiar_pantalla()
    with shelve.open('database_empleados', 'w') as db:  #with reeemplaza shelve.open / shelve.close
        while True:
            print("="*30)
            print("Menu de opciones: ")
            print("1. Crear empleado ")
            print("2. Listar empleados")
            print("3. Editar empleado")
            print("4. Eliminar empleado")
            print("5. Salir del programa")
            print("="*30)
            opcion = input("Digita una opción del menu: ")
            if opcion == "1":
                crear_empleado(db)
            elif opcion == "2":
                listar_empleados(db)
            elif opcion == "3":
                actualizar_empleados(db)                                
            elif opcion == "4":
                eliminar_empleado(db)
            elif opcion == "5":
                break
            else:
                print("Opción no válida, por favor digite una opción válida")