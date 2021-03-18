import time


def bad_login(driver):
    element = driver.find_element_by_id('topLoginLink')
    element.click()
    element = driver.find_element_by_id('userEmail')
    element.send_keys("login")
    element = driver.find_element_by_id('userPass')
    element.send_keys("password")
    #element = driver.find_element_by_id('se_userLogin')
    #element.click


def bad_password(driver):
    element = driver.find_element_by_id('topLoginLink')
    element.click()
    element = driver.find_element_by_id('userEmail')
    element.send_keys("login@login.login")
    element = driver.find_element_by_id('userPass')
    element.send_keys("password")
    element = driver.find_element_by_id('se_userLogin')
    element.click
