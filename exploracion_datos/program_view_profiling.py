import pandas as pd
from pandas_profiling import ProfileReport

df = pd.read_csv('..\data\InventoryLot_v4.csv')
reporte = ProfileReport(df, title="Reporte de Pandas Profiling")
reporte.to_file("Reporte_Pandas_Profiling.html")
