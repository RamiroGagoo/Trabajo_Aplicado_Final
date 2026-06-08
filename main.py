#main
from src.carga_datos_pandas import carga_datos
from graficos.Grafico_general import crear_mapa

ruta = "datos/airbnb.csv"

df = carga_datos(ruta)

if df is not None:

    df_mapa = df.sample(100)

    mapa = crear_mapa(df_mapa)
    mapa.save("mapa_alojamientos.html")

    print("Mapa generado correctamente.")