#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from selenium import webdriver
import io
import os, sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.olx.bg/account/"
URLadd = "https://www.olx.bg/adding/"
textr = io.open("zaglаvie.txt", encoding="utf-8", mode = "r")
zaglavie = textr.readlines()

 
driver = webdriver.Firefox()
driver.get(URL)
driver.find_element_by_id("userEmail").send_keys("my@gmail.com")
driver.find_element_by_id("userPass").send_keys("88888")
driver.find_element_by_id("se_userLogin").click()
driver.get(URLadd)
driver.find_element_by_id("add-title").send_keys("Prodawam laptop")
driver.find_element_by_id("choose-category-ilu").click()
driver.find_element_by_id('cat-632').click()
driver.find_element_by_link_text('Компютри').click()
driver.find_element_by_link_text('Телевизори').click()
driver.find_element_by_name("data[param_price][1]").send_keys("200")
driver.execute_script("document.getElementById('fancybox-overlay').style.display = 'none';")
driver.execute_script("document.getElementById('cookiesBar').style.display = 'none';")
driver.find_element_by_id('targetparam147').click()
driver.find_element_by_link_text('използвано').click()
driver.find_element_by_id('targetid_private_business').click()
driver.find_element_by_link_text('Частна').click()
driver.find_element_by_name("data[description]").send_keys("Blagodarq wi za otziw`iwostta prosto pokazwam na baba mi kak da si puska obqwa. ")
driver.find_element_by_id("show-gallery-html").click()
elm = driver.find_element_by_xpath("//input[@name='image[1]']")
elm.send_keys(os.getcwd() + "/laptop1.jpeg")
driver.find_element_by_name("data[city]").send_keys("s. Trud, Oblast Plowdiw")
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "autosuggest-geo-ul")))
driver.find_element_by_id("autosuggest-geo-ul").click()
#driver.find_element_by_id("add-person").send_keys("Mariq Penkowska")
#driver.find_element_by_name("data[phone]").send_keys("0882633225")
driver.find_element_by_id("save").click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "qa-button-promo-without")))
driver.find_element_by_link_text('Без промотиране').click()

textr.close()
