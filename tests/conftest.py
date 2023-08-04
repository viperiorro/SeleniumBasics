# Fixture for creating a Chrome browser instance
import time

import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def driver():
    chrome_driver = webdriver.Chrome()  # Open Chrome window
    chrome_driver.maximize_window()  # full screen
    yield chrome_driver
    time.sleep(2)  # Wait for 2 seconds
    chrome_driver.quit()  # Close Chrome window


@pytest.fixture
def python_org(driver):
    # Navigate to the Python home page
    driver.get("https://www.python.org/")
    yield driver