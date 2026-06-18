# Trabajo_Aplicado_Final
Participantes: Victoria Fagalde, Camila D'Albora, Martina Sergi, Delfina Puiggari y Ramiro Gago

Trabajo Aplicado — Análisis de Airbnb en CABA
El propósito de este proyecto es diseñar un programa que procese y analice datos de alojamientos de Airbnb en la Ciudad Autónoma de Buenos Aires, con el objetivo de encontrar patrones de precios, zonas más demandadas y factores que influyen en la valoración de los alojamientos. El programa recibe un archivo CSV descargado de Inside Airbnb con datos reales de listings (precio, barrio, tipo de alojamiento, reviews, disponibilidad, entre otros), procesa y limpia esa información, y finalmente presenta al usuario tablas resumen y gráficos comparativos según sus preferencias personales.

Errores y validaciones
Un primer error que identificamos fue la posibilidad de que el archivo CSV no se encuentre en la ruta indicada o que la carga falle por algún motivo. Para esto, en el main.py se usa un bloque try/except que captura un ValueError si carga_datos devuelve None, y un except Exception genérico para cualquier otro error inesperado durante la lectura del archivo.
Un segundo error que identificamos fue la posibilidad de que, durante la limpieza y el filtrado de datos, no queden filas en el DataFrame (por ejemplo, si todos los precios son inválidos). Para esto se usa un try/except similar: se lanza un ValueError si el DataFrame queda vacío después de limpiar_precio y filtrar_datos, y se captura un Exception para errores no previstos en el procesamiento.
Un tercer error que identificamos fue la posibilidad de que el usuario ingrese preferencias inválidas, como un precio o una cantidad de noches que no sean numéricos. En el main.py, al intentar convertir esos valores con float() e int(), Python lanza automáticamente un ValueError que es capturado por el bloque try/except, mostrándole al usuario un mensaje claro indicando qué dato debe corregir.
Un cuarto caso que contemplamos es la posibilidad de que no haya alojamientos en el barrio elegido por el usuario. Si filtrado_por_barrio devuelve un DataFrame vacío, se lanza un ValueError con un mensaje personalizado indicando que no se encontraron alojamientos en ese barrio.
Finalmente, un quinto caso es cuando ningún alojamiento cumple con todas las preferencias ingresadas (tipo, precio y noches). En ese caso el programa no falla, sino que muestra un mensaje de sugerencia indicando qué parámetro podría modificarse (por ejemplo, aumentar el presupuesto, considerar otra cantidad de noches o probar otro tipo de alojamiento).


Estructura del proyecto:
Estructura del repositorio

- main.py — Punto de entrada del programa, orquesta todas las funciones.
- requirements.txt — Lista de librerías necesarias para ejecutarlo.
- README.md — Este archivo.
- declaracion_ia.md — Declaración de uso de IA.
data/ — Carpeta donde debe guardarse el archivo airbnb2.csv.
src/ — Carpeta con los módulos internos:
- carga_datos_pandas.py — Carga del CSV.
- carga_de_preferencias_del_usuario.py — Entrada de preferencias del usuario.
- comparaciones.py — Funciones de comparación y búsqueda de compatibles.
- metricas.py — Cálculo de métricas del barrio.
- procesamiento_datos.py — Limpieza y filtrado de datos.
- validacion.py — Validación del DataFrame y las preferencias.
docs/ — Carpeta con los módulos de visualización:
- Grafico_segun_preferencias_del_usuario.py — Mapa interactivo con Folium.
- tabla_alojamientos.py — Generación de la tabla HTML de resultados.
outputs/ — Carpeta donde se guardan los archivos generados:
- mapa.html — Mapa interactivo generado por el programa.
- tabla_alojamientos.html — Tabla de resultados generada por el programa.
diseño/ — Carpeta que contiene el diagrama de flujo del programa.

