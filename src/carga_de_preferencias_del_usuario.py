
# src/preferencias.py

def carga_preferencias_usuario():
    """

    Solicita al usuario sus preferencias de hospedaje en CABA por medio de la consola.
    
    Combina entradas de texto manuales para campos abiertos (barrio, presupuesto, 
    noches y huéspedes) con un menú numérico interactivo que simula un desplegable 
    para la selección del tipo de alojamiento. Además, realiza un mapeo (traducción) 
    interno de la opción elegida a su equivalente en inglés para mantener la 
    compatibilidad directa con el dataset original de Airbnb.

    Retorna:
        dict: Un diccionario con las preferencias capturadas, donde las llaves 
              corresponden a las columnas técnicas del archivo de datos:
              - 'neighbourhood': Nombre del barrio (str).
              - 'price': Presupuesto máximo (str, aún sin validar).
              - 'minimum_nights': Cantidad de noches (str, aún sin validar).
              - 'accommodates': Cantidad de personas (str, aún sin validar).
              - 'room_type': Tipo de habitación traducido al inglés (str).

    """
    # 1. Inputs manuales
    barrio = input(" ¿En qué barrio de CABA te quieres hospedar?: ").strip()
    precio_max = input(" ¿Cuál es tu presupuesto máximo por noche (en USD)?: ").strip()
    noches = input(" ¿Cuántas noches te vas a quedar?: ").strip()
  
    # 2. Tu menú de opciones fijas en la consola
    print("[Menú Desplegable: Tipo de Alojamiento]")
    print(" 1. Casa o Departamento entero")
    print(" 2. Habitación privada")
    print(" 3. Habitación compartida")
    print(" 4. Habitación de hotel")
    
    opcion = input("Selecciona introduciendo el número (1, 2, 3 o 4): ").strip()
    
    # 3. TU TRADUCTOR DIRECTO A INGLÉS
    # Mapeamos el número elegido al término exacto del CSV original
    if opcion == "1":
        tipo_alojamiento = "Entire home/apt"
    elif opcion == "2":
        tipo_alojamiento = "Private room"
    elif opcion == "3":
        tipo_alojamiento = "Shared room"
    elif opcion == "4":
        tipo_alojamiento = "Hotel room"
    else:
        # Tu red de seguridad por si ponen cualquier otra cosa
        #manejo de error
        tipo_alojamiento = "Entire home/apt"
        
    # 4. El diccionario final con las llaves exactas del CSV
    preferencias = {
        "neighbourhood": barrio,
        "precio": precio_max,
        "minimum_nights": noches,
        "room_type": tipo_alojamiento
    }
    
    print(" ¡Preferencias guardadas con éxito!")
    return preferencias

