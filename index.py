from selenium.webdriver.common.by import By 
from config.configSelenium import ConfigFirefoxSelenium

firefoxDriver = ConfigFirefoxSelenium()

driver = firefoxDriver.get_driver_firefox()


url = "https://www.google.com.br/maps/search/pet+shops+teresina/@-5.1055916,-42.8345119,13z/data=!4m2!2m1!6e6?entry=ttu";


driver.get(url)


