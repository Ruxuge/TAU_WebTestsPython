from selenium.webdriver.common.keys import Keys


def search_covid(driver):
    element = driver.find_element_by_css_selector('input.mZWCj')
    element.send_keys("covid")
    element.send_keys(Keys.ENTER)
    driver.close()
