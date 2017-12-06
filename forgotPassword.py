import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class flyboard(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_newUser(self):
       username="mandeepsingh6"
       password="singh123"
       email="mandeepsingh@unomaha.edu"

       driver = self.driver
       driver.maximize_window()
       driver.get("http://manmohanrathore.pythonanywhere.com")
       time.sleep(2)
       elem = driver.find_element_by_xpath("//*[@id='navbarCollapse']/ul[2]/li[1]/a").click()
       time.sleep(2)
       elem = driver.find_element_by_xpath("/html/body/div[1]/div/form/p/a").click()
       time.sleep(2)
       elem= driver.find_element_by_id("id_email")
       elem.send_keys(email)
       time.sleep(2)
       elem = driver.find_element_by_xpath("/html/body/div/div/div/form/input[3]").click()
       time.sleep(3)




   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()
