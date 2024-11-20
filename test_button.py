from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture()
def browser():
    options = Options()
    # options.headless = True
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    # поиск нужного вебдрайвера и дружба вебдрайвера и текущей версии браузера
    # driver = webdriver.Chrome(
    #     service=ChromeService(ChromeDriverManager().install()),
    #     options=options
    # )
    service = ChromeService(
        executable_path=
        r'C:\Users\serge\.wdm\drivers\chromedriver\win64\131.0.6778.85\chromedriver-win32\chromedriver.exe'
    )
    driver = webdriver.Chrome(
        service=service,
        options=options
    )
    # driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_button_exist(browser):
    browser.get('https://www.qa-practice.com/elements/button/simple')
    assert browser.find_element(By.ID, 'submit-id-submit').is_displayed()
