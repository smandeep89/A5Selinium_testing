import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class flyboard(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_login(self):
       user = "instructor"
       pwd = "instructor1a"
       driver = self.driver
       driver.maximize_window()
       driver.get("http://manmohanrathore.pythonanywhere.com")
       time.sleep(2)
       elem= driver.find_element_by_xpath("//*[@id='navbarCollapse']/ul[2]/li[1]/a").click()

       elem = driver.find_element_by_name("username")
       elem.send_keys(user)
       time.sleep(1)
       elem = driver.find_element_by_name("password")
       elem.send_keys(pwd)
       time.sleep(1)
       elem = driver.find_element_by_xpath("/html/body/div[1]/div/form/input[4]").click()
       time.sleep(5)


   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()
