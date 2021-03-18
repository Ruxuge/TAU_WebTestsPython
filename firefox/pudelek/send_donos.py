import time


def send_correct_text_donos(driver):
    time.sleep(5)
    element = driver.find_element_by_css_selector('.sq0yoh-7')
    element.click()
    time.sleep(10)
    element = driver.find_element_by_css_selector('.sc-2rdf5u-3')
    element.send_keys("Nowy donos testowy")
    element = driver.find_element_by_css_selector('.gmakQZ')
    element.click()
    driver.close()
