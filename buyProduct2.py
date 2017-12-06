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
      # time.sleep(2)
       elem= driver.find_element_by_xpath("//*[@id='navbarCollapse']/ul[2]/li[1]/a").click()
       elem = driver.find_element_by_name("username")
       elem.send_keys(user)
       time.sleep(1)
       elem = driver.find_element_by_name("password")
       elem.send_keys(pwd)
       time.sleep(1)
       elem = driver.find_element_by_xpath("/html/body/div[1]/div/form/input[4]").click()
       #time.sleep(5)
       elem = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/p[2]/a").click()
       elem = driver.find_element_by_id("id_quantity")
       elem.send_keys(5)
       #time.sleep(2)
       elem = driver.find_element_by_xpath("/html/body/div/div/div/form/input[3]").click() #add to cart
      # time.sleep(4)
       elem = driver.find_element_by_xpath("/html/body/div/p/a[1]").click() #continue shopping /html/body/div/p/a[1]
      # time.sleep(2)
       elem = driver.find_element_by_xpath("//*[@id='navbarCollapse']/ul[1]/li[3]/a").click() #accessories //*[@id="navbarCollapse"]/ul[1]/li[3]/a
      # time.sleep(2)
       elem = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/p[2]/a").click() # view details of the pink tool
       #time.sleep(4)
       elem = driver.find_element_by_xpath("/html/body/div/div/div/form/input[3]").click() # add to cart /html/body/div[2]/div/div[2]/p[2]/a
       #time.sleep(2)
       elem = driver.find_element_by_xpath("/html/body/div/p/a[2]").click() # checkout click
       #time.sleep(2)
       elem = driver.find_element_by_name("first_name").send_keys("Mandeep")
       elem = driver.find_element_by_name("last_name").send_keys("Singh")
       elem = driver.find_element_by_name("email").send_keys("mandeepsingh@unomaha.edu")
       elem = driver.find_element_by_name("address").send_keys("809 S 70th plaza, Apartment 2")
       elem = driver.find_element_by_name("postal_code").send_keys(68106)
       elem = driver.find_element_by_name("city").send_keys("Omaha")
       time.sleep(3)
       elem = driver.find_element_by_xpath("/html/body/div/form/p[7]/input").click()
       elem = driver.find_element_by_xpath("/html/body/form/input[12]").click() #click on paypal /html/body/form/input[12]
       time.sleep(8)
       elem = driver.find_element_by_xpath("//*[@id='checkoutAsAGuestBtn']").click()
       time.sleep(8)
       elem = driver.find_element_by_xpath("//*[@id='cc']").send_keys("4836050602797067")
       elem = driver.find_element_by_xpath("//*[@id='expiry_value']").send_keys("09/18")
       elem = driver.find_element_by_xpath("//*[@id='cvv']").send_keys(218)
       elem = driver.find_element_by_xpath("//*[@id='firstName']").send_keys("JADEN")
       elem = driver.find_element_by_xpath("//*[@id='lastName']").send_keys("OWEN")
       elem = driver.find_element_by_xpath("//*[@id='billingLine1']").send_keys("809 S 70th Plaza, Apartment 2")
       elem = driver.find_element_by_xpath("//*[@id='billingLine2']").send_keys(2)
       elem = driver.find_element_by_xpath("//*[@id='billingCity']").send_keys("Omaha")
       elem = driver.find_element_by_xpath("//*[@id='billingState']").send_keys("Nebraska")
       elem = driver.find_element_by_xpath("//*[@id='billingPostalCode']").send_keys(68106)
       elem = driver.find_element_by_xpath("//*[@id='telephone']").send_keys("5312037029")
       elem = driver.find_element_by_xpath("//*[@id='email']").send_keys("mandeepsingh@unomaha.edu")
       time.sleep(3)
       elem = driver.find_element_by_xpath("//*[@id='guestSubmit']").click()
       time.sleep(15)
       elem = driver.find_element_by_xpath("//*[@id='notNow']").click()
       time.sleep(15)
       elem = driver.find_element_by_xpath("//*[@id='merchantReturnBtn']").click()
       time.sleep(3)
       elem = driver.find_element_by_xpath("/html/body/nav/a/img").click()
       time.sleep(3)

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()
