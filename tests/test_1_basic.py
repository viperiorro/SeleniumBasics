import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_example(driver):
    # Navigate to the Google home page
    driver.get("https://www.google.com/")

    # Write "Hillel" in search field and press Enter
    search_field = driver.find_element(By.NAME, "q")
    search_field.send_keys("Hillel")
    search_field.send_keys(Keys.ENTER)
    # Click on the first link
    driver.find_element(By.CSS_SELECTOR, "[href='https://ithillel.ua/']").click()

    # Verify the page title
    assert "Hillel Online" in driver.title

    # Open the Courses menu
    driver.find_element(By.CSS_SELECTOR, "[data-dropdown-trigger='coursesMenu']").click()
    # Click on Testing category
    driver.find_element(By.CSS_SELECTOR, "[data-category='testing']").click()
    # Click on QA Automation - Python course
    driver.find_element(By.CSS_SELECTOR, "[href='https://ithillel.ua/courses/qa-automation-python']").click()

    # Verify the page title after navigation
    assert "QA Automation" in driver.title