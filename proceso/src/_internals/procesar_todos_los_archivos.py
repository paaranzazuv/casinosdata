from proceso.src._internals.agregar_a_excel import agregar_a_excel
from proceso.src._internals.clear_date import clear_date
from proceso.src._internals.read_data import read_data
from proceso.src._internals.read_date_casino import read_date_casino


import os


def procesar_todos_los_archivos():
    input_folder = "data/input"
    ruta_salida = "data/procesados/data.xlsx"

    archivos = [
        os.path.join(input_folder, archivo)
        for archivo in os.listdir(input_folder)
        if archivo.endswith(".xlsx") and not archivo.startswith("~$")
    ]

    for archivo in archivos:
        try:
            print(f"📄 Procesando archivo: {archivo}")
            data = read_data(archivo)
            date, casino = read_date_casino(archivo)
            data = clear_date(data, date, casino)
            agregar_a_excel(ruta_salida, data)

        except Exception as e:
            print(f"❌ Error procesando {archivo}: {e}")