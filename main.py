import os
from pathlib import Path
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By



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
login.send_keys(os.environ["login"])
sleep(random.randint(1, 3))
password = driver.find_element(by=By.ID, value="user_pass")
password.send_keys(os.environ["password"])
sleep(random.randint(1, 3))
login_button = driver.find_element(by=By.ID, value="wp-submit")
login_button.click()
last_issue = driver.find_element(by=By.CLASS_NAME, value="entry-title")
last_issue = int(
    last_issue.find_element(by=By.TAG_NAME, value="a")
    .get_attribute("href")
    .split("/")[-1]
)
for i in range(1, last_issue):
    driver.get(f"https://xakep.ru/pdf/xa/{i:03}")
    sleep(1)