Funciones principales:
- carga_datos(ruta) — Lee el archivo CSV de Airbnb y devuelve un DataFrame. Verifica que el archivo exista antes de leerlo y captura cualquier error durante la lectura.
- limpiar_precio(df) — Limpia la columna precio del DataFrame, eliminando símbolos como $ y comas, y la convierte a tipo numérico. Descarta las filas con precios inválidos.
- filtrar_datos(dataframe) — Filtra el DataFrame dejando únicamente las columnas necesarias para el análisis: id, nombre, barrio, coordenadas, tipo de alojamiento, precio, noches mínimas, disponibilidad y reviews.
- carga_preferencias_usuario(df) — Solicita al usuario sus preferencias por consola: barrio, presupuesto máximo por noche, cantidad de noches y tipo de alojamiento. El menú de tipos de alojamiento se genera dinámicamente a partir del CSV.
- validar_dataframe(df) — Verifica que el DataFrame no esté vacío o sea nulo, mostrando un aviso en caso de error.
- validar_preferencias(preferencias, barrios_validos) — Valida que el precio y la cantidad de noches sean números enteros positivos, y que el barrio ingresado exista en el dataset.
- filtrado_por_barrio(preferencia_del_usuario, dataframe_filtrado) — Crea un nuevo DataFrame con únicamente los alojamientos pertenecientes al barrio elegido por el usuario.
- tipo_de_hospedaje(hospedaje, preferencia_hospedaje) — Verifica si el tipo de alojamiento de un hospedaje coincide con la preferencia del usuario. Devuelve True o False.
precio(hospedaje, preferencia_precio) — Verifica si el precio de un hospedaje está dentro del presupuesto máximo del usuario. Devuelve True o False.
- cant_noches(hospedaje, cant_noches_usuario) — Verifica si la cantidad de noches del usuario está dentro del rango aceptado por el hospedaje. Devuelve True o False.
- buscar_compatibles(df_barrio, preferencias) — Recorre todos los hospedajes del barrio y devuelve un DataFrame con los que cumplen las tres condiciones: tipo, precio y cantidad de noches.
- promedio_precio(df_barrio) — Calcula el precio promedio de los hospedajes de un barrio, redondeado a 2 decimales.
- min_noches(df_barrio) — Devuelve la menor cantidad mínima de noches requerida entre todos los hospedajes del barrio.
- max_noches(df_barrio) — Devuelve la mayor cantidad máxima de noches permitida entre todos los hospedajes del barrio.
- crear_mapa(df_filtrado) — Genera un mapa interactivo con Folium mostrando la ubicación de los alojamientos compatibles, usando sus coordenadas de latitud y longitud.
- crear_tabla_html(df_filtrado) — Genera una tabla HTML con los alojamientos compatibles y la guarda en la carpeta outputs/.

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
Se utilizaron tres librerías externas en este proyecto. La primera es pandas, que se usa para la carga, limpieza y procesamiento del archivo CSV. La segunda es matplotlib, utilizada para la generación de gráficos generales. La tercera es Folium, utilizada para generar el mapa interactivo con la ubicación de los alojamientos compatibles. 
Dataset:
Se utilizan datos públicos de Inside Airbnb, que publica periódicamente información de los listings disponibles en distintas ciudades del mundo. El archivo contiene datos como precio, barrio, tipo de alojamiento, cantidad de reviews y disponibilidad, entre otros.
El archivo CSV no está incluido en este repositorio por su tamaño. Debe descargarse manualmente desde el sitio de Inside Airbnb.

Division de tareas: 
Victoria Fagalde — Infraestructura base: carga del CSV, validación del DataFrame, limpieza de la columna de precios y filtrado de columnas relevantes.
Martina Sergi — Interacción con el usuario: entrada de preferencias, validación de esas preferencias y filtrado por barrio.
Camila Dalbora — Lógica analítica: métricas del barrio (promedio de precio, mínimo y máximo de noches) y funciones de comparación para encontrar alojamientos compatibles.
Ramiro Gago — Visualizaciones: mapa interactivo con Folium y tabla HTML de resultados.
Delfina Puiggari — El main.py, manejo de excepciones, documentación y diagrama de flujo.

Uso de IA
- Durante el desarrollo de este proyecto se utilizaron herramientas de IA generativa como apoyo en distintas etapas del proceso. A continuación se detalla cómo fue utilizada por cada integrante:
- Victoria utilizó Claude y Gemini Pro para la generación de las funciones correspondientes a su módulo y division de tareas. 
- Camila utilizó Claude para la generación de las funciones correspondientes a su módulo.
- Martina utilizó Gemini Pro para la generación de las funciones correspondientes a su módulo.
- Delfina utilizó Claude para redactar y organizar el README, verificando que no faltara ninguna sección y que la estructura fuera clara. También generó una pequeña descripción de cada prompt utilizado por el grupo para facilitar la lectura y comprensión de los profesores. 
- Ramiro utilizó IA para entender el funcionamiento de las visualizaciones con matplotlib y la librería Folium, aplicando ese conocimiento en el desarrollo de su módulo. 

