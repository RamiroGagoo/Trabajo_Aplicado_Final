import folium

def crear_mapa(df):
    """
    Descripción: Crea un mapa con los alojamientos.
    Parámetros: df (DataFrame)
    Retorno: mapa (folium)
    """

    mapa = folium.Map(location=[-34.60, -58.44], zoom_start=12)

    for i, fila in df.iterrows():
        lat = fila["latitude"]
        lon = fila["longitude"]

        folium.Marker(
            location=[lat, lon]
        ).add_to(mapa)

    return mapa