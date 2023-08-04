from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.steps import start_timer, verify_start_btn_disabled


def test_wait_timer_fail(driver):
    start_timer(driver)  # Start the timer
    verify_start_btn_disabled(driver)  # Verify that start button is disabled


def test_wait_timer_implicit(driver):
    driver.implicitly_wait(10)  # Set implicit wait to 10 seconds

    start_timer(driver)
    verify_start_btn_disabled(driver)


def test_wait_timer_explicit(driver):
    wait = WebDriverWait(driver, 10)  # Set explicit wait to 10 seconds

    start_timer(driver)

    # Wait until the start button exists
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".toolbox--manual button.c-timer__btn--start")))

    # Verify that start button is disabled
    verify_start_btn_disabled(driver)
