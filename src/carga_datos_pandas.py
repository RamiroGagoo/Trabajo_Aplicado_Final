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

def validar_dataframe(df):
    """
    Chequea columnas, tipos y nulos.
    Muestra un aviso al usuario en caso de errores en el CSV.
    (Bloque 2 del diagrama de flujo)
    
    Parámetros
    ---------
    df: DataFrame
    """
    if df is None or df.empty:
        print("Aviso: El DataFrame está vacío o es nulo.")
        return False

columnas_esperadas = ['neighbourhood', 'price', 'minimum_nights', 'room_type', 'availability_365']

