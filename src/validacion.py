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


def validar_precio(precio_str):
    """
    Valida que el presupuesto sea un número entero positivo.

    Argumentos:
        precio_str (str): El presupuesto ingresado por el usuario como texto.

    Retorna:
        bool: True si es válido, False si no lo es.
    """
    if not precio_str.isdigit() or int(precio_str) <= 0:
        print(" Dato inválido: el presupuesto debe ser un número entero positivo (sin letras ni símbolos).")
        return False
    return True


def validar_noches(noches_str):
    """
    Valida que la cantidad de noches sea un número entero positivo.

    Argumentos:
        noches_str (str): Las noches ingresadas por el usuario como texto.

    Retorna:
        bool: True si es válido, False si no lo es.
    """
    if not noches_str.isdigit() or int(noches_str) <= 0:
        print(" Dato inválido: la cantidad de noches debe ser un número entero positivo.")
        return False
    return True


def validar_barrio(barrio, barrios_validos):
    """
    Valida que el barrio ingresado exista en el CSV de Airbnb.

    Argumentos:
        barrio (str): El barrio ingresado por el usuario.
        barrios_validos (list): Lista de barrios reales extraídos del CSV.

    Retorna:
        bool: True si es válido, False si no lo es.
    """
    if barrio.strip().lower() not in [b.lower() for b in barrios_validos]:
        print(f" Dato inválido: el barrio '{barrio}' no existe en el registro de CABA.")
        return False
    return True