En todos los casos, las funciones fueron pensadas y diseñadas por el grupo antes de recurrir a la IA. Es decir, el equipo definió qué funciones eran necesarias, qué parámetros recibían y qué debían devolver, y luego se utilizó la IA para ayudar a implementarlas. Todos los integrantes comprenden el código entregado y pueden explicarlo y modificarlo.
También se utilizó IA para la división inicial de tareas del proyecto, como punto de partida para organizar el trabajo grupal.
A continuación se incluyen algunos de los prompts más relevantes utilizados durante el desarrollo:

Prompt de división de tareas y diseño del sistema 
— Se le proporcionó a la IA el contexto general del proyecto junto con la estructura de carpetas y las funciones pensadas por el grupo, y se le pidió que dividiera el trabajo en tareas para 5 personas agrupando funciones similares. También se le pidió que sugiriera funciones o archivos que pudieran estar faltando. 

“Estamos creando un código que busca facilitar el análisis del mercado de alojamientos de Airbnb en CABA, Buenos Aires. El objetivo es que el sistema procese los datos y presente patrones de precios, zonas más demandadas (preferencias por zonas turísticas, laborales, muy en el centro de la ciudad, con buen acceso a transporte público, etc.), ratings previos y otros factores que influyen en la valoración de los alojamientos, para que el usuario pueda tomar la mejor decisión. El programa recibirá archivos CSV descargados de Inside Airbnb con datos reales de listings (precio, barrio, tipo, reviews, disponibilidad, etc.); procesará limpieza de datos, filtrado, agrupación y cálculo de estadísticas descriptivas; y finalmente mostrará tablas resumen, gráficos de barras, distribuciones de precios y comparativas por zona, por preferencia a partir de lo que ingresó el usuario, y por otros datos de relevancia. Finalmente genera gráficos. Si te parece que falta alguna función o archivo importante, avisá. Se adjunta un archivo con la estructura de carpetas del repositorio y las funciones pensadas por el grupo con sus inputs y outputs esperados. Dividí esto en tareas para 5 personas, agrupando funciones similares “

Prompt de diseño e implementación del módulo de carga de datos 
— Se le proporcionó a la IA el contexto general del proyecto junto con el diagrama de flujo, y se le pidió que generara la función carga_datos() para el módulo carga.py. El prompt especificaba que debía leer el CSV de Inside Airbnb, devolver un DataFrame validado y utilizar la librería pandas: 

“Estamos creando un código que busca facilitar el análisis del mercado de alojamientos de Airbnb en CABA, Buenos Aires. El objetivo es que el sistema procese los datos y presente patrones de precios, zonas más demandadas (preferencias por zonas turísticas, laborales, very en el centro de la ciudad, con buen acceso a transporte público, etc.), ratings previos y otros factores que influyen en la valoración de los alojamientos, para que el usuario pueda tomar la mejor decisión. El programa recibirá archivos CSV descargados de Inside Airbnb con datos reales de listings (precio, barrio, tipo, reviews, disponibilidad, etc.); procesará limpieza de datos, filtrado, agrupación y cálculo de estadísticas descriptivas; y finalmente mostrará tablas resumen, gráficos de barras, distribuciones de precios y comparativas por zona, por preferencia a partir de lo que ingresó el usuario, y por otros datos de relevancia. Se adjunta el diagrama de flujo del programa. Comenzando por el módulo de carga de datos, se necesita un código que lea el CSV de Airbnb y devuelva un DataFrame validado. La librería utilizada es pandas y la función principal debe llamarse carga_datos. ”

Prompt de implementación del módulo de usuario 
— Se le proporcionó a la IA el contexto general del proyecto junto con el flujo completo del programa, y se le pidió ayuda para codear paso a paso las funciones correspondientes al módulo de interacción con el usuario: entrada de preferencias, validación y filtrado por barrio. 

