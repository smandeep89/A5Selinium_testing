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
       driver.get("http://manmohanrathore.pythonanywhere.com/")
       time.sleep(5)
       elem= driver.find_element_by_xpath("//*[@id='navbarCollapse']/ul[1]/li[1]/a").click()
       time.sleep(1)
       elem = driver.find_element_by_xpath("//*[@id='navbarCollapse']/ul[1]/li[2]/a").click()
       time.sleep(1)
       elem = driver.find_element_by_xpath("//*[@id='navbarCollapse']/ul[1]/li[3]/a").click()
       time.sleep(1)
       elem = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/p[2]/a").click()
       elem = driver.find_element_by_name("username")
       elem.send_keys(user)
       elem = driver.find_element_by_name("password")
       elem.send_keys(pwd)
       elem = driver.find_element_by_xpath("/html/body/div[1]/div/form/input[4]").click()
       time.sleep(5)



   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()
