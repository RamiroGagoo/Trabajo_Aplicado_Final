
def promedio_precio(df_barrio):
    """
    Calcula el precio promedio de los hospedajes de un barrio.

    Parámetro:
        df_barrio (DataFrame): listings ya filtrados por barrio,
                               con columna 'price' numérica y limpia.
    Devuelve:
        float: promedio de precio, redondeado a 2 decimales.
               Devuelve None si el DataFrame está vacío.
    """
    if df_barrio.empty:
        return None
    return round(df_barrio["price"].mean(), 2)


def min_noches(df_barrio):
    """
    Devuelve la menor cantidad mínima de noches requerida
    entre todos los hospedajes del barrio.

    Parámetro:
        df_barrio (DataFrame): listings ya filtrados por barrio,
                               con columna 'minimum_nights' numérica.
    Devuelve:
        int: el mínimo de minimum_nights del barrio.
             Devuelve None si el DataFrame está vacío.
    """
    if df_barrio.empty:
        return None
    return int(df_barrio["minimum_nights"].min())


def max_noches(df_barrio):
    """
    Devuelve la mayor cantidad máxima de noches permitida
    entre todos los hospedajes del barrio.

    Parámetro:
        df_barrio (DataFrame): listings ya filtrados por barrio,
                               con columna 'maximum_nights' numérica.
    Devuelve:
        int: el máximo de maximum_nights del barrio.
             Devuelve None si el DataFrame está vacío.
    """
    if df_barrio.empty:
        return None
    return int(df_barrio["availability_365"].max())