# Librerías necesarias:
# pandas | openpyxl

import pandas as pd
import openpyxl as px

# Cargo el archivo CSV
df = pd.read_csv("Datos Facturas_inicial.csv")

# Renombro las columnas para que tengan nombres más amigables.
df = df.rename(columns={
    "InvoiceDate": "Fecha de Factura",
    "BillingCity": "Ciudad_Facturada",
    "BillingCountry": "País Facturado",
    "Quantity": "Cantidad",
    "UnitPrice": "Precio Unitario (€)"
})

# Sustituyo valores nulos por la palabra 'sin datos'
df = df.fillna("sin datos")

# Hago un formato para las columnas con precios. Las indico como euro, con dos decimales y separador de miles con punto.
def formato_euro(x):
    try:
        return f"{float(x):.2f}".replace(".", ",") + " €"
    except:
        return x
# Aplico el formato a las columnas correspondientes cuyos datos indican precios.
df["Total_Fra"] = df["Total_Fra"].apply(formato_euro)

df["Precio Unitario (€)"] = df["Precio Unitario (€)"].apply(formato_euro)

# Hago un formato para la columna Cantidad, convirtiendo los valores a enteros.
def formato_entero(x):
    try:
        return int(float(x))
    except:
        return x

df["Cantidad"] = df["Cantidad"].apply(formato_entero)


# Guardo el resultado en un archivo Excel
df.to_excel("Datos Facturas - modificado.xlsx", index=False)

# Muestro las primeras filas para verificar los cambios realizados.
print(df.head(8))