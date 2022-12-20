from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Pages.BasePage import BasePage
from Utilities import configreader


class RegistrationPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    def fillform(self,name,phone,email,country,city,username,password):
        self.type("Name_Xpath",name)
        self.type("Phone_Xpath",phone)
        self.type("Email_Xapth",email)
        self.select("Country_Xpath",country)
        self.type("City_Xpath",city)
        self.type("Username_Xpath",username)
        self.type("Password_CSS", password)
        self.click("Submit_Xpath")