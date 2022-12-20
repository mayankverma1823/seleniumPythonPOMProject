from Pages.BasePage import BasePage


class NewCarHomePage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    def hyundai(self):
        self.click("Hyundai_Xpath")

    def mahindra(self):
        self.click("Mahindra_Xpath")

    def jeep(self):
        self.click("Jeep_Xpath")

    def honda(self):
        self.click("Honda_Xpath")