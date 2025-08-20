<img width="150" height="150" alt="image" src="https://github.com/user-attachments/assets/c22815c9-8b0e-4dd5-ab7a-7a44c8f93504" />

# PROYECTO FINAL: ANÁLISIS DE UNA BASE DE DATOS MEDIANTE SQL Y PYTHON. ELABORACIÓN DE DASHBOARDS CON LOS DATOS OBTENIDOS

En este proyecto he plasmado lo aprendido durante el curso, intentando utilizar todos los conocimientos que nos han enseñado durante este tiempo.

# 1. Descripción del proyecto.

Para la realización del proyecto, he intentado poner en práctica los conocimientos que hemos aprendido en todos los temas. La idea que se me ocurrió para esto fue, utilizar una base de datos de donde extraer varias tablas mediante sentencias SQL, después realizar una limpieza de datos mediante Python y, por último, realizar un análisis de datos junto con un dashboard en Excel para poder analizar los resultado obtenidos, de esta forma utilizaría los conocimientos de todos los módulos vistos durante el curso.

# 1.1. Extracción de los datos a utilizar de una base de datos.

Para obtener los archivos con los datos que iba a utilizar, he utilizado una base de datos que muestra las ventas de canciones en una tienda online.

La base de datos se organiza mediante el siguiente diagrama:

<img width="709" height="840" alt="image" src="https://github.com/user-attachments/assets/885d6a7f-3d30-4b8c-8caf-f3b2263c86d0" />

Una vez obtenido el diagrama de la base de datos, revisé qué tipo de datos podía necesitar para llevar a cabo este proyecto, y me decidí por realizar tres scripts diferentes para extraer tres archivos con los datos que iba a analizar.

Primero quería obtener todos los datos relacionados con las canciones que pudiera analizar posteriormente, por lo que realicé la siguiente consulta:

<img width="932" height="330" alt="image" src="https://github.com/user-attachments/assets/053a2d47-6aa4-4057-ac91-cd7dac3c6a5d" />

Una vez obtenidos los datos de las canciones, quería obtener los datos de los empleados y los clientes, por lo que hice la siguiente consulta:

<img width="932" height="134" alt="image" src="https://github.com/user-attachments/assets/ec3c0335-6108-4173-8bed-a00b3399652d" />

Por último, necesitaba saber los datos relacionados con las ventas y las facturas, por lo que realicé esta última consulta:

<img width="862" height="121" alt="image" src="https://github.com/user-attachments/assets/f887f078-7b5c-4f58-bdf9-fab6dad8f1cc" />

Las consultas que he realizado no son muy restrictivas ni complejas, por que la idea es obtener datos en bruto, para "limpiarlos" mediante Python, por lo que no he modificado nombres de columnas, .....

Lo que si he tenido en cuenta, es que cada archivo extaído tenga una columna de Id que se pueda relacionar entre ellos, por que quieres analizarlos como un modelo conjunto, por lo que tengo que tener columnas de Id que me sirvan para poder relacionar las tablas y realizar dicho modelo.

# 1.2 Limpieza de los datos obtenidos mediante Python.

Una vez que ya tenía mis tres archivos csv con los datos que necesitaba, he realizado una limpieza de los mismos mediante Python.

Para la limpieza de los archivos me he centrado en cuatro aspectos que consideraba más importantes:

- Renombrar las columnas para ponerle títulos más adecuados para el análisis posterior.
- Formatear los datos que fueran de número o precio, para indicarle el separador de miles y utilizar la coma como separador decimal, además poner números enteros donde fuera necesario.
- Revisión de nulos, cambiándolos por la frase "Sin datos".
- Obtener un archivo Excel con el que poder formar un modelo para analizar.

Como en el caso anterior de extracción de datos mediante SQL, las consultas realizadas en Python no son la realización de un análisis EDA completo en profundidad, ya que esa parte, la haré mediante Excel y la creación de Dashboards de control. Me he centrado en reailizar una pequeña limpieza de los datos para que me queden unos archivos Excel preparados para analizar.

En la primera consulta de Python realicé los siguientes pasos para el archivo que contenía los datos de las canciones:

<img width="1209" height="787" alt="image" src="https://github.com/user-attachments/assets/205518f4-93d0-447a-95ca-792820bffadb" />

El siguiente archivo csv que analicé fue el que contenía los datos de los empleados y clientes, para el que hice un análisis similar al anterior:

<img width="1218" height="564" alt="image" src="https://github.com/user-attachments/assets/90daa876-cce8-4d5e-b681-2b668fda0eb5" />

Por último, realizo la limpieza del archivo que contiene los datos de las facturas:

<img width="995" height="897" alt="image" src="https://github.com/user-attachments/assets/fbc85c5f-12b7-441c-a19c-ef375214c33a" />

