import pandas as pd
import os

def carga_datos(ruta):
    """
    Lee el archivo CSV de Airbnb y devuelve un DataFrame.
    (Bloque 1 del diagrama de flujo)
    
    Parámetros
    ---------
    ruta: arcivo CSV
    
    Retorna
    ------
    DataFrame
    Con la información del CSV dividida en las columnas correspondientes.
    
    """
    if not os.path.exists(ruta):
        print(f"Error: No se encontró el archivo en la ruta especificada: {ruta}")
        return None
        
    try:
        df = pd.read_csv(ruta)
        print("Datos cargados exitosamente.")
        return df
    except Exception as e:
        print(f"Error al leer el archivo CSV: {e}")
        return None



