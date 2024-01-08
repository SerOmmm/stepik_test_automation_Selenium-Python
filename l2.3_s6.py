from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/redirect_accept.html")
    browser.find_element(By.CSS_SELECTOR, "button.trollface").click()
    time.sleep(1)
    # переключаем на след окно
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    # Пишем ответ в поле
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "button.btn-primary").click()   
finally:
    time.sleep(10)
    browser.quit()
