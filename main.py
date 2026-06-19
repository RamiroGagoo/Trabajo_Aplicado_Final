# main
import pandas as pd
from src.carga_datos_pandas import carga_datos
from src.procesamiento_datos import limpiar_precio, filtrar_datos, filtrado_por_barrio
from src.comparaciones import buscar_compatibles
from src.carga_de_preferencias_del_usuario import carga_preferencias_usuario
from docs.Grafico_segun_preferencias_del_usuario import crear_mapa
from docs.tabla_alojamientos import crear_tabla_html

ruta = "data/airbnb2.csv"
df = carga_datos(ruta)

if df is not None:
    try:
        df = limpiar_precio(df)
        df = filtrar_datos(df)
        df["latitude"] = pd.to_numeric(df["latitude"], errors="coerce")
        df["longitude"] = pd.to_numeric(df["longitude"], errors="coerce")
    except Exception as e:
        print(f"Hubo un problema al procesar el archivo de datos. Revisá que el CSV esté completo y bien formateado. Detalle: {e}")
        df = None

if df is not None:
    try:
        preferencias = carga_preferencias_usuario(df)
        preferencias["precio"] = float(preferencias["precio"])
        preferencias["minimum_nights"] = int(preferencias["minimum_nights"])
    except ValueError as e:
        print(f"Los valores ingresados no son válidos. Asegurate de ingresar números en precio y noches. Detalle: {e}")
        preferencias = None
    except Exception as e:
        print(f"Ocurrió un error inesperado al cargar tus preferencias. Detalle: {e}")
        preferencias = None

if df is not None and preferencias is not None:
    try:
        df_barrio = filtrado_por_barrio(preferencias, df)
        if df_barrio is None or len(df_barrio) == 0:
            raise ValueError(f"No encontramos el barrio '{preferencias.get('neighbourhood')}' en nuestros registros. Revisá la ortografía e intentá de nuevo.")
    except ValueError as e:
        print(f"Error: {e}")
        df_barrio = None
    except Exception as e:
        print(f"Ocurrió un error inesperado al buscar el barrio. Detalle: {e}")
        df_barrio = None

if df is not None and preferencias is not None and df_barrio is not None:
    try:
        df_filtrado = buscar_compatibles(df_barrio, preferencias)
    except Exception as e:
        print(f"Ocurrió un error inesperado al buscar alojamientos compatibles. Detalle: {e}")
        df_filtrado = None

    if df_filtrado is None or len(df_filtrado) == 0:
        print(f"\nNo encontramos alojamientos en {preferencias.get('neighbourhood')} que cumplan todas tus condiciones.")
        print("Algunas sugerencias:")
        print("  - Probá aumentar tu presupuesto máximo")
        print("  - Considerá reducir la cantidad de noches")
        print("  - Probá con otro tipo de alojamiento")
    else:
        barrio = preferencias.get("neighbourhood", "el barrio elegido")
        cantidad = len(df_filtrado)
        precio_prom = round(df_filtrado["precio"].mean(), 2)
        precio_min = df_filtrado["precio"].min()
        precio_max = df_filtrado["precio"].max()
        noches_min = int(df_filtrado["minimum_nights"].min())
        print(f"\n En {barrio} encontramos {cantidad} alojamiento(s) que se ajustan a "
              f"tus preferencias. El precio promedio por noche es de ${precio_prom}, "
              f"con un rango que va desde ${precio_min} hasta ${precio_max}. "
              f"La estadía mínima requerida en esta zona es de {noches_min} noche(s).\n")
        print("Para ver la tabla con los datos hay que cerrar el mapa y frenar el programa.")
        try:
            mapa = crear_mapa(df_filtrado)
            mapa.save("outputs/mapa.html")
            mapa.show_in_browser()
            print("Mapa generado correctamente.")
            crear_tabla_html(df_filtrado)
        except Exception as e:
            print(f"No se pudo generar el mapa o la tabla.  Detalle: {e}")
            
