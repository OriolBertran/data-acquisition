#-------------------------------#
# Importing the libraries       #
#-------------------------------#
import os
import sys
from datetime import datetime
from toCSV import excel_to_csv
from scraper import download_report

def main():
    startDate_str = sys.argv[1]
    endDate_str = sys.argv[2]

    startDate = datetime.strptime(startDate_str, '%d-%m-%Y')
    endDate = datetime.strptime(endDate_str, '%d-%m-%Y')

    if startDate.year < 2007:
        print("Error: Starting date must be after 2007.")
        return

    if endDate > datetime.now():
        print("Error: End date cannot be later than the current date.")
        return

    if startDate > endDate:
        print("Error: The start date must be earlier than the end date.")
        return
    
    download_report(startDate, endDate)

    currentDirectory = os.getcwd()
    parentDirectory = os.path.abspath(os.path.join(currentDirectory, os.pardir))
    file_path = os.path.join(parentDirectory, "dataset", "ACA-Consulta_de_dades_del_medi.xlsx")
    excel_to_csv(file_path)
    
if __name__ == "__main__":
    main()
    
