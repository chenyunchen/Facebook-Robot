#encoding: utf-8

import time
import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Login
print "\r"
print "[Robot] Facebook Like"
print "\r"
email = raw_input("Email: ")
password = getpass.getpass()
print "\r"
print "https://www.facebook.com/(Who post want to like)"
print "【Like: Alex.YunChen】"
person = raw_input("Who: ")
print "\r"

driver = webdriver.Firefox()
driver.get("http://www.facebook.com")
elem = driver.find_element_by_id("email")
elem.send_keys(email)
elem = driver.find_element_by_id("pass")
elem.send_keys(password)
elem.send_keys(Keys.RETURN)
time.sleep(5)
driver.get("http://www.facebook.com/"+person)

# Like's click numbers in range(10)
for i in range(10):
  elem = driver.find_element_by_link_text("Like")
  elem.click()
  time.sleep(10)

driver.close()
