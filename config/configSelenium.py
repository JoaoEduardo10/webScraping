from selenium import webdriver
from selenium import webdriver

from selenium.webdriver.firefox.service import Service as Firefox

service =  Firefox()
options = webdriver.FirefoxOptions()

class ConfigFirefoxSelenium:
    def __init__(self):
        self.__options__ = options
        self.__service__ = service   
    

    def get_driver_firefox(self):
        
        return webdriver.Firefox(service=self.__service__, options=self.__options__)
