import os
import webbrowser
import pandas as pd

def crear_tabla_html(df, nombre_archivo="tabla_alojamientos.html"):
    """
    Genera una tabla HTML estilizada con los alojamientos disponibles 
    y la abre en el navegador web por defecto.
    
    Parámetros:
        df (pd.DataFrame): DataFrame con los alojamientos filtrados.
        nombre_archivo (str): Nombre del archivo HTML a generar.
    """
    if df is None or df.empty:
        print("No hay datos para mostrar en la tabla.")
        return

    columnas_interes = {
        'name': 'Nombre del Alojamiento',
        'room_type': 'Tipo de Habitación',
        'precio': 'Precio por Noche ($)',
        'minimum_nights': 'Noches Mínimas',
        'number_of_reviews': 'Reseñas Totales',
        'review_scores_rating': 'Puntuación'
    }
    
    columnas_validas = {col: nom for col, nom in columnas_interes.items() if col in df.columns}
    df_tabla = df[list(columnas_validas.keys())].rename(columns=columnas_validas)

    estilos_css = """
    <style>
        body { font-family: Arial, sans-serif; margin: 30px; background-color: #f8f9fa; }
        h2 { color: #333; text-align: center; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; background-color: #fff; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }
        th, td { padding: 12px 15px; text-align: left; border-bottom: 1px solid #ddd; }
        th { background-color: #007bff; color: white; text-transform: uppercase; font-size: 14px; }
        tr:hover { background-color: #f1f1f1; }
        .contenedor { max-width: 1200px; margin: auto; }
    </style>
    """

    tabla_html = df_tabla.to_html(index=False, classes="tabla-alojamientos")

    html_final = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Alojamientos Disponibles</title>
        {estilos_css}
    </head>
    <body>
        <div class="contenedor">
            <h2>🏠 Alojamientos Encontrados según tus Preferencias</h2>
            {tabla_html}
        </div>
    </body>
    </html>
    """

    ruta_completa = os.path.abspath(nombre_archivo)
    with open(ruta_completa, "w", encoding="utf-8") as f:
        f.write(html_final)

    webbrowser.open(f"file://{ruta_completa}")
    print("Tabla de alojamientos generada y abierta en el navegador.")