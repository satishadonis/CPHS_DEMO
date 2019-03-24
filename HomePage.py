from Locators.locators import locators
class HomePage():

    def __init__(self,driver):
        self.driver = driver

        self.toggle_id = locators.toggle_id
        self.log_out = locators.log_out

    def click_Toggle(self):
        self.driver.find_element_by_xpath(self.toggle_id).click()

    def click_logout(self):
        self.driver.find_element_by_xpath(self.log_out).click()