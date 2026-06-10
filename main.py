# main
import pandas as pd
from src.carga_datos_pandas import carga_datos
from src.procesamiento_datos import limpiar_precio, filtrar_datos, filtrado_por_barrio
from src.comparaciones import buscar_compatibles
from src.carga_de_preferencias_del_usuario import carga_preferencias_usuario
from graficos.Grafico_segun_preferencias_del_usuario import crear_mapa

ruta = "datos/airbnb2.csv"

df = carga_datos(ruta)

if df is not None:

    df = limpiar_precio(df)

    df = filtrar_datos(df)

    df["latitude"] = pd.to_numeric(df["latitude"], errors="coerce") 
    df["longitude"] = pd.to_numeric(df["longitude"], errors="coerce")

    preferencias = carga_preferencias_usuario(df)

    preferencias["precio"] = float(preferencias["precio"])
    preferencias["minimum_nights"] = int(preferencias["minimum_nights"])

    df_barrio = filtrado_por_barrio(preferencias, df)

    df_filtrado = buscar_compatibles(df_barrio, preferencias)

    if df_filtrado is None or len(df_filtrado) == 0:
        print("No se encontraron alojamientos compatibles.")
    else:
        mapa = crear_mapa(df_filtrado)
        mapa.show_in_browser()

        print("Mapa generado correctamente.")
