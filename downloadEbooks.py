from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
page = requests.get("https://english-e-reader.net/level/intermediate-plus")

soup = BeautifulSoup(page.content, 'html.parser')
for a in soup.find_all('a', href=True):
    if("/book" in a['href']):
        print(a['href'])
        driver.get("https://english-e-reader.net"+a['href'])
        
        elements = driver.find_elements_by_class_name("cc-window")
        for e in elements:
            driver.execute_script("""
        var element = arguments[0];
        element.parentNode.removeChild(element);
        """, e)
            
        elements = driver.find_elements_by_class_name("onesignal-slidedown-dialog")
        for e in elements:
            driver.execute_script("""
        var element = arguments[0];
        element.parentNode.removeChild(element);
        """, e)
        # element = driver.find_element_by_class_name('cc-window')
        # driver.execute_script("""
        # var element = arguments[0];
        # element.parentNode.removeChild(element);
        # """, element)

        
        driver.find_element(By.ID,"download").click()
driver.close()
        
