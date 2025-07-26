# Librerías necesarias:
# pandas | openpyxl

import pandas as pd
import openpyxl as px

# Cargo el archivo CSV con los datos de empleados y clientes.
df = pd.read_csv("Datos Empleados_Clientes_inicial.csv")

# Cambio el nombre de las columnas para que sean más amigables y descriptivas.
df = df.rename(columns={
    "Title": "Título",
    "ReportsTo": "Reporte",
    "Country": "País",           # Cambio ambas columnas 'Country' (las dos tienen el mismo nombre)
    "Company": "Compañía"
})

# Como hay dos columnas que he cambiado a "País", renombro la que se ha quedado con el sufijo '.1', para evitar confusiones. La indico como "País Cliente".
if 'Country.1' in df.columns:
    df = df.rename(columns={"Country.1": "País Cliente"})

# Si hubiera valores "null", los sustituyo por la palabra "sin datos"
df = df.fillna("sin datos")

# Guardo el resultado en un archivo Excel para su posterior análisis
df.to_excel("Datos Empleados_Clientes - modificado.xlsx", index=False)

# Hago una muestra para que se puedan verificar los cambios realizados.
print(df.head(8))