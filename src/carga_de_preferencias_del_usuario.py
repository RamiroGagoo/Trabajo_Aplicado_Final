from src.validacion import validar_barrio, validar_precio, validar_noches


def carga_preferencias_usuario(df):
    """
    Solicita al usuario sus preferencias de hospedaje en CABA por medio de la consola.
    
    Combina entradas de texto manuales para campos abiertos (barrio, presupuesto, 
    noches y huéspedes) con un menú numérico interactivo que simula un desplegable 
    para la selección del tipo de alojamiento. Las opciones del menú se extraen 
    dinámicamente de la columna 'room_type' del DataFrame recibido.
    
    Parámetros:
        df (pd.DataFrame): DataFrame con los datos de Airbnb, debe contener
                           las columnas 'room_type' y 'neighbourhood'.
    
    Retorna:
        dict: Un diccionario con las preferencias capturadas y validadas, donde las llaves 
              corresponden a las columnas técnicas del archivo de datos:
              - 'neighbourhood': Nombre del barrio (str).
              - 'precio': Presupuesto máximo (int, ya validado).
              - 'minimum_nights': Cantidad de noches (int, ya validado).
              - 'room_type': Tipo de habitación tal como figura en el CSV (str).
    """
    opciones = df["room_type"].dropna().unique().tolist()
    barrios_validos = df["neighbourhood"].dropna().unique().tolist()
    barrios_minuscula = [b.lower() for b in barrios_validos]

    # 1. Barrio
    while True:
        barrio = input(" ¿En qué barrio de CABA te quieres hospedar?: ").strip()
        if validar_barrio(barrio, barrios_validos):
            posicion = barrios_minuscula.index(barrio.lower())
            barrio = barrios_validos[posicion]
            break

    # 2. Precio
    while True:
        precio_max = input(" ¿Cuál es tu presupuesto máximo por noche (en pesos argentinos)?: ").strip()
        if validar_precio(precio_max):
            precio_max = int(precio_max)
            break

    # 3. Noches
    while True:
        noches = input(" ¿Cuántas noches te vas a quedar?: ").strip()
        if validar_noches(noches):
            noches = int(noches)
            break

    # 4. Tipo de alojamiento
    print("\n[Menú Desplegable: Tipo de Alojamiento]")
    for i, opcion in enumerate(opciones, start=1):
        print(f" {i}. {opcion}")

    while True:
        seleccion = input(f" Selecciona introduciendo un número (1-{len(opciones)}): ").strip()
        if seleccion.isdigit() and 1 <= int(seleccion) <= len(opciones):
            tipo_alojamiento = opciones[int(seleccion) - 1]
            break
        else:
            print(f" Dato inválido: ingresá un número entre 1 y {len(opciones)}.")

    preferencias = {
        "neighbourhood": barrio,
        "precio": precio_max,
        "minimum_nights": noches,
        "room_type": tipo_alojamiento
    }

    print(" ¡Preferencias guardadas con éxito!")
    return preferencias