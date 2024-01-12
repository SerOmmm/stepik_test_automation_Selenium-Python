import pytest
def test_abs1():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration1.html")
    browser.find_element(By.CSS_SELECTOR, "div.first_block div:nth-of-type(1) input").send_keys("Ivan")
    browser.find_element(By.CSS_SELECTOR, "div.first_block div:nth-of-type(2) input").send_keys("Petrov")
    browser.find_element(By.CSS_SELECTOR, "div.first_block div:nth-of-type(3) input").send_keys("pochta@gmail.com")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)    
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text, "Registration 1 failed."
    browser.quit()
                
    # на этой половине тест валится, так запланировано                
def test_abs2():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration2.html")
    browser.find_element(By.CSS_SELECTOR, "div.first_block div:nth-of-type(1) input").send_keys("Ivan")
    browser.find_element(By.CSS_SELECTOR, "div.first_block div:nth-of-type(2) input").send_keys("Petrov")
    browser.find_element(By.CSS_SELECTOR, "div.first_block div:nth-of-type(3) input").send_keys("pochta@gmail.com")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)    
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text, "Registration 2 failed."
    browser.quit()
        
if __name__ == "__main__":
    pytest.main()