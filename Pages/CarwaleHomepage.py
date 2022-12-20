from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Pages.FindNewCarPage import NewCarHomePage
from Utilities import configreader


class HomePage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    def goToNewCars(self):
       self.hover("NewCar_Xpath")
       self.click("FindNewCar_Xpath")

       return NewCarHomePage(self.driver)


    def goToCompareCars(self):
        pass

    def UsedCars(self):
        pass