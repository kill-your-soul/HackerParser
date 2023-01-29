import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from typing import List
from pathlib import Path


class XakerParser:
    def __init__(self, login: str, password: str, download_dir: Path) -> None:
        self.login = login
        self.password = password
        self.download_dir = download_dir
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_experimental_option('prefs', {'download.default_directory': str(download_dir)})
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def __downloads_pdfs(self, links: List[WebElement]) -> None:
        for link in links:
            link.click()
            sleep(1)

    def __login_to_site(self) -> None:
        self.driver.get('https://xaker.ru/issues/')
        self.driver.find_element(by=By.CLASS_NAME, value='login-link').click()
        sleep(1)
        self.driver.find_element(by=By.CLASS_NAME, value='input').send_keys(self.login)
        sleep(1)
        self.driver.find_element(by=By.CLASS_NAME, value='user_pass').send_keys(self.password)
        sleep(1)
        self.driver.find_element(by=By.ID, value='wp-submit').click()
        sleep(1)
        
    def parse_site(self) -> None:
        self.__login_to_site()
        all_pages = int(self.driver.find_element(by=By.CLASS_NAME, value="pages").text[-2::])
        for i in range(1, all_pages):
            pdfs = self.driver.find_elements(by=By.CLASS_NAME, value='download-button')
            self.__downloads_pdfs(pdfs)
            self.driver.refresh()
            self.driver.find_element(by=By.ID, value='bdaia-next-page').click()
