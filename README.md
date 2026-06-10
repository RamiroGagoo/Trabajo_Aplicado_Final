# Trabajo_Aplicado_Final
Participantes: Victoria Fagalde, Camila D'Albora, Martina Sergi, Delfina Puiggari y Ramiro Gago

Trabajo Aplicado — Análisis de Airbnb en CABA
El propósito de este proyecto es diseñar un programa que procese y analice datos de alojamientos de Airbnb en la Ciudad Autónoma de Buenos Aires, con el objetivo de encontrar patrones de precios, zonas más demandadas y factores que influyen en la valoración de los alojamientos. El programa recibe un archivo CSV descargado de Inside Airbnb con datos reales de listings (precio, barrio, tipo de alojamiento, reviews, disponibilidad, entre otros), procesa y limpia esa información, y finalmente presenta al usuario tablas resumen y gráficos comparativos según sus preferencias personales.

Errores y validaciones:
Un primer error que identificamos fue la posibilidad de que el archivo CSV no se encuentre en la ruta indicada o que esté vacío. Para evitar ese error, implementamos bloques try/except que capturan el FileNotFoundError y el ValueError, informando al usuario con un mensaje claro y deteniendo la ejecución de forma controlada.

Un segundo error que identificamos fue la posibilidad de que el usuario ingrese preferencias inválidas, como un precio negativo, una cantidad de noches igual a cero, o un barrio que no existe en el dataset. Para esto implementamos validaciones con raise ValueError dentro de las funciones correspondientes, que interrumpen el flujo y le indican al usuario exactamente qué dato es incorrecto.

Un tercer caso que contemplamos es cuando ningún alojamiento cumple con todas las preferencias ingresadas por el usuario. En ese caso, el programa no falla sino que muestra un mensaje de sugerencia indicando qué parámetro podría modificarse (por ejemplo, aumentar el precio máximo o considerar barrios cercanos).


Estructura del proyecto:
El proyecto está organizado de la siguiente manera:
main.py — Punto de entrada del programa.
requirements.txt — Lista de librerías necesarias para ejecutarlo.
src/ — Carpeta con los módulos internos:
carga.py — Carga y validación del CSV.
usuario.py — Entrada y validación de las preferencias del usuario.
analisis.py — Métricas, comparaciones y filtros.
graficos.py — Generación de gráficos y tablas.
datos/ — Carpeta donde debe guardarse el archivo airbnb.csv descargado de Inside Airbnb.
diseño/ — Carpeta que contiene el diagrama de flujo del programa.



Guía de ejecución:
Para correr el programa, el usuario debe seguir los siguientes pasos:
Clonar el repositorio o descargar los archivos del proyecto.
Instalar las librerías necesarias ejecutando en la terminal:
pip install -r requirements.txt
Nota: Si el mapa no se visualiza correctamente, verificar que la librería folium esté instalada.
En ese caso, ejecutar:
pip install folium
El programa generará un mapa interactivo con los alojamientos compatibles, el cual se abrirá automáticamente en el navegador del usuario.

Descargar el dataset de Inside Airbnb( http://insideairbnb.com/get-the-data/ ) (seleccionar Buenos Aires) y guardarlo como datos/airbnb.csv.
Desde la raíz del repositorio, ejecutar python main.py
El programa pedirá al usuario que ingrese sus preferencias: barrio, precio máximo, cantidad de noches y tipo de hospedaje.
Una vez ingresadas las preferencias, se mostrarán los resultados en forma de tabla y gráficos.

Librerías utilizadas:
Se utilizaron dos librerías externas en este proyecto: 
pandas: Se usa para la carga, limpieza y procesamiento del archivo CSV. 
matplotlib: Se usa para la generación de los gráficos y visualizaciones que se le presentan al usuario.
folium: Se usa para la visualización geográfica de los alojamientos en un mapa interactivo.
Dataset:
Se utilizan datos públicos de Inside Airbnb, que publica periódicamente información de los listings disponibles en distintas ciudades del mundo. El archivo contiene datos como precio, barrio, tipo de alojamiento, cantidad de reviews y disponibilidad, entre otros.
El archivo CSV no está incluido en este repositorio por su tamaño. Debe descargarse manualmente desde el sitio de Inside Airbnb.


