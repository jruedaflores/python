from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .mv_conf import CHROME_DRIVER, FIREFOX_DRIVER, OPEN_CHROME_DRIVER
from .common import URL_SING_IN, URL_YOUTUBE

import time


def get_driver_chrome():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized");
    options.add_argument("--mute-audio")
    options.add_argument("--incognito")
    return webdriver.Chrome(chrome_options=options, executable_path=CHROME_DRIVER)


def get_driver_firefox():
    profile = webdriver.FirefoxProfile()
    profile.set_preference("media.volume_scale", "0.0")

    options = webdriver.FirefoxOptions()
    options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    options.add_argument("-private")
    # options.add_argument("--headless")
    return webdriver.Firefox(firefox_profile=profile, firefox_options=options, executable_path=FIREFOX_DRIVER)


def get_driver():
    if OPEN_CHROME_DRIVER:
        return get_driver_chrome()
    else:
        return get_driver_firefox()


def connect(driver, with_sing_in=False, url_base=URL_YOUTUBE, user_name=False, user_password=False):
    if with_sing_in and user_name and user_password:
        driver.get(URL_SING_IN)
        sign_in(driver, user_name, user_password)
        if url_base != URL_YOUTUBE:
            driver.get(url_base)
    else:
        driver.get(url_base)


def sign_in(driver, user_name, user_password):
    # Usuario
    driver.find_element_by_name("identifier").send_keys(user_name)
    driver.find_element_by_xpath("//*[@id='identifierNext']/div/button").click()
    # driver.find_element_by_id("identifierNext").click()
    time.sleep(5)

    # Password
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
    driver.find_element_by_name("password").send_keys(user_password)
    driver.find_element_by_xpath("//*[@id='passwordNext']/div/button").click()
    time.sleep(5)
