#!/usr/bin/env python
# -*-coding:utf-8-*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

os.environ["PATH"] += os.pathsep + os.path.dirname(os.path.realpath(__file__))
driver = webdriver.PhantomJS()
driver.get("https://gw.ict.ac.cn/cgi-bin/srun_portal")
print(driver.page_source)
name = driver.find_element_by_id("username")
name.send_keys('myusername')
password = driver.find_element_by_id('password')
password.send_keys('mypassword')
btn = driver.find_element_by_class_name('btn-login')
btn.click()
#password.send_keys(Keys.RETURN)
time.sleep(1)
driver.quit()
