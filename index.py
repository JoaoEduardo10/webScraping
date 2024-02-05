from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from services.screen import Screen


from config.configSelenium import ConfigSelenium


configSelenium = ConfigSelenium()

driver = configSelenium.get_driver()


url = "https://www.google.com.br/maps/@-5.1052418,-42.834512,13z?entry=ttu";


driver.get(url)


search = driver.find_element(By.ID, 'searchboxinput')


query = "Encontrar pet shops e hospitais para animais em Teresina, Piauí."


search.send_keys(query)

search.send_keys(Keys.ENTER)
    
screen = Screen(query, driver)

screen.start()

    


    



