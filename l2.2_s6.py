from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try: 
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    browser.execute_script("window.scrollBy(0, 100);") #Скроллим на 100 пикселей
    # Пишем ответ в поле
    browser.find_element(By.ID, "answer").send_keys(y)
    # Ставим метки
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click() 
    browser.find_element(By.CSS_SELECTOR, "button.btn-primary").click() #давим кнопу
finally:
    time.sleep(10)
    browser.quit()
