from appium import webdriver
from selenium.webdriver.common.by import By
import unittest
from time import sleep

desired_cap = {
  "platformName": "Android",
  "platformVersion": "11",
  "deviceName": "R9BMA09X2AJ",
}

driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)

driver.find_element(By.XPATH,'//android.widget.TextView[@content-desc="Petsi"]').click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//android.widget.ImageView[@content-desc="Tab 3 of 5"]').click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//android.widget.Button[@content-desc="Report Missing"]').click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//android.widget.ImageView[@content-desc="Sign in with email"]').click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//android.widget.EditText[@text="Email"]').click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//android.widget.EditText[@text="Email"]').send_keys('test@gmail.com')
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//android.widget.EditText[@text="Password"]').click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//android.widget.EditText[@text="Password"]').send_keys('test1234')
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//android.widget.ImageView[@bounds="[579,427][688,511]"]').click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//android.widget.Button[@content-desc="Login"]').click()











