from selenium import webdriver
import time
import unittest
# import sys
# import os
# sys.path.append(os.path.join(os.path.dirname(__file__),"...","..."))
from Pages.loginpage import Loginpage
from Pages.HomePage import HomePage
import HtmlTestRunner



class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):


        # driver = webdriver.Firefox(executable_path='D:\Testing\Automation\Python\Automation\CPHS\geckodriver-v0.24.0-win64\geckodriver.exe')
        cls.driver = webdriver.Chrome(executable_path='D:\Testing\Automation\Python\Automation\CPHS\chromedriver_win32\chromedriver.exe')

        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get('http://svwp15:82/login')
        login = Loginpage(driver)
        login.enter_username("woodjudy")
        login.enter_password("Span@123")
        login.click_login()

    def logout(self):
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_Toggle()
        # print("HI")
        driver.save_screenshot('D:/Testing/Automation/Python/Automation/CPHS/s.png')
        homepage.click_logout()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.implicitly_wait(10)
        cls.driver.quit()
        print("Test Completed Successfully")

if __name__ == '__main__':
    unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output='D:/Testing/Automation/Python/Automation/CPHS_DEMO/Reports'))

    # unittest.main(testRunner)
    # unittest.main()


    # suite = unittest.TestSuite()
    # suite.addTest(unittest.makeSuite(LoginTest))
    # dateTimeStamp = time.strftime('%Y%m%d_%H_%M_%S')
    # buf = file("TestReport" + "_" + dateTimeStamp + ".html", 'wb')
    # runner = LoginTest.HTMLTestRunner(stream=buf,title='Test the Report',description='Result of tests')
    # runner.run(suite)



    # unittest.main()
# testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/Testing/Automation/Python/Automation/CPHS_DEMO/Reports')