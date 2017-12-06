import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class flyboard(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_newUser(self):
       username="mandeepsingh9"
       password="singh123"
       email="mandeepsingh@unomaha.edu"

       driver = self.driver
       driver.maximize_window()
       driver.get("http://manmohanrathore.pythonanywhere.com")
       time.sleep(2)
       elem = driver.find_element_by_xpath("//*[@id='navbarCollapse']/ul[2]/li[1]/a").click()
       time.sleep(2)
       elem = driver.find_element_by_xpath("/html/body/div[1]/div/form/a").click()
       time.sleep(2)
       elem= driver.find_element_by_name("username")
       elem.send_keys(username)
       time.sleep(2)
       elem=driver.find_element_by_name("email")
       elem.send_keys(email)
       time.sleep(2)
       elem=driver.find_element_by_name("password1")
       elem.send_keys(password)
       elem = driver.find_element_by_name("password2")
       elem.send_keys(password)
       time.sleep(2)
       elem = driver.find_element_by_xpath("/html/body/div/form/button").click()
       time.sleep(3)

       elem = driver.find_element_by_xpath("//*[@id='navbarCollapse']/ul[2]/li[1]/a").click()
       time.sleep(3)
       elem = driver.find_element_by_name("username")
       elem.send_keys(username)
       time.sleep(2)
       elem = driver.find_element_by_name("password")
       elem.send_keys(password)
       time.sleep(2)

       elem = driver.find_element_by_xpath("/html/body/div[1]/div/form/input[4]").click()
       time.sleep(4)




   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()
