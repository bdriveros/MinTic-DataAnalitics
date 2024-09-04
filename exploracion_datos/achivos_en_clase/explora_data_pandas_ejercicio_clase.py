import pandas as pd

df = pd.read_csv('..\data\Order_v3.csv',encoding='latin-1')
#'.\data\Order_v3.csv',encoding='latin-1'
#df = pd.read_csv('..\data\SupplyPlan_v2.csv')
print(df)
#print(df.dtypes)
#print(df.columns)