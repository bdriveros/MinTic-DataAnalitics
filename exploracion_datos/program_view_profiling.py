# Instalamos bibliotecas
import pandas as pd
from pandas_profiling import ProfileReport

# Cargamos el conjunto de datos
df = pd.read_csv('..\data\InventoryLot_v4.csv')

#  Creamos un informe
reporte = ProfileReport(df, title="Reporte de Pandas Profiling")

#  Mostramos el informe
reporte.to_file("Reporte_Pandas_Profiling.html")
