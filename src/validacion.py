
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
        return True

columnas_esperadas = ['neighbourhood', 'precio', 'minimum_nights', 'room_type', 'availability_365']

def validar_preferencias(preferencias, barrios_validos):
    """
    Valida que los datos ingresados en el diccionario de preferencias sean correctos.
    Si todo está bien, convierte los números de texto a tipo entero (int) para Pandas.
    
    Argumentos:
        preferencias (dict): El diccionario que generó tu función de carga.
        barrios_validos (list): Una lista con los nombres de barrios reales que tu compañero 
                                extrae del CSV de Airbnb.
                                
    Retorna:
        bool: True si todo es válido, False si encuentra algún error.
    """

    precio_str = preferencias["price"]
    if not precio_str.isdigit() or int(precio_str) <= 0:
        print(" Error: El presupuesto máximo debe ser un número entero positivo (sin letras ni símbolos).")
        return False

    noches_str = preferencias["minimum_nights"]
    if not noches_str.isdigit() or int(noches_str) <= 0:
        print("Error: La cantidad de noches debe ser un número entero positivo.")
        return False

    barrio_usuario = preferencias["neighbourhood"].strip().lower()
    
    barrios_csv_minuscula = [b.lower() for b in barrios_validos]
    
    if barrio_usuario not in barrios_csv_minuscula:
        print(f"Error: El barrio '{preferencias['neighbourhood']}' no existe en el registro de CABA.")
        return False

    
    preferencias["precio"] = int(precio_str)
    preferencias["minimum_nights"] = int(noches_str)
  
   
    posicion = barrios_csv_minuscula.index(barrio_usuario)
    preferencias["neighbourhood"] = barrios_validos[posicion]

    print("¡Todas las preferencias son válidas y preparadas para Pandas!")
    return True 