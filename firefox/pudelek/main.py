import threading
import time

from selenium import webdriver
import logging
import search_check as sc
import login as l
import send_donos as sd

logger = logging.getLogger('simple_example')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


def pop_up(driver):
    pop = 0
    while pop == 0:
        try:
            pop_button = driver.find_element_by_css_selector('.m0zy07y')
            pop = 1
        except:
            time.sleep(10)
            print("no element")
            pop = 0
            pop_button.click()

    print('pop are denide')


if __name__ == "__main__":
    url = 'https://www.pudelek.pl'
    driver = webdriver.Firefox(executable_path='/home/ruxuge/Dokumenty/geckodriver')
    driver.get(url)
    driver.maximize_window()
    element = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[3]/div/button[2]')
    element.click()
    #y = threading.Thread(target=pop_up(driver))
    #y.start()
    # x = threading.Thread(target=sc.search_covid(driver))
    # x = threading.Thread(target=l.bad_login(driver))
    # x = threading.Thread(target=l.bad_password(driver))
    x = threading.Thread(target=sd.send_correct_text_donos(driver))
    x.start()
