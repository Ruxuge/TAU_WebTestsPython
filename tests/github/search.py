from selenium.webdriver.common.keys import Keys


def find_repository(driver):
    element = driver.find_element_by_xpath('/html/body/div[1]/header/div[3]/div/div/form/label/input[1]')
    element.send_keys("Ruxuge/TAU")
    element.send_keys(Keys.ENTER)


def find_user(driver):
    element = driver.find_element_by_xpath('/html/body/div[1]/header/div[3]/div/div/form/label/input[1]')
    element.send_keys("Ruxuge")
    element.send_keys(Keys.ENTER)
