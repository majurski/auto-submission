#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from selenium import webdriver
import io
import os, sys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://mentormate.com/bg/careers/full-stack-developer-python-and-aws/?city=%D0%9F%D0%BB%D0%BE%D0%B2%D0%B4%D0%B8%D0%B2"
firstname = "Minko"
lastname = "Terziyski"
email = "example@gmail.com"
phone = "064556456456456"
filename = os.getcwd() + "/CV-English.pdf"

def apply():
	driver = webdriver.Firefox()
	driver.get(URL)
	driver.find_element_by_name("firstname").send_keys(firstname)
	driver.find_element_by_name("lastname").send_keys(lastname)
	driver.find_element_by_name("email").send_keys(email)
	driver.find_element_by_name("phone").send_keys(phone)
	driver.execute_script("document.getElementById('hs-en-cookie-confirmation-buttons-area').style.display = 'none';")
	driver.execute_script("document.getElementById('hs-eu-cookie-confirmation-inner').style.display = 'none';")
	driver.find_element_by_tag_name('input[id^="bg_upload"]').send_keys(filename)
	driver.find_element_by_tag_name('textarea[id^="message"]').send_keys("The link of the video is here https://www.youtube.com/watch?v=A8LkZbOsDrE&feature=youtu.be")
	driver.execute_script("document.getElementsByClassName('hs-form-booleancheckbox-display')[1].children[1].click()")
	driver.execute_script("document.getElementsByClassName('hs-button')[0].click()")

for _ in range(1):
	sleep(10)
	apply()
