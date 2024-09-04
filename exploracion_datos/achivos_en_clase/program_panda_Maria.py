import pandas as pd
import os

dir_path = os.path.dirname(os.path.realpath(__file__))  #almacenará la ruta del directorio en el que se encuentra el script que se está ejecutando.
#path_to_csv = os.path.join(dir_path, "..", "DemandPlan_v1.csv") #Va al archivo .csv que deseamos a partir de la ubicacion del presente script

while True:
    print("#"*30)
    print("¿Qué archivo deseas explorar?: ")
    print("1. Catalog_v2")
    print("2. DemandPlan_v1")
    print("3. Inventory_v2")
    print("4. Location_v3")
    print("5. Salir del programa")
    print("#"*30)
    opcion = input("Digita una opción del menú: ")           

    if opcion == "1":
        path_to_csv = os.path.join(dir_path, "..", "Catalog_v2.csv")
        break
    elif opcion == "2":
        path_to_csv = os.path.join(dir_path, "..", "DemandPlan_v1.csv")
        break
    elif opcion == "3":
        path_to_csv = os.path.join(dir_path, "..", "Inventory_v2.csv")
        break
    elif opcion == "4":
        path_to_csv = os.path.join(dir_path, "..", "Location_v3.csv")
        break
    elif opcion == "5":
        break
    else:
        print("Opción no válida, por favor digite una opción válida")

if opcion != "5":
    filename = os.path.basename(path_to_csv)
    if os.path.isfile(path_to_csv):
        print("*"*30)
        print(f"Qué datos deseas explorar del archivo {filename}")
        print("1. Primeras filas")
        print("2. Últimas filas")
        print("3. Columnas")
        print("4. Tipo de datos")
        print("5. Información detallada de las columnas")
        print("6. Resumen estadistico descriptivo")
        print("*"*30)
        df = pd.read_csv(path_to_csv)
        explorar = input("Digita una opción del menú: ")

        if opcion == "1":
            print(df.head())
        elif opcion == "2":
            print(df.tail())
        elif opcion == "3":
            print(df.columns)
        elif opcion == "4":
            print(df.dtypes)
        elif opcion == "5":
            print(df.info())
        elif opcion == "6":
            print(df.describe())
        else:
            print("Opción no válida, por favor digite una opción válida")
        #print(df.head()) #Imprimir las primeras líneas
        #print(df.tail()) #Muestra las últimas filas del df
        #print(df) #Imprime todo el df
        #print(df.loc[:,:]) #Imprimir todo el df
        #print(df.columns)   #imprimir columnas del df
        #print(df.dtypes)    #Imprimir tipo de datos objects(Pandas cadena de texto)
        #print(df.info())    #Imprime información detallada de las columnas
        #print(df.describe())    #Imprime resumen estadistico descriptivo del csv
    else:
        print(f"Archivo {path_to_csv} no encontrado")