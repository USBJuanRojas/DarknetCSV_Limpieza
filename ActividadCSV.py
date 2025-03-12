import pandas as pd

df = pd.read_csv("C:/Users/jroja/OneDrive/Documents/big data/Actividad2/Darknet.csv")
df1=df.dropna()
df2=df


# print(len(df1))
# print(len(df))
# print(len(df2))
# print(len(df)-len(df1))
# print(df.info())

def tiempo():
    df2["Timestamp"]=pd.to_datetime(df2["Timestamp"])
    print(df2.columns)
    print(df2.info())

def transformacion():
    for columna in df2.columns:
        try:
            df2[columna] = pd.to_numeric(df2[columna])
            df2[columna].fillna(0, inplace=True)
        except:
            df2[columna] = df2[columna].astype(str)
            df2[columna].fillna("Juan", inplace=True)
    
    print(df2.describe())

transformacion()
tiempo()
print(df2.info())
df2.to_csv("C:/Users/jroja/OneDrive/Documents/big data/Actividad2/Darknet2.csv", index=False)