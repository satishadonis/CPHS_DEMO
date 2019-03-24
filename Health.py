from Locators.locators import locators
from Pages.loginpage import Loginpage


class personal():
    def __init__(self,driver):
        self.driver = driver
        self.personal_contact = locators.personal_contact

    def click_personal_contact(self):
        self.driver.find_element_by_id(self.personal_contact).click()


