from selenium import webdriver

class ConfigSelenium:
    def __init__(self, service, options):
        self.__options__ = options
        self.__service__ = service   
    

    def get_driver_firefox(self):
        
        return webdriver.Firefox(service=self.__service__, options=self.__options__)
