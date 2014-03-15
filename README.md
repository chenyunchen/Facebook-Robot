#Facebook-Robot

Use Python&amp;Webdriver to AUTO-Reply、Post、Like、Message on Facebook
There are four easy example to help you to know. 

##Selenium

Webdriver can create a real browser and make real click just like your mouse!

It support java、javasript、ruby、python...etc 

You can watch more detail on [Webdrivar](http://docs.seleniumhq.org/projects/webdriver/)

##Webdriver

```python
from selenium import webdriver
driver = webdriver.Firefox()
```

Import webdriver from selenium and create browser on your code.

Selenium can support chrome、firefox or more.

```
webdriver.Firefox
webdriver.FirefoxProfile
webdriver.Chrome
webdriver.ChromeOptions
webdriver.Ie
webdriver.Opera
```

But you have to notice that there must have these browser on your system.

##Facebook Login

```python
driver.get("http://www.facebook.com")
elem = driver.find_element_by_id("email")
elem.send_keys(email)
elem = driver.find_element_by_id("pass")
elem.send_keys(password)
elem.send_keys(Keys.RETURN)
time.sleep(5)
```

Now,we use driver to get the page first.

Find DOM in the page and get the object, then you can create event you want.

Selenium have many ways to help you find the element,Here you can use...

```
find_element_by_id
find_element_by_name
find_element_by_xpath
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector
```

Xpath is a easy way to find the Object.

I recommand Firefox XPath Checker 0.4.4:An interactive editor for XPath expressions.

Watch more detail about editor on [XPath Checker]("https://addons.mozilla.org/zh-tw/firefox/addon/xpath-checker/")

On Facebook, button's or textarea's "id" and "name" are both change after you use it,
so I only use tag_name、link_text、class_name to get it.

And using send_keys("What you want to send here")

```python
Enter = Keys.RETURN
ESC = Keys.ESCAPE
```

###Time

```python
print 【Like: 2014-03-10 22:43】
temtime = str(datetime.now()).split(".")[0].split(":")
systemtime = temtime[0]+":"+temtime[1]
if systemtime == yourtime:
    pass
```
Here is an easy way to rule your time form and judge.

###AutoReply

```python
elem = driver.find_element_by_css_selector("div textarea._552m")
elem.send_keys(u"[Auto]Sorry, I not on my seat now.")
elem.send_keys(Keys.RETURN)
```
css_selector to find element.

So you can give textarea with css class _552m which under the div tag! 

###Like

```python
elem = driver.find_element_by_link_text("Like")
elem.click()
```

Find Link text "Like" <a href="">Like</a>.

###Message

```python
driver.get("https://facebook.com/messages/"+person)
elem = driver.find_element_by_css_selector("div textarea.uiTextareaNoResize")
elem.send_keys(u"Put your message here")
elem.send_keys(Keys.RETURN)
```

If you want to use some special character, use unicode type for your text.

###Post

```python
driver.get("https://www.facebook.com/"+person)
elem = driver.find_element_by_tag_name("textarea")
elem.click()
elem.send_keys(u"Put your content here.")
elem.send_keys(Keys.RETURN)
driver.find_element_by_xpath('//button[text()="Post"]').click()
```

Find tage name like:"textarea" "input" "button" or more

Element by xpath: you can use Firefox-XPath Checker to help you more easily to find it.

###Warning

```python
time.sleep(5)
driver.close()
```
sleep()

Sometimes you have to make sleep in your connect.
Because the web page may not load already before you send the keys(text).

close()

Close the browser in the final to release memory.
