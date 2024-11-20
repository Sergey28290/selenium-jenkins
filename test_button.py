from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')
    service = Service(ChromeDriverManager(driver_version="114.0.5735.90").install())
    # driver = webdriver.Chrome(executable_path=ChromeDriverManager(driver_version="114.0.5735.90").install(), options= options)
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_button_exist(browser):
    browser.get('https://www.qa-practice.com/elements/button/simple')
    assert browser.find_element(By.ID, 'submit-id-submit').is_displayed()
