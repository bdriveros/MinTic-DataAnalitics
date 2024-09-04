import pandas as pd
import sweetviz as sv

df = pd.read_csv('..\data\InventoryLot_v4.csv')
reporte =sv.analyze(df)
reporte.show_html('reporte_InventoryLot.html')