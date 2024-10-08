#Queremos saber el numero de nuevos establecimientos que se han abierto por año y por entidad

import pandas as pd
import statistics as sts
import missingno as msno
import matplotlib.pyplot as plt
import seaborn as sns
s_salud= pd.read_csv("C:/Users/zaira/Desktop/alan/analisis_de_datos/conjunto_de_datos/denue_inegi.csv")
ds_salud= s_salud[["nombre_act", "entidad","fecha_alta"]]
ds_salud =ds_salud.copy()
gs_salud= ds_salud.groupby("entidad").count()
fs_salud= ds_salud.groupby("fecha_alta").count()
fs_salud = fs_salud.sort_values (by= "nombre_act", ascending= False)
ds_salud["conteo"] = 1
pivot_df = ds_salud.pivot_table(index="entidad", columns="fecha_alta", values="conteo", aggfunc="sum")
pivot_df= pivot_df.fillna(0)
pivot_df2= ds_salud.pivot_table(index= "nombre_act", columns= "entidad", values= "conteo", aggfunc= "sum")
pivot_df2.fillna(0)
por_act= ds_salud["nombre_act"].value_counts(normalize=True)



def menu_p():
    print("\n1. Selección de datos")
    print("2. Limpieza de datos")
    print("3. Estadísticos básicos")
    print("4. Agrupación de datos")
    print("5. Generar tablas con datos agrupados")
    return input("Escribe el número de la opción que deseas: ")

while True:
    menu = menu_p()
    
    if menu == "1":
        while True: 
                print("\n1. Información general de los datos")
                print("2. Selección de datos")
                print("3. Regresar al menú principal")
                sub_menu = input("Escribe el número de la opción que deseas: ")
                if sub_menu == "1":
                        print("Los tipos de datos son : \n")
                        s_salud.info()
                        print(f"La lista de servicios es: \n {ds_salud["nombre_act"].unique()}") 
                        print(f"El rango de fechas es de: {ds_salud["fecha_alta"].min()} a {ds_salud['fecha_alta'].max()}") 
                        break
                elif sub_menu == "2":
                        print("\nLos datos selccionados para esta revisiòn fueron: fecha en que se dio de alta el establecimiento,\n el nombre de la actividad realizada en el establecimiento y su ubicaciòn por estado.")
                        break
                elif sub_menu == "3":
                        break
                else:
                      print(f"\nLa opción {sub_menu} no existe")  

    elif menu == "2":
        while True: 
            print("\n1. Revisión de necesidad de limpieza de datos")
            print("2. Regresar al menú principal")
            sub_menu = input("Escribe el número de la opción que deseas: ")
            if sub_menu == "1":
                print(f"\n El listado de estados tiene una extensiòn de : {len(ds_salud["entidad"].unique())} estados") #evitar datos repetidos
                msno.matrix (s_salud) #esto me permite visualizar si las variables que requiero tienen datos faltantes
                plt.show()
                msno.bar(ds_salud) #solo para confirmar de modo exacto que no falte ningun dato
                plt.show()
                print("En este caso no fue necesaria la limpieza da datos")
                break
            elif sub_menu == "2":
                break  
            else:
                print(f"\nLa opción {sub_menu} no existe")

    elif menu == "3":
        while True:  
            print("\n1. Generar estadísticos básicos")
            print("2. Regresar al menú principal")
            sub_menu = input("Escribe el número de la opción que deseas: ")
            if sub_menu == "1":
                print(ds_salud)
                print(f"Los estadisticos basicos de ds_salud : \n {ds_salud[["nombre_act", "entidad","fecha_alta"]].describe()}")
                break
            if sub_menu == "2":
                break 
            else:
                print(f"\nLa opción {sub_menu} no existe")

    elif menu == "4":
        while True:  
                print("\n1. Agrupación por entidad")
                print("2. Agrupación por fecha de alta")
                print("3. Establecimientos abiertos por año y por identidad")
                print("4. Establecimientos abiertos por entidad")
                print("5. Distribución en porcentajes de los centros por actividad realizada")
                print("6. Regresar al menú principal")
                sub_menu = input("Escribe el número de la opción que deseas: ")
                if sub_menu == "1":
                        print(gs_salud)
                        break
                elif sub_menu == "2":
                        print(fs_salud)
                        break
                elif sub_menu == "3":
                        print(pivot_df)
                        break
                elif sub_menu == "4":
                        print(pivot_df2)
                        break
                elif sub_menu == "5":
                        print(por_act)
                        break
                elif sub_menu == "6":
                        break 
                else:
                        print(f"\nLa opción {sub_menu} no existe")

    elif menu == "5":
        while True:  
                print("\n1. Gráfica de distribución por entidad")
                print("2. Gráfica de distribución por fecha")
                print("3. Mapa de calor de distribución por año y por identidad")
                print("4. Mapa de calor de establecimientos abiertos por entidad")
                print("5. Gráfica de porcentajes de los centros por actividad realizada")
                print("6. Regresar al menú principal")
                sub_menu = input("Escribe el número de la opción que deseas: ")
                if sub_menu == "1":
                        ax= gs_salud["nombre_act"].plot(kind="bar")
                        for p in ax.patches:
                                ax.annotate(str(p.get_height()), (p.get_x() * .95, p.get_height() * 1.01)) 
                        plt.title("Gráfica de distribución por entidad", pad= 30)
                        plt.show()
                        break
                elif sub_menu == "2":
                        ax= fs_salud["nombre_act"].plot(kind="bar") 
                        for p in ax.patches:
                                ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() + 1.1)) 
                        plt.title("Gráfica de distribución por fecha")
                        plt.show()
                        break
                      
                elif sub_menu == "3":
                        sns.heatmap(pivot_df, cmap="Blues")
                        plt.title("Distribucion de establecimientos abiertos por año y por identidad")
                        plt.show()
                        break
                elif sub_menu == "4": 
                        sns.heatmap(pivot_df2 ,cmap="Blues")
                        plt.title("Tipo de establecimiento abierto por entidad", pad= 10)
                        plt.xticks(rotation=45, ha="right", fontsize=7)
                        plt.yticks(fontsize=7)
                        plt.subplots_adjust(left=0.514)
                        plt.show()
                        break
                elif sub_menu == "":
                        por_act.plot(kind="bar")
                        plt.xticks(rotation=40, ha="right", fontsize=6)
                        plt.ylabel("Porcentaje")
                        plt.title("Distribuciòn en porcentajes de los centros por actividad realizada", pad= 20)
                        plt.subplots_adjust(bottom=0.2)
                        plt.show() 
                        break                 
                if sub_menu == "6":
                        break  
                else:
                      print(f"\nLa opción {sub_menu} no existe")

    else:
        print(f"\nLa opción {menu} no existe")
