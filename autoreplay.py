#encoding: utf-8

import time
import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Login
print "\r"
print "[Robot] Facebook AutoReply"
print "\r"
email = raw_input("Email: ")
password = getpass.getpass()
print "\r"

driver = webdriver.Firefox()
driver.get("http://www.facebook.com")
elem = driver.find_element_by_id("email")
elem.send_keys(email)
elem = driver.find_element_by_id("pass")
elem.send_keys(password)
elem.send_keys(Keys.RETURN)
time.sleep(5)
while True:
  try:
    time.sleep(1)
    elem = driver.find_element_by_css_selector("div textarea._552m")
    elem.send_keys(u"[Auto]Sorry, I not on my seat now.")
    elem.send_keys(Keys.RETURN)
    elem.send_keys(Keys.ESCAPE)
  except:
    pass
