import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    browser.find_element(By.NAME, "firstname").send_keys("Ivan")
    browser.find_element(By.NAME, "lastname").send_keys("Petrov")
    browser.find_element(By.NAME, "email").send_keys("email@email.com")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file.txt"
    file_path = os.path.join(current_dir, file_name)
    browser.find_element(By.ID, "file").send_keys(file_path) # send file.txt
    browser.find_element(By.CSS_SELECTOR, "button.btn-primary").click() # press submit
finally:
    time.sleep(10)
    browser.quit()
