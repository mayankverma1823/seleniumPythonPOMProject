import time

import pytest

from Pages.CarBase import CarBase
from Pages.CarwaleHomepage import HomePage
from Testcases.BaseTest import BaseTest
import logging

from Utilities import dataProvider
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


class Test_CarWale(BaseTest):
    @pytest.mark.skip
    def test_NewCarPage(self):
        log.logger.info("Inside new car page")
        home = HomePage(self.driver)
        home.goToNewCars()

    @pytest.mark.parametrize("CarBrands,CarTitle",
                             dataProvider.get_data("CarBrand"))  # called that data with function name
    def test_selectCars(self, CarBrands,CarTitle):
        log.logger.info("Inside Car Brands")
        home = HomePage(self.driver)
        car = CarBase(self.driver)
        if CarBrands == "hyundai":
            home.goToNewCars().hyundai()
            title = car.getCarHeader()
            print(("The car title is: " + title).encode('utf8'))
            assert title == CarTitle, "Not correct title or title is not matching"
        elif CarBrands == "jeep":
            home.goToNewCars().jeep()
            title = car.getCarHeader()
            print(("The car title is: " + title).encode('utf8'))
            assert title == CarTitle, "Not correct title or title is not matching"
        elif CarBrands == "mahindra":
            home.goToNewCars().mahindra()
            title = car.getCarHeader()
            print(("The car title is: " + title).encode('utf8'))
            assert title == CarTitle, "Not correct title or title is not matching"
        elif CarBrands == "honda":
            home.goToNewCars().honda()
            title = car.getCarHeader()
            print(("The car title is: " + title).encode('utf8'))
            assert title == CarTitle, "Not correct title or title is not matching"
