from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By 

class Companies:
    def __init__(self):
        self.__punctuation__ = ""
        self.__name__ = ""
        self.__companyType__ = ""
        self.__address__ = ""
        self.__contact__ = ""
    

    def get(self, searchs: list[WebElement] ):
        results = {"pontuação": [],  "nome": [],  "tipo_da_empresa": [], "endereço": []  , "contato": [] }

        for result in searchs:
            self.__punctuation__ = result.find_element(By.CLASS_NAME, "MW4etd").text if result.find_elements(By.CLASS_NAME, "MW4etd") else "Sem pontuação"
            
            try:
                self.__name__ = result.find_element(By.CLASS_NAME, "fontHeadlineSmall").text
            except:
                self.__name__ = "Sem nome"

            company_type_with_address_elements = result.find_elements(By.CLASS_NAME, "W4Efsd")

            company_type_with_address_texts = company_type_with_address_elements[2].text.split(" · ")

            try:
                self.__companyType__ = company_type_with_address_texts[0]
            except:
                self.__companyType__ = "Sem tipo"

            try:
                self.__address__ = company_type_with_address_texts[1]
            except:
                self.__address__ = "Sem endereço"
        

            information_container_for_time_contact =  result.find_element(By.CLASS_NAME, "fontBodyMedium")

            time_with_contact = information_container_for_time_contact.find_elements(By.CLASS_NAME, "W4Efsd")


            try:
                self.__contact__ = time_with_contact[3].text.split(" · ")[1]
            
            except:
                self.__contact__ = "Sem contato"


            results["pontuação"].append(self.__punctuation__)
            results["nome"].append(self.__name__)
            results["tipo_da_empresa"].append(self.__companyType__)
            results['endereço'].append(self.__address__)
            results["contato"].append(self.__contact__)
        

        return results