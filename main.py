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
        pdf.click()
        sleep(1)


try:
    login = os.environ['login']
    password = os.environ['password']
except KeyError:
    print(Fore.RED + 'password or login not found in environment variables' + Fore.RESET)
    login = str(input('Input login for xakep.ru: '))
    password = str(input('Input password for xakep.ru: '))



chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option(
    "prefs", {"download.default_directory": str(Path(__file__).parent / "pdfs")}
)
chromeOptions.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chromeOptions)


driver.get("https://xakep.ru/issues")
elem = driver.find_element(by=By.CLASS_NAME, value="login-link")
elem.click()
login = driver.find_element(by=By.CLASS_NAME, value="input")
login.send_keys(login)
sleep(random.randint(1, 3))
password = driver.find_element(by=By.ID, value="user_pass")
password.send_keys(password)
sleep(random.randint(1, 3))
login_button = driver.find_element(by=By.ID, value="wp-submit")
login_button.click()
all_pages = driver.find_element(by=By.CLASS_NAME, value="pages")
all_pages = int(all_pages.text[-2::])
for i in range(1, all_pages):
    pdfs = driver.find_elements(by=By.CLASS_NAME, value="download-button")
    download_pdfs(pdfs=pdfs)
    driver.refresh()
    next_page = driver.find_element(by=By.ID, value="bdaia-next-page")
    next_page.click()
