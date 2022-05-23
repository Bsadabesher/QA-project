import unittest
import requests
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys


class PetsmartUITesting(unittest.TestCase):
    """A Class for all the UI testing to be done with selenium."""

    def setUp(self):
        """Initialize webdriver."""
        self.driver = webdriver.Firefox()
        self.base_url = "http://www.petsmart.com"

    # def test_title_in_petsmart_org(self):
    #     """Test if the name PetSmart is mentioned in the title."""
    #     """Important for SEO."""
    #     driver = self.driver
    #     driver.get(self.base_url)
    #     self.assertIn("PetSmart", driver.title)

    # def test_gdpr_cookie_notice(self):
    #     """Test gdpr complice by checking cookie notice."""
    #     driver = self.driver
    #     driver.get(self.base_url)
    #     driver.implicitly_wait(20)
    #     elem = driver.find_element_by_id("onetrust-consent-sdk")
    #     gdpr_compliance_text_segment = "This website uses cookies"
    #     self.assertIn(gdpr_compliance_text_segment, elem.text)

    # def test_search_functionality_invalid(self):
    #     """Test the search functionality."""
    #     """Return no results warning if given invalid."""
    #     driver = self.driver
    #     driver.get(self.base_url)
    #     driver.implicitly_wait(20)
    #     elem = driver.find_element_by_name("q")
    #     elem.send_keys("momomdoamdadswerwer")
    #     elem.send_keys(Keys.RETURN)
    #     driver.implicitly_wait(20)
    #     elem2 = driver.find_element_by_class_name("search-result-msg-wrapper")
    #     # elem2 = driver.find_element_by_class_name("page-content")
    #     self.assertIn("no results", elem2.text)

    def test_valid_search_functionality(self):
        """Test the search functionality."""
        """Don't show no results warning if given valid input."""
        driver = self.driver
        driver.get(self.base_url)
        driver.implicitly_wait(20)
        elem = driver.find_element_by_name("q")
        elem.send_keys("food")
        elem.send_keys(Keys.RETURN)
        driver.implicitly_wait(20)
        elem2 = driver.find_element_by_class_name("showing-result-msg")

    def test_cart_button_functionaliy(self):
        """Test hover functionality in menu bar."""
        driver = self.driver
        driver.get(self.base_url)
        action = ActionChains(driver)
        elem1 = driver.find_element_by_class_name("icon-cart")
        driver.implicitly_wait(15)
        action.move_to_element(elem1).click().perform()
        driver.implicitly_wait(15)
        elem2 = self.driver.find_element_by_class_name("cartheader")


    # def test_cart_button_functionaliy(self):
    #     """Test hover functionality in menu bar."""
    #     driver = self.driver
    #     driver.get(self.base_url)
    #     action = ActionChains(driver)
    #     elem1 = driver.find_element_by_class_name("icon-cart")
    #     driver.implicitly_wait(15)
    #     action.move_to_element(elem1).click().perform()
    #     driver.implicitly_wait(15)
    #     elem2 = self.driver.find_element_by_class_name("cartheader")

    # def test_hover_functionality_shop_by_pet_dog(self):
    #     """Test hover functionality in menu bar."""
    #     driver = self.driver
    #     driver.get(self.base_url)
    #     action = ActionChains(driver)
    #     elem1 = driver.find_element_by_link_text("shop by pet")
    #     action.move_to_element(elem1).perform()
    #     driver.implicitly_wait(5)
    #     # elem2 = driver.find_element_by_link_text("cat")
    #     # action.move_to_element(elem2).perform()
    #     elem3 = driver.find_element_by_link_text("Dry Food")
    #     action.move_to_element(elem3).click().perform()
    #     elem4 = self.driver.find_element_by_class_name("heading")
    #     self.assertIn("Dry Dog Food", elem4.text)

    # def test_hover_functionality_shop_by_pet_fish(self):
    #     """Test hover functionality in menu bar."""
    #     driver = self.driver
    #     driver.get(self.base_url)
    #     action = ActionChains(driver)
    #     elem1 = driver.find_element_by_link_text("shop by pet")
    #     action.move_to_element(elem1).perform()
    #     driver.implicitly_wait(5)
    #     elem2 = driver.find_element_by_link_text("Fish")
    #     driver.implicitly_wait(5)
    #     action.move_to_element(elem2).perform()
    #     # elem3 = driver.find_element_by_link_text("Food")
    #     # action.move_to_element(elem3).click().perform()
    #     # elem4 = self.driver.find_element_by_class_name("heading")
    #     # self.assertIn("Dry Dog Food", elem4.text)

    # def test_hover_functionality_help_contactus(self):
    #     """Test hover functionality in menu bar."""
    #     driver = self.driver
    #     driver.get(self.base_url)
    #     action = ActionChains(driver)
    #     elem1 = driver.find_element_by_link_text("help")
    #     action.move_to_element(elem1).perform()
    #     driver.implicitly_wait(5)
    #     elem2 = driver.find_element_by_link_text("Contact Us")
    #     action.move_to_element(elem2).click().perform()
    #     elem3 = self.driver.find_element_by_class_name("my-account-header")
    #     self.assertIn("help & contact us", elem3.text)

    # def test_hover_functionality_track_your_order(self):
    #     """Test hover functionality in menu bar."""
    #     driver = self.driver
    #     driver.get(self.base_url)
    #     action = ActionChains(driver)
    #     elem1 = driver.find_element_by_link_text("help")
    #     action.move_to_element(elem1).perform()
    #     driver.implicitly_wait(5)
    #     elem2 = driver.find_element_by_link_text("Track Your Order")
    #     action.move_to_element(elem2).click().perform()
    #     elem3 = self.driver.find_element_by_class_name("my-account-header")
    #     self.assertIn("track your order", elem3.text)

    # def test_for_broken_links(self):
    #     """Test for broken links by sending requests to all link"""
    #     driver = self.driver
    #     driver.get(self.base_url)
    #     links = driver.find_elements_by_css_selector("a")
    #     for link in links:
    #         r = requests.head(link.get_attribute('href'))
    #         print(link.get_attribute('href'), r.status_code)
    #         # assert not 400 <= r.status_code

    def tearDown(self):
        """Shutdown web driver when finished."""
        self.driver.close()


# execute the script
if __name__ == "__main__":
    unittest.main()
