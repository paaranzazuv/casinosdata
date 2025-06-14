import pandas as pd


def read_data(input_folder):
    columnas_deseadas = ["Maq", "NUC", "Serial", 'Marca', 'Juego', 'Billetero', 'Bruto', 'Premios','Retanqueo', 'Neto']

    df = pd.read_excel(
        input_folder,
        sheet_name="RptMovMaquinaAcumulado",
        header=11
    )


    # Filtrar columnas deseadas
    df = df[columnas_deseadas]

    # Limpiar espacios de los nombres de columnas (debería ir antes del filtro)
    df.columns = df.columns.str.strip()

    # Eliminar puntos en los valores de texto
    df = df.applymap(lambda x: str(x).replace(".", "") if isinstance(x, str) else x)

    # Convertir columnas numéricas a int (manejar errores por seguridad)
    columnas_numericas = columnas_deseadas[5:]
    df[columnas_numericas] = df[columnas_numericas].apply(
        lambda col: pd.to_numeric(col, errors="coerce").fillna(0).astype(int)
    )

    # Eliminar filas donde Neto y Premios son 0
    df = df[~((df["Neto"] == 0) & (df["Premios"] == 0))]
    df = df.iloc[:-1]

    return df