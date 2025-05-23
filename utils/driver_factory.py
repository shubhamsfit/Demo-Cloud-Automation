from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

def create_driver():
    chrome_options = Options()
    # Uncomment below to run headless:
    # chrome_options.add_argument("--headless")

    driver_path = os.getenv("CHROMEDRIVER_PATH", None)
    if driver_path:
        service = Service(driver_path)
    else:
        service = Service()

    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    return driver
