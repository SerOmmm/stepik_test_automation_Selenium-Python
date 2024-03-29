from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.ID, "num1").text
    y = browser.find_element(By.ID, "num2").text
    # Выбираем ответ в поле
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(int(x) + int(y))) # ищем элемент в списке
     # Давим кнопу
    browser.find_element(By.CSS_SELECTOR, "button.btn-default").click() 
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
