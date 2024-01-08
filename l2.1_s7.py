from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try: 
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    # Пишем ответ в поле
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
    # Ставим метки
    browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
    browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()
    # Давим кнопу
    browser.find_element(By.CSS_SELECTOR, "button.btn-default").click()
finally:
    time.sleep(10)
    browser.quit()
    
