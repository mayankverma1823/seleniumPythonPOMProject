import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from  webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeDriver
from selenium.webdriver.firefox.service import Service as FirefoxDriver

import Utilities


@pytest.fixture(params=["chrome"],scope="function")
def get_browser(request):
    global driver
    if request.param == "chrome":
        driver = webdriver.Chrome(service=ChromeDriver(ChromeDriverManager().install()))
    if request.param == "firefox":
        driver = webdriver.Firefox(service=FirefoxDriver(GeckoDriverManager().install()))
    request.cls.driver = driver
    driver.get(Utilities.configreader.readConfig("Basic Information", "carwale"))
    #driver.get("https://way2automation.com/way2auto_jquery/index.php")
    driver.maximize_window()
    driver.implicitly_wait(4)
    yield driver
    driver.quit()
