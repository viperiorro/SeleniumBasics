from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.steps import open_entry_ad_page, close_ad, restart_ad, \
    verify_modal_displayed


def test_wait_ad_fail(driver):
    open_entry_ad_page(driver)  # Open the "Entry Ad" page
    close_ad(driver)  # Close the ad
    restart_ad(driver)  # Restart the ad
    verify_modal_displayed(driver)  # Verify that the modal is displayed


def test_wait_ad_implicit(driver):
    driver.implicitly_wait(10)  # Set implicit wait to 10 seconds

    open_entry_ad_page(driver)
    close_ad(driver)
    restart_ad(driver)
    verify_modal_displayed(driver)


def test_wait_ad_explicit(driver):
    wait = WebDriverWait(driver, 10)  # Set explicit wait to 10 seconds

    open_entry_ad_page(driver)

    # Wait until the Close button is clickable
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.modal .modal-footer p")))

    close_ad(driver)

    # Wait until the Restart button is clickable
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a#restart-ad")))
    restart_ad(driver)

    # Wait until the modal is displayed
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.modal")))

    verify_modal_displayed(driver)


def test_wait_ad_explicit_with_lambda(driver):
    wait = WebDriverWait(driver, 10)  # Set explicit wait to 10 seconds

    open_entry_ad_page(driver)

    # Wait until the Close button is clickable
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.modal .modal-footer p")))

    close_ad(driver)

    # Wait until the Restart button is clickable
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a#restart-ad")))
    restart_ad(driver)

    # Wait until the modal is displayed
    wait.until(lambda dr: dr.find_element(By.CSS_SELECTOR, "div.modal").is_displayed())

    verify_modal_displayed(driver)


