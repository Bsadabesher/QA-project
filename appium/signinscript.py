import unittest
from appium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class AppiumTest(unittest.TestCase):
    dc = {}
    driver = None

    def setUp(self):
        # This is the Application and ‘app’ desired capability to specify a path to Appium.
        # self.dc['app'] = "c:\\eribank.apk"
        # appPackage and appActivity  desired capability specify app details to Appium
        # self.dc['appPackage'] = "com.experitest.ExperiBank"
        # self.dc['appActivity'] = ".LoginActivity"
        # platformName desired capability specify platform detail to Appium
        self.dc['platformVersion'] = '11'
        self.dc['platformName'] = 'Android'
        # deviceName desired capability specify the device id detail to Appium
        # device id is got from running adb devices command in PC
        self.dc['deviceName'] = 'R9BMA09X2AJ'
        # Creating the Driver by passing Desired Capabilities.
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.dc)

    def testFirstAutomation(self):

        # Find location of Elements and perform action.
        self.driver.find_element(By.XPATH, '//android.widget.TextView[@content-desc="Petsi"]').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH,'//android.widget.ImageView[@bounds="[0,57][98,155]"]').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ACCESSIBILITY_ID,'Login').click()
        sleep(1)
        self.driver.find_element(By.ACCESSIBILITY_ID,'Sign in with Google').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH,'//android.widget.TextView[@text="sada Besher"]').click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()