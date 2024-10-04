#Queremos saber el numero de nuevos establecimientos que se han abierto por año y por entidad
import pandas as pd
import statistics as sts
import missingno as msno
import matplotlib.pyplot as plt
import seaborn as sns

s_salud= pd.read_csv("C:/Users/zaira/Desktop/alan/analisis_de_datos/conjunto_de_datos/denue_inegi.csv")
#s_salud.info() #para conocer el tipo de datos
ds_salud = s_salud.copy()
#ds_salud= ds_salud.set_index("id")
ds_salud= ds_salud[["nombre_act", "entidad","fecha_alta"]]
#print(ds_salud["nombre_act"].unique()) #para conocer el tipo de servicio de salud
"""print(ds_salud["fecha_alta"].min()) Obtener el rango de fechas
print(ds_salud["fecha_alta"].max())"""
#print(len(ds_salud["entidad"].unique())) #evitar datos repetidos
#msno.matrix (ds_salud) #esto me permite visualizar si las variables que requiero tienen datos faltantes
#msno.bar(s_salud) #solo para confirmar de modo exacto que no falte ningun dato

#gs_salud= ds_salud.groupby("entidad").count()
#print(gs_salud)
#gs_salud["nombre_act"].plot(kind="bar")# para conocer la distribucion por fecha
#fs_salud= ds_salud.groupby("fecha_alta").count()
#fs_salud["nombre_act"].plot(kind="bar")
ds_salud["conteo"] = [1 for r in range(len(ds_salud["nombre_act"]))]
#pi_salud= pd.pivot_table( ds_salud["nombre_act"],index= ["entidad"], columns=["fecha_alta"],values= ["conteo"])
# Para conocer la distribucion de establecimientos abiertos por año y por identidad
#pivot_df = ds_salud.pivot_table(index="entidad", columns="fecha_alta", values="conteo", aggfunc="sum")
#pivot_df= pivot_df.fillna(0)
#print(pivot_df)
#sns.heatmap(pivot_df, cmap="Blues")
#plt.title("Distribucion de establecimientos abiertos por año y por identidad")
#Para conocer el tipo de establecimiento abierto por entidad
pivot_df2= ds_salud.pivot_table(index= "nombre_act", columns= "entidad", values= "conteo", aggfunc= "sum")
pivot_df2.fillna(0)
#print(pivot_df2)
sns.heatmap(pivot_df2, cmap="Blues")
plt.title("Tipo de establecimiento abierto por entidad")
plt.show()