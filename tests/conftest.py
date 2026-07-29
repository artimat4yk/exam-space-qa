import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

@pytest.fixture(scope="function")
def driver():
    # Путь к geckodriver.exe
    gecko_driver_path = "drivers/geckodriver.exe"
    service = Service(gecko_driver_path)

    options = webdriver.FirefoxOptions()
    # запускать без гуя:
    # options.add_argument("--headless")

    driver = webdriver.Firefox(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
