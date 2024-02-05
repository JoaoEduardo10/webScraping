from selenium import webdriver
from selenium import webdriver

from selenium.webdriver.chrome.service import Service 

service =  Service()
options = webdriver.ChromeOptions()

class ConfigSelenium:
    def __init__(self):
        self.__options__ = options
        self.__service__ = service   
    

    def get_driver(self):

        self.__options__.add_argument("--headless") 
        
        return webdriver.Chrome(service=self.__service__, options=self.__options__)
