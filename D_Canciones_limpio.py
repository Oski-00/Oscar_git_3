# Librerías necesarias para este Script:
# pandas | openpyxl

import pandas as pd
import openpyxl as px

# Cargo el archivo CSV original sacado de la base de datos
df = pd.read_csv("Datos Canciones.csv")

# Renombro columnas para que tengan nombres más amigables
df = df.rename(columns={
    "t_cancion": "Canción",
    "Composer": "compositor",
    "Milliseconds": "Duración",
    "Bytes": "Tamaño",
    "UnitPrice": "Precio Unitario",
    "Title": "Albúm"
})

# si hubiera valores "null", los sustituyo por la palabra "sin datos"
df = df.fillna("sin datos")

# Formateo la columna Duración: Le indico separadores de miles con un punto y convierto los números a enteros.
df["Duración"] = df["Duración"].apply(lambda x: f"{int(float(x)):,}".replace(",", ".") if str(x).isdigit() or str(x).replace('.', '').isdigit() else x)

# Formateo la columna Tamaño: Inco el separador de miles con un punto y convierto los números a enteros
df["Tamaño"] = df["Tamaño"].apply(lambda x: f"{int(float(x)):,}".replace(",", ".") if str(x).isdigit() or str(x).replace('.', '').isdigit() else x)

# Formateo la columna Precio Unitario: Indico que la moneda es el €, con dos decimales, el separador de miles con punto y el decimal con una coma 
def formateo_precio(x):
    try:
        return f"{float(x):.2f}".replace(".", ",") + " €"
    except:
        return x
df["Precio Unitario"] = df["Precio Unitario"].apply(formateo_precio)

# Guardo el archivo modificado en formato Excel
df.to_excel("Datos Canciones - modificado.xlsx", index=False)

# Muestro las primeras 8 filas para verificar cambios
print(df.head(8))