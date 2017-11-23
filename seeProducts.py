import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class flyboard(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_seeProducts(self):
       user = "instructor"
       pwd = "instructor1a"
       driver = self.driver
       driver.maximize_window()
       driver.get("http://abrarblog.pythonanywhere.com")
       time.sleep(5)
       elem= driver.find_element_by_xpath("//*[@id='navbarNavDropdown']/ul/ul").click()
       elem = driver.find_element_by_css_selector("#content > div.wrapper > form > input:nth-child(3)")
       elem.send_keys(user)
       elem = driver.find_element_by_css_selector("#content > div.wrapper > form > input:nth-child(4)")
       elem.send_keys(pwd)
       elem= driver.find_element_by_css_selector("#content > div.wrapper > form > input.btn.btn-lg.btn-primary.btn-block").click()
       time.sleep(5)
       elem = driver.find_element_by_link_text("SKATEBOARDS").click()
       time.sleep(3)
       elem = driver.find_element_by_link_text("SHOES").click()
       time.sleep(3)
       elem = driver.find_element_by_link_text("ACCESSORIES").click()
       time.sleep(3)
       elem = driver.find_element_by_link_text("BLOWOUT DEALS").click()
       time.sleep(3)

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()