“Estamos creando un código que busca facilitar el análisis del mercado de alojamientos de Airbnb en CABA, Buenos Aires. El objetivo es que el sistema procese los datos y presente patrones de precios, zonas más demandadas (preferencias por zonas turísticas, laborales, muy en el centro de la ciudad, con buen acceso a transporte público, etc.), ratings previos y otros factores que influyen en la valoración de los alojamientos para que el usuario pueda tomar la mejor decisión. El programa recibirá archivos CSV descargados de Inside Airbnb con datos reales de listings (precio, barrio, tipo, reviews, disponibilidad, etc.); procesará limpieza de datos, filtrado, agrupación y cálculo de estadísticas descriptivas; y finalmente mostrará tablas resumen, gráficos de barras, distribuciones de precios y comparativas por zona, por preferencia a partir de lo que ingresó el usuario, y por otros datos de relevancia. Finalmente genera gráficos.
Te adjunté el flujo del programa. Soy la persona 2, Marty, y me encargo de todo lo que toca el usuario: entrada de preferencias, validación de esas preferencias y filtrado por barrio. Ya te pasé la función validar_dataframe(). Ayudame a hacer todo lo otro paso a paso.”

Prompt de diseño e implementación del módulo de métricas y comparaciones 
— Se le proporcionó a la IA el contexto general del proyecto junto con las funciones asignadas, y se le pidió que antes de codear explicara qué funciones serían necesarias, qué parámetros reciben y qué devuelven, para tener un panorama completo antes de arrancar. 

“Estamos creando un código que busca facilitar el análisis del mercado de alojamientos de Airbnb en CABA, Buenos Aires. El objetivo es que el sistema procese los datos y presente patrones de precios, zonas más demandadas (preferencias por zonas turísticas, laborales, muy en el centro de la ciudad, con buen acceso a transporte público, etc.), ratings previos y otros factores que influyen en la valoración de los alojamientos, para que el usuario pueda tomar la mejor decisión. El programa recibirá archivos CSV descargados de Inside Airbnb con datos reales de listings (precio, barrio, tipo, reviews, disponibilidad, etc.); procesará limpieza de datos, filtrado, agrupación y cálculo de estadísticas descriptivas; y finalmente mostrará tablas resumen, gráficos de barras, distribuciones de precios y comparativas por zona, por preferencia a partir de lo que ingresó el usuario, y por otros datos de relevancia. Finalmente genera gráficos.
Te adjunto la parte que me toca: el módulo de métricas y comparaciones. Las funciones son promedio_precio(), min_noches() y max_noches(). También me sugirieron agregar un calcular_score() que puntúe coincidencias parciales (2/3 condiciones) para mostrarle al usuario resultados "casi compatibles" cuando no hay resultados al 100%. Antes de arrancar a codear, decime todo lo que tengo que tener en cuenta: las funciones que voy a necesitar, qué toman por parámetro y qué devuelven, y detalles importantes a considerar.”

Prompt de correcciones y consultas sobre el módulo de métricas 
— Tras recibir el código generado, se le hicieron a la IA preguntas puntuales de comprensión: qué hace round(), si es necesario importar pandas, y cómo adaptar el código para que sea compatible con el diccionario de preferencias que usa el módulo de otra integrante. 

“Correcciones y preguntas a partir de lo que me devolviste:
¿Qué es el round() en return round(df_barrio["price"].mean(), 2)?
¿No tengo que poner import pandas as pd al principio si estoy usando funciones de pandas?
Mi compañera, que se ocupa de pedirle las preferencias al usuario, está guardando cada una en un diccionario: preferencias = {"neighbourhood": barrio, "price": precio, "minimum_nights": noches, "room_type": tipo_hospedaje}. ¿Cómo debería llamar a las preferencias para que mi código sea compatible con esto? “

Prompt de implementación del módulo principal (main.py) 
— Se le proporcionó a la IA el contexto general del proyecto junto con todas las funciones desarrolladas por el grupo, y se le pidió que armara el main.py integrando dichas funciones, detectando posibles errores o inconsistencias entre ellas.

“Te paso las funciones que hicimos. el objetivo es que el programa corra. detecta posibles errores y arma un main.py que integre y haga funcionar el programa de airbnb”

Prompt de implementación del módulo de visualización con Folium 
— Se le proporcionó a la IA el contexto del proyecto y se le pidió ayuda para generar la base del código que crea el mapa con Folium usando latitud y longitud, incluyendo validaciones: aviso si no hay alojamientos disponibles, conversión de precio a float y noches a int, y confirmación final de creación del mapa.

“Estamos creando un código usando Folium para representar los alojamientos disponibles, una vez ingresadas las preferencias del usuario. La idea es que me ayudes a generar la base para el código de Folium usando la longitud y latitud de cada alojamiento. Además, como requisito el código debe avisar si no hay alojamientos disponibles, cambiar el precio de los alojamientos a float, cambiar la cantidad de noches a int, y finalmente, dar un aviso final si es posible crear el mapa.”






