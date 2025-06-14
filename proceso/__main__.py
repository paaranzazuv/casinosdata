import os
from proceso.src._internals.clear_date import clear_date
from proceso.src._internals.agregar_a_excel import agregar_a_excel
import shutil

from proceso.src._internals.read_data import read_data
from proceso.src._internals.read_date_casino import read_date_casino

def main():
    input_folder = "data/input"
    ruta_salida = "data/procesados/data.xlsx"
    procesados_folder = "data/procesados"

    archivos = [
        os.path.join(input_folder, f)
        for f in os.listdir(input_folder)
        if f.endswith(".xlsx") and not f.startswith("~$")
    ]

    for archivo in archivos:
        try:
            print(f"📄 Procesando: {archivo}")
            data = read_data(archivo)
            date, casino = read_date_casino(archivo)
            data = clear_date(data, date, casino)
            agregar_a_excel(ruta_salida, data)

            # Mover archivo procesado
            shutil.move(archivo, os.path.join(procesados_folder, os.path.basename(archivo)))

        except Exception as e:
            print(f"❌ Error procesando {archivo}: {e}")

if __name__ == "__main__":
    main()