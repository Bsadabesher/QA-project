
from appium import webdriver
from selenium.webdriver.common.by import By

desired_cap = {
    "platformName": "Android",
    "appium:platformVersion": "11",
    "appium:platformDivice": "R9WN30FW70J",

}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)
driver.find_element(By.XPATH, '//android.widget.TextView[@content-desc="Michu Dev"]').click()
driver.implicitly_wait(10)


def singin():
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/phone').send_keys('0913396213')
    driver.implicitly_wait(10)
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/password').send_keys('123456')
    driver.implicitly_wait(10)
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/button').click()
    driver.implicitly_wait(15)

def basicinfo():
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/name').send_keys('no one')
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/spinAge').click()
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                  '.ListView/android.widget.LinearLayout[4]/android.widget.TextView').click()
    driver.implicitly_wait(10)
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/gender_spinner').click()
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                  '.ListView/android.widget.LinearLayout[2]/android.widget.TextView').click()
    driver.implicitly_wait(10)
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/email').send_keys('nonoe@gmail.com')
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/next').click()
    driver.implicitly_wait(5)

def Basicinfo2():

    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/spinRegion').click()
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                  '.ListView/android.widget.LinearLayout[8]/android.widget.TextView').click()
    driver.implicitly_wait(10)
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/spinCity').click()
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                  '.ListView/android.widget.LinearLayout[2]/android.widget.TextView').click()

    driver.implicitly_wait(10)
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/zone').send_keys('gulele')
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/woreda').send_keys('09')
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/house').send_keys('w/123')
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/typeOfId').click()
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                  '.ListView/android.widget.LinearLayout[2]/android.widget.TextView').click()
    driver.implicitly_wait(10)
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/idNumber').send_keys('526341')
    driver.implicitly_wait(5)

    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/maritalStatus').click()
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                  '.ListView/android.widget.LinearLayout[2]/android.widget.TextView').click()
    driver.implicitly_wait(10)
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/educationLevel').click()
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                  '.ListView/android.widget.LinearLayout[6]/android.widget.TextView').click()
    driver.implicitly_wait(10)
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/emergencyContact').send_keys('0921635584')
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/next').click()
    driver.implicitly_wait(15)


def Businessdetails():

    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/tin').send_keys('1111559963')
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/tinSpouse').send_keys('0234569638')
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/accountType').click()
    driver.implicitly_wait(15)
    driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                  '.ListView/android.widget.LinearLayout[1]/android.widget.TextView').click()
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/coopSavingAcNo').send_keys('1054200010945')
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/tradeName').send_keys('opps')
    driver.implicitly_wait(15)
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/businessLevel').click()
    driver.implicitly_wait(15)
    driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                  '.ListView/android.widget.LinearLayout[2]/android.widget.TextView').click()
    driver.implicitly_wait(15)
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/layout_date_picker').click()
    driver.implicitly_wait(15)
    driver.find_element(By.ID, 'android:id/button1').click()
    driver.implicitly_wait(15)
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/employeeCount').send_keys('5000')
    driver.implicitly_wait(15)
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/spin_source').click()
    driver.implicitly_wait(15)
    driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                  '.ListView/android.widget.LinearLayout[3]/android.widget.TextView').click()
    driver.implicitly_wait(15)
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/businessSector').click()
    driver.implicitly_wait(15)
    driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                  '.ListView/android.widget.LinearLayout[4]/android.widget.TextView').click()
    driver.implicitly_wait(15)
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/businessLine').click()
    driver.implicitly_wait(15)
    driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                  '.ListView/android.widget.LinearLayout[13]/android.widget.TextView').click()
    driver.implicitly_wait(15)
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/businessForm').click()
    driver.implicitly_wait(15)
    driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                  '.ListView/android.widget.LinearLayout[8]/android.widget.TextView').click()
    driver.implicitly_wait(15)
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/startingCapital').send_keys('10')
    driver.implicitly_wait(5)

    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/currentCapital').send_keys('50')
    driver.implicitly_wait(15)
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/annualIncome').send_keys('1')
    driver.implicitly_wait(15)
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/annualProfit').send_keys('0')
    driver.implicitly_wait(15)
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/next').click()
    driver.implicitly_wait(15)


def BusinessDetel2():
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/spinRegion').click()
    driver.implicitly_wait(15)
    driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                  '.ListView/android.widget.LinearLayout[8]/android.widget.TextView').click()
    driver.implicitly_wait(15)
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/spinCity').click()
    driver.implicitly_wait(15)
    driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                  '.ListView/android.widget.LinearLayout/android.widget.TextView').click()
    driver.implicitly_wait(15)
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/zone').send_keys('gulele')
    driver.implicitly_wait(15)
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/woreda').send_keys('100')
    driver.implicitly_wait(15)
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/house').send_keys('!@#$%^&*()_:MNGV  <KK')
    driver.implicitly_wait(15)
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/next').click()
    driver.implicitly_wait(15)


def BusinessDetel3():

    driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                  '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                                  '.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget'
                                  '.Spinner/android.widget.TextView').click()
    driver.implicitly_wait(15)
    driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                  '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                                  '.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android'
                                  '.widget.ListView/android.widget.RelativeLayout[2]/android.widget.CheckBox').click()
    driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                  '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                                  '.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android'
                                  '.widget.ListView/android.widget.RelativeLayout[4]/android.widget.CheckBox').click()
    driver.implicitly_wait(15)
    driver.find_element(By.ID, 'android:id/button1').click()
    driver.implicitly_wait(15)
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/submit').click()
    driver.implicitly_wait(15)


def UploadDoc():
    driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                  '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                                  '.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android'
                                  '.widget.LinearLayout['
                                  '6]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ImageView'
                                  '').click()
    driver.implicitly_wait(15)
    driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                  '.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view'
                                  '.ViewGroup/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup'
                                  '/android.widget.FrameLayout/android.widget.FrameLayout['
                                  '2]/android.widget.LinearLayout/android.view.ViewGroup/androidx.recyclerview.widget'
                                  '.RecyclerView/android.widget.LinearLayout['
                                  '5]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget'
                                  '.LinearLayout[1]/android.widget.TextView').click()
    driver.implicitly_wait(15)
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/submit').click()
    driver.implicitly_wait(15)


def Reviewloan():
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/checkBox').click()
    driver.implicitly_wait(15)
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/accept').click()
    driver.implicitly_wait(15)


def loancontract():
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/downloadButton').click()
    driver.implicitly_wait(15)


def verification():
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/iv_back').click()
    driver.implicitly_wait(15)


def loanstatus():
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/viewContract').click()
    driver.implicitly_wait(15)
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/iv_back').click()
    driver.implicitly_wait(15)


def makepayment():
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/makePayment').click()
    driver.implicitly_wait(10)
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/eBirrButton').click()
    driver.implicitly_wait(10)


def payfromAcount():
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/checkBalance').click()
    driver.implicitly_wait(15)
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/paymentAmount').send_keys('25800.00')
    driver.implicitly_wait(10)
    driver.find_element(By.ID, 'com.kifiya.digital.lending.dev:id/button').click()


singin()
basicinfo()
Basicinfo2()
Businessdetails()
BusinessDetel2()
BusinessDetel3()
UploadDoc()
Reviewloan()
loancontract()
loanstatus()
makepayment()
payfromAcount()
