import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    driver=webdriver.Chrome()
    yield driver

def open_url_verify_title(driver):
    driver.get("https://app.vwo.com")
    print(driver.title)
    assert "login-VWO"==driver.title