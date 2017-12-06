import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class flyboard(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_admin(self):
       user = "instructor"
       pwd = "instructor1a"
       driver = self.driver
       driver.maximize_window()
       driver.get("http://manmohanrathore.pythonanywhere.com/admin/login/?next=/admin/")
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       elem.send_keys(Keys.RETURN)
       time.sleep(5)
       elem = driver.find_element_by_xpath("//*[@id='content-main']/div[5]/table/tbody/tr[2]/th/a")
       elem.click()
       time.sleep(4)
       elem = driver.find_element_by_xpath("//*[@id='site-name']/a").click()
       time.sleep(4)
       elem = driver.find_element_by_xpath("//*[@id='content-main']/div[5]/table/tbody/tr[1]/th/a").click()
       time.sleep(4)
       elem = driver.find_element_by_xpath("//*[@id='site-name']/a").click()
       elem = driver.find_element_by_xpath("//*[@id='content-main']/div[4]/table/tbody/tr/th/a").click()
       time.sleep(4)
       driver.get("http://manmohanrathore.pythonanywhere.com/")
       assert "Logged In"
       time.sleep(5)

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()
