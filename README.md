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

# 1.3 Análisis de los datos mediante Dashboards en Excel.

Una vez obtenidos los tres archivos Excel con los datos de las canciones, empleados - clientes y las facturas, quiero montar un modelo en Excel para poder analizar los datos de las tablas.

Lo primero que hago es ir a la opción de modelo de datos en Excel, y cargar mis tres archivos. Una vez cargados, los relaciono mediente las columnas de Id que comentaba en el apartado de SQL. Cuando ya tengo mis tres tablas relacionadas, añado al modelo una tabla calendario para poder realizar análisis por periodos de tiempo. El modelo que he preparado queda de la siguiente manera:

<img width="966" height="512" alt="image" src="https://github.com/user-attachments/assets/0cdea64b-6ea1-4387-b41b-3e9b4112689e" />

Como mis tablas y los Dashboards que voy a preparar van a estar en un mismo archivo, decido hacer dos menús interactivos, uno para mostrar la información de las tablas y el análisis con tablas dinámicas realizado sobre ellas,

<img width="160" height="476" alt="image" src="https://github.com/user-attachments/assets/c33b17e4-4ca1-45f0-a950-9e06664be7ac" />

y otro, para mostrar directamente los dashboards con los datos más relevantes. 

<img width="1492" height="75" alt="image" src="https://github.com/user-attachments/assets/04f0c202-8d90-43c2-b815-afda088105b8" />

Como el análisis de los datos es de un modelo de tres tablas, he decidido realizar cuatro dashboards diferentes para tener un análisis completo del modelo.

El primero de ellos tendría la información más relevante del modelo, analizando los datos mediante la relación de las diferentes tablas

<img width="1581" height="660" alt="image" src="https://github.com/user-attachments/assets/e34eccc4-41d3-47d2-994f-eed06629e50b" />

Los siguientes dashboards contienen el análisis individual de los datos de cada tabla obtenida, es decir:

# Para la tabla de Canciones:

<img width="1615" height="660" alt="image" src="https://github.com/user-attachments/assets/138a2921-d71a-43d1-99ab-7ea38adbe859" />


# Para la tabla de Empleados - Clientes

<img width="1568" height="651" alt="image" src="https://github.com/user-attachments/assets/4d93b8a2-d162-49cc-b152-a7129d11ca34" />


# Para la tabla de Facturas:

<img width="1593" height="658" alt="image" src="https://github.com/user-attachments/assets/6c161725-e668-4ec7-8103-894a4221de16" />

Con este último paso, tendríamos el análisis de los datos obtenidos mediante las consultas realizadas a una base de datos inicial.

# 2. Estructura del proyecto.

A continuación, describo los archivos obtenidos que se encuentran en el repositorio.

Primer Paso SQL:

Tres archivos con los scripts para la obtención de la tabla de Canciones, Tabla de empleados - Clientes y Tabla de Facturas.

Obtenemos los archivos Datos Canciones_inicial, Datos Empleados_Clientes_Inicial y Datos Facturas_inicial

Segundo Paso Python:

Tres archivos con los scripts para la limpieza de los archivos anteriores.

Obtenemos los archivos Datos Canciones - modificado, Datos empleados_Clientes-modificado y Datos Facturas - modificado

Tercer paso Excel.
   
Un archivo Data_Anal_PFinal con el análisis de los datos obtenidos de los pasos anteriores.

** También añado un archivo denominado Análisis Datos Obtenidos, que contiene el análisis de manera redactada de los datos más relevantes que se han obtenido del modelo.

# 3. Instalación y requisitos.

Este proyecto se estructura mediante una serie de archivos que hemos obtenido de una base de datos inicial. Los programas que he utilizado para obtener dichos archivos serían los siguientes:

- DBeaver, versión 25.1.3
  
- Visual Studio Code 1.97.0
    con las siguientes Librerías:
    1. Pandas
    2. Openpyxl
      
- Microsoft Excel

# 4. Resultados y conclusiones.

Los resultados y las conclusiones están analizadas en profundidad en el archivo Análisis Datos Obtenidos, pero como resumen puedo indicar lo siguiente:

Las mayoría de las ventas se encuentran concentradas en muy pocos países, no ha diversificación de las mismas

<img width="491" height="299" alt="image" src="https://github.com/user-attachments/assets/46c9d6c5-3375-45f0-a6c0-7f76525c6427" />

A parte, el modelo se sostiene con ventas de poco importe, no hay grandes ventas durante el transcurso de los años. Con el paso del tiempo las ventas son estables por importes muy parecidos y sin grandes subidas.

<img width="523" height="106" alt="image" src="https://github.com/user-attachments/assets/58973e04-24bf-4475-b0dd-e2ebed914297" />

Así mismo, las ventas también se concentran en muy pocas canciones y con las mayores ventas concentradas en la franja de 40 € - 50 €.

<img width="550" height="680" alt="image" src="https://github.com/user-attachments/assets/32e2f072-ebcb-49d7-9a47-e1b5fe0f46e4" />

# 5. Próximos Pasos.

Este sería el proyecto final del curso, por lo que no debería llevar un desarrollo posterior al realizado hasta ahora. Siempre se podría retocar y mejorar con las indicaciones qeu me dieran los profesores con su análisis,

# 6. Contribuciones

El proyecto está abierto a cualquier contribución que se quiera indicar y a cualquier mejora sugerida.

# 7. Autor.

Óscar Pérez Chico

<img width="167" height="33" alt="image" src="https://github.com/user-attachments/assets/53ed93a7-ac09-486d-bb3d-df8be38a833c" />

