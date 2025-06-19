import os
import shutil
import argparse

from proceso.src._internals.clear_date import clear_date
from proceso.src._internals.agregar_a_excel import agregar_a_excel
from proceso.src._internals.read_data import read_data
from proceso.src._internals.read_date_casino import read_date_casino

def main():
    
    parser = argparse.ArgumentParser(description="Procesar archivos Excel de casinos")
    parser.add_argument('--input', '-i', required=True, help="Ruta de la carpeta de entrada con archivos .xlsx")
    parser.add_argument('--output', '-o', required=True, help="Ruta del archivo .xlsx de salida")
    parser.add_argument('--procesados', '-p', default=None, help="Carpeta donde mover archivos procesados (opcional)")

    args = parser.parse_args()

    input_folder = args.input
    ruta_salida = args.output
    procesados_folder = args.procesados or os.path.join(os.path.dirname(ruta_salida), "procesados")

    os.makedirs(procesados_folder, exist_ok=True)

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

            shutil.move(archivo, os.path.join(procesados_folder, os.path.basename(archivo)))
        except Exception as e:
            print(f"❌ Error procesando {archivo}: {e}")

if __name__ == "__main__":
    main()
excel(ruta_salida, data)

            shutil.move(archivo, os.path.join(procesados_folder, os.path.basename(archivo)))
        except Exception as e:
            print(f"❌ Error procesando {archivo}: {e}")

