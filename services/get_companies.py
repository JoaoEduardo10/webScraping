from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By 

class Companies:
    def __init__(self):
        self.__punctuation__ = ""
        self.__name__ = ""
        self.__companyType__ = ""
        self.__address__ = ""
        self.__contact__ = ""
    

    def get(self, searchs):
        results = []

        for result in searchs:
            self.__punctuation__ = result.find_element(By.CLASS_NAME, "MW4etd").text if result.find_elements(By.CLASS_NAME, "MW4etd") else "Sem pontuação"
            self.__name__ = result.find_element(By.CLASS_NAME, "fontHeadlineSmall").text

            company_type_with_address_elements = result.find_elements(By.CLASS_NAME, "W4Efsd")

            company_type_with_address_texts = company_type_with_address_elements[2].text.split(" · ")

            self.__companyType__ = company_type_with_address_texts[0]
            self.__address__ = company_type_with_address_texts[1]    
        

            information_container_for_time_contact =  result.find_element(By.CLASS_NAME, "fontBodyMedium")

            time_with_contact = information_container_for_time_contact.find_elements(By.CLASS_NAME, "W4Efsd")

            results.append({
                "punctuation": self.__punctuation__,
                "name": self.__name__,
                "companyType": self.__companyType__,
                "address": self.__address__,  
            })
        

        return results