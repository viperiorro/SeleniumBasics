import time

from selenium.webdriver.common.by import By


def start_timer(driver):
    driver.get("https://www.timeanddate.com/timer/")  # Open the timer page

    # Click on Accept Cookie button
    time.sleep(1)  # Wait for 1 seconds
    driver.find_element(By.CSS_SELECTOR, "button[mode=primary]").click()

    # Set 5 seconds to the timer
    driver.find_element(By.CSS_SELECTOR, "span.timeLeft").click()  # Click on change time
    driver.find_element(By.CSS_SELECTOR, "#hourInput").clear()  # Clear the hours input
    driver.find_element(By.CSS_SELECTOR, "#minuteInput").clear()  # Clear the minutes input
    secs = driver.find_element(By.CSS_SELECTOR, "#secondInput")
    secs.clear()  # Clear the seconds input
    secs.send_keys("5")  # Set 5 seconds
    driver.find_element(By.CSS_SELECTOR, "div.modal-footer input").click()  # Click on Done button

    # Click on Start button
    driver.find_element(By.CSS_SELECTOR, ".toolbox--manual button.c-timer__btn--start").click()


def verify_start_btn_disabled(driver):
    # Verify that start button is disabled
    start_btn = driver.find_element(By.CSS_SELECTOR, ".toolbox--manual button.c-timer__btn--start")
    assert not start_btn.is_enabled()


def open_entry_ad_page(driver):
    driver.get("https://the-internet.herokuapp.com/")  # Open the-internet page
    driver.find_element(By.LINK_TEXT, "Entry Ad").click()  # Click on the "Entry Ad" link


def close_ad(driver):
    driver.find_element(By.CSS_SELECTOR, "div.modal .modal-footer p").click()  # Click on the close button


def restart_ad(driver):
    driver.find_element(By.CSS_SELECTOR, "a#restart-ad").click()  # Click on the restart button


def verify_modal_displayed(driver):
    modal = driver.find_element(By.CSS_SELECTOR, "div#modal")  # Find the modal
    assert modal.is_displayed()  # Verify that the modal is displayed