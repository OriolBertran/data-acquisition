# WEB SCRAPING
## AUTHOR
Oriol Bertran

## OBJECTIVE
To obtain a dataset using specific web scraping tools by implementing code in the Python programming language. To download the latest version of Python, it is recommended to visit:

https://www.python.org/downloads/

In this case, the goal is to study the evolution of piezometric levels in the shallow aquifer of the Besòs delta. Therefore, data is extracted from the website of the Catalan Water Agency. You can explore all the available data through the following link:

https://aplicacions.aca.gencat.cat/sdim21/

## METHODOLOGY
The tool used for web scraping in this project is Selenium together with Chrome Driver, which works with the Google Chrome browser. In addition to having this browser installed, you must also download the Chrome Driver, which can be obtained from:

https://googlechromelabs.github.io/chrome-for-testing/

You’ll need to check which version of Google Chrome is installed (Help > About Google Chrome) to download the appropriate version of Chrome Driver. **NOTE:** The `chromedriver.exe` attached in this repository is from platform win64 and its version is 138.0.7204.183.

The downloaded executable file (`chromedriver.exe`) should be placed in the same folder as the `main.py` script. Afterward, execute `chromedriver.exe`. You can find more information about using Selenium and Chrome Driver in the following YouTube video:

https://www.youtube.com/watch?v=WnWQgUerR0c

Thus, the folder structure should look like this:

web-scraping/

├── source/

│            ├── main.py
      
│            ├── scraper.py
      
│            ├── toCsv.py
      
├── requirements.txt

├── chromedriver.exe

├── README.md

## HOW TO RUN THE CODE:
From the terminal, install the necessary modules using the following command:

````
pip install -r requirements.txt
````

The following command will execute `main.py` and download the data to the created "dataset" folder between the specified dates. Date format: "dd-mm-yyyy".

````
python main.py <"start_date"> <"end_date">
````

For example,

````
python main.py "01-01-2015" "01-01-2016"
````

*Restrictions: The start date must be from 2007 onwards and before the end date. The end date cannot be later than today.*

To run the code on a Mac, use the following instructions:

Install the required modules:

````
python3 -m pip install -r requirements.txt
````

Download the data to the "dataset" folder:

````
python3 main.py <"data_inicial"> <"data_final">
````

