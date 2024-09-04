import pandas as pd  #Importando libreria pandas con alias

df = pd.read_csv('..\data\InventoryLot_v4.csv') # Cargamos archivo df (Data Frame)

#print(df.head()) #Imprimir muestra de datos
#print(df.tail()) #Muestra las ultimas filas del df
#print(df) # Imprimir todo el df
#print(df.loc[:, :]) # Imprimir todo el df
#print(df.columns) #Imprimir columnas del df
#print(df.shape) #La shape propiedad devuelve una tupla que contiene la forma del DataFrame.
#print(df.dtypes) #Imprimir tipos de datos object(Pandas cadena de texto)
#print(df.info()) #Imprime información detallada de columnas
print(df.describe()) #mostramos estadísticas descriptivas del csv 
