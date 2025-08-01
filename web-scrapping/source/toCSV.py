########################################################################
##                       Importem libraries                           ##
########################################################################
import os
import csv
from itertools import islice
from openpyxl import load_workbook
########################################################################

def excel_to_csv(file_path):
    """
    Funció que converteix el dataset obtingut en format excel a
    un arxiu CSV.
    Paràmetres:
        - path_file (str): ruta de l'arxiu Excel a conevrtir
    """
    if not os.path.exists(file_path):
        print("Error: No es troba l'arxiu.")
        return

    # Carrega l'arxiu Excel
    workbook = load_workbook(file_path)
    sheet = workbook.active

    # Obre l'arxiu CSV per escriure
    csv_path = os.path.splitext(file_path)[0] + ".csv"
    with open(csv_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        # Recorre cada fila a l'Excel i escriu-la a l'arxiu CSV
        for row in islice(sheet.iter_rows(values_only=True), 8, None):
            writer.writerow(row[1:])
