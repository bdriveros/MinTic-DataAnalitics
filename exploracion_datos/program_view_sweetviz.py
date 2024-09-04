# Instalamos bibliotecas
import pandas as pd
import sweetviz as sv

# Cargamos el conjunto de datos
df = pd.read_csv('..\data\InventoryLot_v4.csv')

#  Creamos un informe
reporte =sv.analyze(df)

#  Mostramos el informe
reporte.show_html('reporte_InventoryLot.html')