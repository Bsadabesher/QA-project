import unittest
from appium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class AppiumTest(unittest.TestCase):
    dc = {}
    driver = None

    def setUp(self):
        self.dc['platformVersion'] = '11'
        self.dc['platformName'] = 'Android'
        self.dc['deviceName'] = 'R9BMA09X2AJ'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.dc)

    def testFirstAutomation(self):
        self.driver.find_element(By.XPATH, '//android.widget.TextView[@content-desc="Petsi"]').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ACCESSIBILITY_ID,'For adoption').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH,'//android.view.View[@bounds="[24,332][360,705]"]').click()
        self.driver.find_element(By.ACCESSIBILITY_ID,'Call').click()



    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
