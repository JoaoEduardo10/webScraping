import pandas
import time

from services.get_companies import Companies
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys


class Screen:
    def __init__(self, query, driver):
        self.__query__ = query
        self.__driver__ = driver    

    def start(self, quantity=0):
        wait = WebDriverWait(self.__driver__, 10)

        sidebar = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f"div[aria-label='Resultados para {self.__query__}']")))

        keepScrolling = True


        print("iniciando screen...")
        count = 1
        while keepScrolling:

            
            print(f"numero de rolagem = {count}")


            sidebar.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.5)
            sidebar.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.5)


            html = self.__driver__.find_element(By.TAG_NAME, "html").get_attribute('outerHTML')

            searchs = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "CpccDe")))

            if(count == 50):
                keepScrolling = False
            

            if(quantity == len(searchs) and quantity != 0):
                keepScrolling = False

            if(html.find("Você chegou ao final da lista.")!=-1):
                keepScrolling=False

            count += 1
            
            


        if(keepScrolling == False):
            searchs = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "CpccDe")))

            companies = Companies()

            try:
                print("analizando dados")

                allSearchs = companies.get(searchs)


                print("criando documento...!")
                df = pandas.DataFrame(allSearchs)
                df.to_csv("../../Downloads/todo_os_petShops.csv", encoding="utf-8")
                print("dicumento criado...!")

                self.__driver__.close()
            except Exception as error:
                print("não foi possvel buscar " + str(error))

                self.__driver__.close()
