from selenium import webdriver

url = 'https://www.zalando.'


def chrome_bad_login():
    driver = webdriver.Chrome(executable_path='/home/ruxuge/Dokumenty/chromedriver')

    driver.maximize_window()
    driver.get(url)


def chrome_add_to_cart():
    driver = webdriver.Chrome(executable_path='/home/ruxuge/Dokumenty/chromedriver')

    driver.maximize_window()
    driver.get(url)
