# WEB SCRAPPING
## AUTOR
Oriol Bertran

## OBJECTIU
Obtenció d'un dataset fent servir eines específiques de web scraping implementant un codi en llenguatge Python. Per la descàrrega de l'última versió de Python, es recomana visitar:

https://www.python.org/downloads/

En aquest cas, es vol estudiar l'evolució dels nivells piezomètrics a l'aqüífer superficial del delta del Besòs i, per tant, s'extreuen les dades de la web de l'Agència Catalana de l'Aigua. Podeu consultar totes les dades que hi tenen disponibles seguint l'enllaç:

https://aplicacions.aca.gencat.cat/sdim21/

## METODOLOGIA
L'eina utilitzada per a fer web scraping durant aquesta pràctica, es la de Selenium conjuntament amb Chrome Driver, del navegador Google Chrome. A banda de tenir instal·lat aquest navegador, caldrà doncs tenir també baixat el Chrome Driver, podent-t'ho fer des de la pàgina:

https://googlechromelabs.github.io/chrome-for-testing/

Caldrà veure quina versió de Google Chrome està instal·lada (Ajuda > Quant a Google Chrome) per tal de baixar el Chrome Driver adeqüat. L'executable descarregat (chromedriver.exe), l'emplaçarem a la carpeta on hi situarem també el codi main.py i l'arxiu requeriments.txt facilitat. Posteriorment, executem chromedriver.exe. Podeu trobar més informació sobre l'ús de Selenium i Chrome Driver en el següent video de Youtube:

https://www.youtube.com/watch?v=WnWQgUerR0c

Així doncs, l'estructura de la carpeta hauria de ser la següent:

PRAC1/

├── dataset/

│            ├── ACA-Consulta_de_dades_del_medi.xlsx

│            ├── ACA-Consulta_de_dades_del_medi.csv
      
│            ├── xarxa_Control.csv
      
│            ├── ambit_geografic.csv

│            ├── aqüifers_catalunya.csv

├── source/

│            ├── main.py
      
│            ├── scraper.py
      
│            ├── toCsv.py
      
├── requirements.txt

├── chromedriver.exe

├── README.md

## COM CÓRRER EL CODI
Des de la terminal, s'instal·len els mòduls necessaris fent servir la instrucció:

````
pip install -r requirements.txt
````

La següent instrucció executarà el codi main.py i descarregarà les dades a la carpeta "dataset" entre les dates especificades. Format de les dates: "dd-mm-yyyy".

````
python main.py <"data_inicial"> <"data_final">
````

*Restriccions: La data inicial ha de ser a partir de l'any 2007 i anterior a la data final. La data final no pot ser posterior a la data actual.*

Per poder executar el codi des d'un Mac, les instruccions seran les següents:

Instal·lar els mòduls necessaris:
````
python3 -m pip install -r requirements.txt
````

Descàrrega de les dades a la carpeta "dataset":
````
python3 main.py <"data_inicial"> <"data_final">
````

