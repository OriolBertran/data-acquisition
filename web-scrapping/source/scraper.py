########################################################################
##                       Importem libraries                           ##
########################################################################
import os
import sys
import time
import pandas as pd
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
########################################################################

# Es defineix on desar els 3 datasets generats amb l'scraping i també l'informe executat
currentDirectory = os.getcwd()
parentDirectory = os.path.abspath(os.path.join(currentDirectory, os.pardir))
datasetFolder = "dataset"
os.makedirs(os.path.join(parentDirectory, datasetFolder), exist_ok=True)
folderToSaveDataset = os.path.join(parentDirectory, datasetFolder)

# Es defineix les opcions del Chrome Driver
chrome_options = Options()
# chrome_options.add_argument('--headless') 
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_prefs = {
    "download.default_directory": folderToSaveDataset,
    "download.prompt_for_download": False,  
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
}
chrome_options.add_experimental_option("prefs", chrome_prefs)
driver = webdriver.Chrome(options=chrome_options)
user_agent = driver.execute_script("return navigator.userAgent;")
print(f"\n\nThe user agent used in this chrome driver is the following: \n{user_agent}\n\n")
driver.implicitly_wait(10)

def download_report(startDate, endDate):
    """
    Funció que navega automàticament per la web de l'Agència Catalana de l'Aigua fins a capturar 
    els tres datasets, més l'informe executat.
    Paràmetres:
        -  startDate (date): data inicial de l'informe a executar
        -  endDate (date): data final de l'informe a executar
    """
    try:
        # Pàgina inicial
        url_inicial = 'https://aplicacions.aca.gencat.cat/sdim21/'
        driver.get(url_inicial)

        # Definim el temps d'espera
        wT = 25

        # Des de la pàgina inicial, es selecciona "Entrar"
        enterButton = driver.find_element(By.XPATH, '/html/body/div[2]/div/form/input[3]')
        enterButton.click()

        # Es selecciona "DADES A PARTIR DEL 2007" i es procedeix a la pàgina següent
        yearButton = driver.find_element(By.XPATH, '/html/body/div[2]/div/form/div[1]/div[2]/label[1]/input')
        yearButton.click()
        time.sleep(2) #####
        selectionButton = driver.find_element(By.XPATH, '/html/body/div[2]/div/form/div[2]/input')
        selectionButton.click()
        time.sleep(2) #####

        ## Primer dataset: Xarxa de control i elements
        #xarxaControl = []
        #elements = []
        #t = 2
        #while True:
        #    xpathXarxa = f'//*[@id="llistaXarxesControl"]/div[3]/div[{t}]/div[1]/label'
        #    try:
        #        tagTitle = driver.find_element(By.XPATH, xpathXarxa)
        #        titleControl = tagTitle.get_attribute("title")
        #        xarxaControl.append(titleControl)
        #        e = 2
        #        elements_list = []  
        #        while True: 
        #            xpathElements = f'//*[@id="llistaXarxesControl"]/div[3]/div[{t}]/div[{e}]/label'          
        #            try: 
        #                tagTitle = driver.find_element(By.XPATH, xpathElements)
        #                titleElement = tagTitle.get_attribute("title")
        #                elements_list.append(titleElement)
        #                e += 1                     
        #            except NoSuchElementException:
        #                # No elements found, exit the loop
        #                break
        #        elements.append(', '.join(elements_list))
        #        t += 1
        #    except NoSuchElementException:
        #        # No elements found, exit the loop
        #        break
        ## Create DataFrame from lists
        #xarxaControl = pd.DataFrame({'Xarxa de Control': xarxaControl, 'Elements': elements})
        #xarxaControl.to_csv(os.path.join(folderToSaveDataset,r'xarxa_Control.csv'), index=False, encoding="utf-8-sig")

        # "Xarxa de control". Es selecciona "Nivells piezomètrics" i es procedeix al següent pas: "Paràmetres"
        piezometricLevelsSelectionButton = WebDriverWait(driver, wT).until(EC.element_to_be_clickable((By.XPATH, "//label[@title='Nivells piezomètrics']")))
        piezometricLevelsSelectionButton.click()   
        loadingCircle = WebDriverWait(driver, wT).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/img')))
        loadingCircle = WebDriverWait(driver, wT).until(EC.invisibility_of_element((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/img')))
        toParametersButton = WebDriverWait(driver, wT).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/form/div[1]/div[2]/div[6]/div/div/div[2]/div[1]/a/div')))
        toParametersButton.click()
        
        # "Paràmetres". Es selecciona "Piezometria" i es procedeix al següent pas: "Àmbit geogràfic"
        #piezometriaSelectionButton = WebDriverWait(driver, wT).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/form/div[1]/div[2]/div[3]/div/div/div[6]/div/ul/li/input')))
        piezometriaSelectionButton = WebDriverWait(driver, wT).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/form/div[1]/div[2]/div[3]/div/div/div[6]/div/ul/li/input')))
        piezometriaSelectionButton.click()
        loadingCircle = WebDriverWait(driver, wT).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/img')))
        loadingCircle = WebDriverWait(driver, wT).until(EC.invisibility_of_element((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/img')))
        toZoneButton = WebDriverWait(driver, wT).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/form/div[1]/div[2]/div[6]/div/div/div[2]/div[2]/a/div')))
        toZoneButton.click()
        time.sleep(5) #####

        # "Àmbit  geogràfic". Es selecciona "Aqüífers", es deseleccionen tots els aqüífer i es selecciona: "Aqüífer al·luvial de la cubeta de la Llagosta". 
        # Després es procedeix al següent pas: "Ajust selecció final"
        loadingCircle = WebDriverWait(driver, wT).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/img')))
        loadingCircle = WebDriverWait(driver, wT).until(EC.invisibility_of_element((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/img')))
        aquifersButton = WebDriverWait(driver, wT).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/form/div[1]/div[2]/div[4]/div/div[3]/div[6]/div/input')))
        aquifersButton.click() 
        loadingCircle = WebDriverWait(driver, wT).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/img')))
        loadingCircle = WebDriverWait(driver, wT).until(EC.invisibility_of_element((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/img')))

        # ## Segon dataset: Aqüífer de Catalunya
        # totalAquifers = []
        # elements = driver.find_elements(By.CSS_SELECTOR, '.inputLabel.valorAquifer')
        # for element in elements:
        #     text = element.text.strip()
        #     if text:
        #         totalAquifers.append(element.get_attribute("title"))
        # totalAquifers = pd.DataFrame({'Aqüífer de Catalunya': totalAquifers})
        # totalAquifers.to_csv(os.path.join(folderToSaveDataset,r'aqüífers_catalunya.csv'), index=False, encoding="utf-8-sig")

        deselectionButton = driver.find_element(By.XPATH, "//input[@id='checkAllAquifers']")
        deselectionButton.click()
        besosSelectionButton = driver.find_element(By.XPATH, "//label[contains(@class, 'valorAquifer')][contains(text(), 'Aqüífer al·luvial de la cubeta de la Llagosta')]/preceding-sibling::input")
        besosSelectionButton.click()
        toFinalAdjustmentButton = driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div[1]/div[2]/div[6]/div/div/div[2]/div[3]/a/img[1]')
        toFinalAdjustmentButton.click()
        loadingCircle = WebDriverWait(driver, wT).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/img')))
        loadingCircle = WebDriverWait(driver, wT).until(EC.invisibility_of_element((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/img')))
        time.sleep(2) #####

        # "Ajust selecció final". Es deixen tots els punts de control seleccionats i es passa al següent pas: "Informe Resultats"
        toReportButton = driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div[1]/div[2]/div[6]/div/div/div[2]/div[4]/a/img')
        toReportButton.click()
        time.sleep(2) #####

        # Es selecciona la finestra d'estudi en base a les dates entrades
        startYear = startDate.year
        startMonth = startDate.month - 1
        startDay = startDate.day
        endYear = endDate.year
        endMonth = endDate.month - 1
        endDay = endDate.day
        
        # Data inicial
        startingDateButton = driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div[3]/div[1]/div/div[2]/div/div/div[1]/div[2]/img')
        startingDateButton.click()
        time.sleep(2) #####
        # Mes inicial
        selectStartMonth = Select(driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div/div/select[1]'))
        selectStartMonth.select_by_value(str(startMonth))
        time.sleep(2) #####
        # Any inicial
        selectStartYear = Select(driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div/div/select[2]'))
        selectStartYear.select_by_value(str(startYear))
        time.sleep(2) #####
        # Dia inicial
        selectStartDay = driver.find_element(By.XPATH, f'//*[@id="ui-datepicker-div"]/table/tbody/tr/td[@data-handler="selectDay"]/a[text()="{startDay}"]')
        selectStartDay.click()
        time.sleep(2) #####

        # Data final
        endingDateButton = driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div[3]/div[1]/div/div[2]/div/div/div[2]/div[2]/img')
        endingDateButton.click()
        time.sleep(2) #####
        # Mes final
        selectEndMonth = Select(driver.find_element(By.XPATH, '/html/body/div[4]/div/div/select[1]'))
        selectEndMonth.select_by_value(str(endMonth))
        time.sleep(2) #####
        # Any final
        selectEndYear = Select(driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div/div/select[2]'))
        selectEndYear.select_by_value(str(endYear))
        time.sleep(2) #####
        # Dia final
        selectEndDay = driver.find_element(By.XPATH, f'//*[@id="ui-datepicker-div"]/table/tbody/tr/td[@data-handler="selectDay"]/a[text()="{endDay}"]')
        selectEndDay.click()
        time.sleep(2) #####
        
        # Es selecciona "Excel" com a format de l'arxiu de sortida corresponent a l'informe executat
        format_dropdown = Select(driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div[3]/div[1]/div/div[2]/div/div/div[3]/div/select'))
        format_dropdown.select_by_value('excel')  # 'excel' is the value of the "Excel" option
        time.sleep(2) #####
        executa_informe_button = driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div[3]/div[1]/div/div[3]/button[1]')
        executa_informe_button.click()

        time.sleep(10)

    finally:
        # Close the webdriver
        driver.quit()
