import os
from pathlib import Path
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from typing import List
from colorama import Fore


def download_pdfs(pdfs: List[WebElement]) -> None:
    for pdf in pdfs:
        pdf.click() # click download button to download pdf
        sleep(1)


def parse(driver: webdriver.Chrome, _login: str, _password: str) -> None:
    driver.get("https://xakep.ru/issues") # get page
    elem = driver.find_element(by=By.CLASS_NAME, value="login-link") # find login button
    elem.click() # go to login page
    login = driver.find_element(by=By.CLASS_NAME, value="input") # find login input
    login.send_keys(_login) # input login 
    sleep(random.randint(1, 3))
    password = driver.find_element(by=By.ID, value="user_pass") # find password input
    password.send_keys(_password) # input password
    sleep(random.randint(1, 3))
    login_button = driver.find_element(by=By.ID, value="wp-submit") #find login button
    login_button.click() # login to  site
    all_pages = driver.find_element(by=By.CLASS_NAME, value="pages") # find amount of pages
    all_pages = int(all_pages.text[-2::]) # get amount of pages 
    for i in range(1, all_pages):
        pdfs = driver.find_elements(by=By.CLASS_NAME, value="download-button") # find downloads buttonn
        download_pdfs(pdfs=pdfs) # evalute download pdfs
        driver.refresh() # refresh page to avoid some errors
        next_page = driver.find_element(by=By.ID, value="bdaia-next-page") # find next page button
        next_page.click() # go to next page


if __name__ == "__main__":
    try:
        login = os.environ["login"] # try to get login from environment variables
        password = os.environ["password"] # try to get password from environment variables
    except KeyError:
        print(
            Fore.RED
            + "password or login not found in environment variables"
            + Fore.RESET
        )
        login = str(input("Input login for xakep.ru: "))
        password = str(input("Input password for xakep.ru: "))
    chromeOptions = webdriver.ChromeOptions() # create chromeOptions
    chromeOptions.add_experimental_option(
        "prefs", {"download.default_directory": str(Path(__file__).parent / "pdfs")} # set preferences to default download directory
    )
    chromeOptions.add_argument("--headless") # set preferences to hide browser
    driver = webdriver.Chrome(chrome_options=chromeOptions) # create webdriver
    parse(driver=driver, _login=login, _password=password) # parse site

