# src/comparaciones.py

def tipo_de_hospedaje(hospedaje, preferencia_hospedaje):
    """
    Verifica si el tipo de hospedaje coincide con la preferencia del usuario.

    Parámetros:
        hospedaje (pd.Series): una fila del DataFrame de listings,
                               representa un hospedaje individual.
        preferencia_hospedaje (str): tipo deseado por el usuario, 
                                     ej: "Entire home/apt", "Private room".
    Devuelve:
        bool: True si el room_type del hospedaje coincide con la preferencia.
    """
    return hospedaje["room_type"].strip().lower() == preferencia_hospedaje.strip().lower()


def precio(hospedaje, preferencia_precio):
    """
    Verifica si el precio del hospedaje está dentro del presupuesto del usuario.

    Parámetros:
        hospedaje (pd.Series): una fila del DataFrame de listings,
                               representa un hospedaje individual.
        preferencia_precio (float): precio máximo que el usuario quiere pagar por noche.
    Devuelve:
        bool: True si el precio del hospedaje es menor o igual al máximo.
    """
    return hospedaje["price"] <= preferencia_precio


def cant_noches(hospedaje, cant_noches_usuario):
    """
    Verifica si la cantidad de noches del usuario está dentro del rango
    aceptado por el hospedaje (entre minimum_nights y maximum_nights).

    Parámetros:
        hospedaje (pd.Series): una fila del DataFrame de listings,
                               representa un hospedaje individual.
        cant_noches_usuario (int): cantidad de noches que el usuario quiere quedarse.
    Devuelve:
        bool: True si cant_noches_usuario está entre el mínimo y máximo del hospedaje.
    """
    return hospedaje["minimum_nights"] <= cant_noches_usuario <= hospedaje["maximum_nights"]

def buscar_compatibles(df_barrio, preferencias):
    """
    Recorre todos los hospedajes del barrio y devuelve los que cumplen
    las tres condiciones: tipo, precio y cantidad de noches.

    Parámetros:
        df_barrio (DataFrame): listings ya filtrados por barrio.
        preferencias (dict): diccionario con las preferencias del usuario.
                             Claves esperadas: "room_type", "price", "minimum_nights".
    Devuelve:
        resultados: lista de dicts, cada uno con los datos del hospedaje compatible.
    """
    resultados = []

    for _, hospedaje in df_barrio.iterrows():
        cumple_tipo   = tipo_de_hospedaje(hospedaje, preferencias["room_type"])
        cumple_precio = precio(hospedaje, preferencias["price"])
        cumple_noches = cant_noches(hospedaje, preferencias["minimum_nights"])

        if cumple_tipo and cumple_precio and cumple_noches:
            resultados.append({
                "nombre"    : hospedaje["name"],
                "precio"    : hospedaje["price"],
                "min_noches": hospedaje["minimum_nights"],
                "max_noches": hospedaje["maximum_nights"]
            })

    return resultados