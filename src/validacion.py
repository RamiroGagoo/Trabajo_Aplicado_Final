# src/preferencias.py

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

    # 1. Validar el Precio (Debe ser un número entero mayor a 0)
    precio_str = preferencias["price"]
    if not precio_str.isdigit() or int(precio_str) <= 0:
        print(" Error: El presupuesto máximo debe ser un número entero positivo (sin letras ni símbolos).")
        return False

    # 2. Validar las Noches Mínimas (Debe ser un número entero mayor a 0)
    noches_str = preferencias["minimum_nights"]
    if not noches_str.isdigit() or int(noches_str) <= 0:
        print("Error: La cantidad de noches debe ser un número entero positivo.")
        return False

    # 3. Validar el Barrio (Ignorando si el usuario escribió con mayúsculas o minúsculas)
    barrio_usuario = preferencias["neighbourhood"].strip().lower()
    
    # Pasamos toda la lista de barrios válidos del CSV a minúsculas para comparar fácil
    barrios_csv_minuscula = [b.lower() for b in barrios_validos]
    
    if barrio_usuario not in barrios_csv_minuscula:
        print(f"Error: El barrio '{preferencias['neighbourhood']}' no existe en el registro de CABA.")
        return False

    # ==========================================
    # 🎉 ¡PASO PRO DE TRANSFORMACIÓN PARA PANDAS!
    # ==========================================
    # Si el código llegó hasta acá, significa que todos los datos son perfectos.
    # Ahora transformamos los textos ("2", "15000") en números reales (2, 15000) 
    # para que Pandas pueda hacer operaciones matemáticas de menor/mayor.
    
    preferencias["price"] = int(precio_str)
    preferencias["minimum_nights"] = int(noches_str)
  
    # Además, le devolvemos al diccionario el nombre del barrio con las mayúsculas 
    # prolijas del CSV (Ej: si el usuario escribió "palermo", lo corrige a "Palermo")
    posicion = barrios_csv_minuscula.index(barrio_usuario)
    preferencias["neighbourhood"] = barrios_validos[posicion]

    print("¡Todas las preferencias son válidas y preparadas para Pandas!")
    return True#validacion 
