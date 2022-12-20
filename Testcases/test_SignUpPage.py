import openpyxl
import pytest as pytest
import allure
from allure_commons.types import AttachmentType
from Pages.RegistrationPage import RegistrationPage
from Testcases.BaseTest import BaseTest
from Utilities import dataProvider
import logging
from Utilities.LogUtil import Logger

log =Logger(__name__,logging.INFO)


class Test_SignupTest(BaseTest):
        @pytest.mark.parametrize("name,phone,email,country,city,username,password", dataProvider.get_data("LoginDetails"))  # called that data with function name
        def test_Signup(self,name,phone,email,country,city,username,password):
                log.logger.info("Test Start")
                regPage=RegistrationPage(self.driver)
                regPage.fillform(name,phone,email,country,city,username,password)
                log.logger.info("Test completed")
