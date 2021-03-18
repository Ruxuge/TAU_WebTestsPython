import time

def bad_login(driver):
    element = driver.find_element_by_id('ol-widget-login-button')
    time.sleep(10)
    element.click()
    time.sleep(5)
    element = driver.find_element_by_id('login')
    element.send_keys("login")
    element = driver.find_element_by_id('password')
    element.send_keys("password")
    element = driver.find_element_by_xpath('/html/body/div[3]/div[1]/main/div/div/div/div[1]/form/button')
    element.click()
    driver.close()


def bad_password(driver):
    element = driver.find_element_by_id('ol-widget-login-button')
    time.sleep(10)
    element.click()
    time.sleep(5)
    element = driver.find_element_by_id('login')
    element.send_keys("login@login.login")
    element = driver.find_element_by_id('password')
    element.send_keys("password")
    element = driver.find_element_by_xpath('/html/body/div[3]/div[1]/main/div/div/div/div[1]/form/button')
    element.click()
    driver.close()

