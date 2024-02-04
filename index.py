from selenium import webdriver
from selenium.webdriver.common.by import By 
from config.configSelenium import ConfigSelenium
from selenium.webdriver.firefox.service import Service as Firefox

service =  Firefox()
options = webdriver.FirefoxOptions()

firefoxDriver = ConfigSelenium(service=service, options=options)

driver = firefoxDriver.get_driver_firefox()


url = "https://www.google.com.br/maps/search/pet+shops+teresina/@-5.1055916,-42.8345119,13z/data=!4m2!2m1!6e6?entry=ttu";


driver.get(url)


