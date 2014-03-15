#encoding: utf-8

import time
import getpass
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Login
print "\r"
print "[Robot] Facebook Message"
print "\r"
email = raw_input("Email: ")
password = getpass.getpass()
print "\r"
print "https://www.facebook.com/messages/(Who you want to talk)"
print "【Like: Alex.YunChen】"
person = raw_input("Who: ")
print "\r"
print "What time you want to leave your message?"
print "【Like: 2014-03-10 22:43】"
yourtime = raw_input("Time: ")
print "\r"

#Message
while True:
  temtime = str(datetime.now()).split(".")[0].split(":")
  systemtime = temtime[0]+":"+temtime[1]
  if systemtime == yourtime:
    driver = webdriver.Firefox()
    driver.get("http://www.facebook.com")
    elem = driver.find_element_by_id("email")
    elem.send_keys(email)
    elem = driver.find_element_by_id("pass")
    elem.send_keys(password)
    elem.send_keys(Keys.RETURN)
    time.sleep(5)
    driver.get("https://facebook.com/messages/"+person)
    elem = driver.find_element_by_css_selector("div textarea.uiTextareaNoResize")
    #Put your message here
    elem.send_keys(u"Put your message here")
    elem.send_keys(Keys.RETURN)
    driver.close()
    break
  else:
    time.sleep(5)
