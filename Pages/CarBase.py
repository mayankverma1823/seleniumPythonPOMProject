
from selenium.webdriver.common.by import By
from selenium import webdriver

from Utilities import configreader


class CarBase:

    def __init__(self,driver):
        self.driver = driver

    def getCarHeader(self):
        return self.driver.find_element(By.XPATH,configreader.readConfig("Titles","CarHeader_Xpath")).text

    def getCarTitleAndPrices(self):
        carNames = self.driver.find_elements(By.XPATH,configreader.readConfig("Titles","CarTitle_Xpath"))
        carTitles = self.driver.find_elements(By.XPATH,configreader.readConfig("Titles","CarPrice_Xpath"))

        for i in range(1, len(carTitles)):
            print((carNames[i].text+"_______car price is________"+carTitles[i].text).encode('utf8'))







