
def carga_preferencias_usuario(df):
    """
    Solicita al usuario sus preferencias de hospedaje en CABA por medio de la consola.
    
    Combina entradas de texto manuales para campos abiertos (barrio, presupuesto, 
    noches y huéspedes) con un menú numérico interactivo que simula un desplegable 
    para la selección del tipo de alojamiento. Las opciones del menú se extraen 
    dinámicamente de la columna 'room_type' del DataFrame recibido.
    
    Parámetros:
        df (pd.DataFrame): DataFrame con los datos de Airbnb, debe contener
                           la columna 'room_type'.
    
    Retorna:
        dict: Un diccionario con las preferencias capturadas, donde las llaves 
              corresponden a las columnas técnicas del archivo de datos:
              - 'neighbourhood': Nombre del barrio (str).
              - 'precio': Presupuesto máximo (str, aún sin validar).
              - 'minimum_nights': Cantidad de noches (str, aún sin validar).
              - 'room_type': Tipo de habitación tal como figura en el CSV (str).
    """
    barrio = input(" ¿En qué barrio de CABA te quieres hospedar?: ").strip()
    precio_max = input(" ¿Cuál es tu presupuesto máximo por noche (en USD)?: ").strip()
    noches = input(" ¿Cuántas noches te vas a quedar?: ").strip()
<<<<<<< Updated upstream
  
    print("[Menú Desplegable: Tipo de Alojamiento]")
    print(" 1. Casa o Departamento entero")
    print(" 2. Habitación privada")
    print(" 3. Habitación compartida")
    print(" 4. Habitación de hotel")
    
    opcion = input("Selecciona introduciendo el número (1, 2, 3 o 4): ").strip()
    
   
    if opcion == "1":
        tipo_alojamiento = "Entire home/apt"
    elif opcion == "2":
        tipo_alojamiento = "Private room"
    elif opcion == "3":
        tipo_alojamiento = "Shared room"
    elif opcion == "4":
        tipo_alojamiento = "Hotel room"
    else:
        tipo_alojamiento = "Entire home/apt"
        
=======

    # 2. Extraer opciones únicas de room_type desde el DataFrame
    opciones = df["room_type"].dropna().unique().tolist()

    # 3. Mostrar menú dinámico
    print("\n[Menú Desplegable: Tipo de Alojamiento]")
    for i, opcion in enumerate(opciones, start=1):
        print(f" {i}. {opcion}")

    # 4. Validar selección dentro del rango disponible
    while True:
        seleccion = input(f"Selecciona introduciendo un número (1-{len(opciones)}): ").strip()
        if seleccion.isdigit() and 1 <= int(seleccion) <= len(opciones):
            tipo_alojamiento = opciones[int(seleccion) - 1]
            break
        else:
            print(f" Opción inválida. Ingresá un número entre 1 y {len(opciones)}.")

    # 5. Diccionario final con las llaves exactas del CSV
>>>>>>> Stashed changes
    preferencias = {
        "neighbourhood": barrio,
        "price": precio_max,
        "minimum_nights": noches,
        "room_type": tipo_alojamiento
    }

    print(" ¡Preferencias guardadas con éxito!")
    return preferencias
