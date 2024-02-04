from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from services.get_companies import Companies

from config.configSelenium import ConfigFirefoxSelenium

import pandas

import time

firefoxDriver = ConfigFirefoxSelenium()

driver = firefoxDriver.get_driver_firefox()


url = "https://www.google.com.br/maps/@-5.1052418,-42.834512,13z?entry=ttu";


driver.get(url)


search = driver.find_element(By.ID, 'searchboxinput')


query = "Encontrar pet shops e hospitais para animais em Teresina, Piauí."


search.send_keys(query)

button_get = driver.find_element(By.CLASS_NAME, "google-symbols")

button_get.click()


wait = WebDriverWait(driver, 59)

prev_search_count = len(wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "CpccDe"))))
sidebar = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f"div[aria-label='Resultados para {query}']")))

keepScrolling = True

while keepScrolling:
    sidebar.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)
    sidebar.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)

    html =driver.find_element(By.TAG_NAME, "html").get_attribute('outerHTML')
    if(html.find("Você chegou ao final da lista.")!=-1):
        keepScrolling=False


if(keepScrolling == False):
    searchs = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "CpccDe")))

    companies = Companies()

    try:
        allSearchs = companies.get(searchs)

        df = pandas.DataFrame(allSearchs)
        df.to_csv("../../Downloads/todo_os_petShops.csv", encoding="utf-8")
        driver.close()
    except Exception as error:
        print("não foi possvel buscar " + str(error))
        driver.close()

    

    


    



