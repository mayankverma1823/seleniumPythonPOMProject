
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Utilities import configreader
class BasePage:

      def __init__(self,driver):
            self.driver=driver


      def click(self,locator):
            if str(locator).endswith("_Xpath"):
                  self.driver.find_element(By.XPATH,configreader.readConfig("Reg Locators",locator)).click()
            elif str(locator).endswith("_CSS"):
                  self.driver.find_element(By.CSS_SELECTOR,configreader.readConfig("Reg Locators",locator)).click()
            elif str(locator).endswith("ID"):
                  self.driver.find_element(By.ID, configreader.readConfig("Reg Locators", locator)).click()

      def type(self,locator, value):
            if str(locator).endswith("_Xpath"):
                  self.driver.find_element(By.XPATH,configreader.readConfig("Reg Locators",locator)).send_keys(value)
            elif str(locator).endswith("_CSS"):
                  self.driver.find_element(By.CSS_SELECTOR,configreader.readConfig("Reg Locators",locator)).send_keys(value)
            elif str(locator).endswith("ID"):
                  self.driver.find_element(By.ID, configreader.readConfig("Reg Locators", locator)).send_keys(value)

      def select(self,locator,value):
            global dropdown
            if str(locator).endswith("_Xpath"):
                  dropdown = self.driver.find_element(By.XPATH,configreader.readConfig("Reg Locators",locator))
            elif str(locator).endswith("_CSS"):
                  dropdown = self.driver.find_element(By.CSS_SELECTOR,configreader.readConfig("Reg Locators",locator))
            elif str(locator).endswith("ID"):
                  dropdown =self.driver.find_element(By.ID, configreader.readConfig("Reg Locators", locator))

            select = Select(dropdown)
            select.select_by_visible_text(value)

      def hover(self, locator):

            if str(locator).endswith("_Xpath"):
                  element = self.driver.find_element(By.XPATH, configreader.readConfig("Reg Locators", locator))
            elif str(locator).endswith("_CSS"):
                  element = self.driver.find_element(By.CSS_SELECTOR, configreader.readConfig("Reg Locators", locator))
            elif str(locator).endswith("ID"):
                  element = self.driver.find_element(By.ID, configreader.readConfig("Reg Locators", locator))

            action=ActionChains(self.driver)
            action.move_to_element(element).perform()