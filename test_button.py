from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pytest


@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')
    # options.binary_location = "C:/Chrome114/chrome.exe"
    options.binary_location = "C:/Chrome114/UserData/Application/chrome.exe"
    service = Service(ChromeDriverManager(driver_version="114.0.5735.90").install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_button_exist(browser):
    browser.get('https://www.qa-practice.com/elements/button/simple')
    assert browser.find_element(By.ID, 'submit-id-submit').is_displayed()
    # assert 1 == 2
