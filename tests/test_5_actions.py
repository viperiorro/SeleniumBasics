import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_navigate_to_url(driver):
    # Navigate to URL
    driver.get("http://www.python.org")

    # Assert that the title is correct
    assert "Python" in driver.title


def test_click(python_org):
    # Click on all items in the list of Dive Into Python elements
    elems = python_org.find_elements(By.CSS_SELECTOR, ".flex-control-nav > li > a")
    for elem in elems:
        elem.click()
        print(f"Clicked on {elem.text}")


def test_type_and_clear(python_org):
    search_field = python_org.find_element(By.NAME, "q")  # find search input
    search_field.send_keys("Java")  # type 'Java'
    search_field.clear()  # clear search input
    search_field.send_keys("Python")  # type 'Python'

    # Click on search button
    python_org.find_element(By.ID, "submit").click()

    # Assert that there are no results
    result = python_org.find_element(By.CSS_SELECTOR, ".list-recent-events > p")
    assert "No results found." in result.text


def test_press_keys(python_org):
    search_field = python_org.find_element(By.NAME, "q")  # find search input
    search_field.send_keys("Python")  # type 'Python'
    search_field.send_keys(Keys.ENTER)  # Press Enter

    # Assert that there are no results
    result = python_org.find_element(By.CSS_SELECTOR, ".list-recent-events > p")
    assert "No results found." in result.text


def test_submit(python_org):
    search_field = python_org.find_element(By.NAME, "q")  # find search input
    search_field.send_keys("Python")  # type 'Python'
    search_field.submit()  # Submit form

    # Assert that there are no results
    result = python_org.find_element(By.CSS_SELECTOR, ".list-recent-events > p")
    assert "No results found." in result.text


def test_select_option_from_dropdown(python_org):
    # Click on Documentation
    python_org.find_element(By.LINK_TEXT, "Documentation").click()
    # Click on Python Docs
    python_org.find_element(By.LINK_TEXT, "Python Docs").click()

    # Change language
    dropdown = python_org.find_element(By.CSS_SELECTOR, ".switchers #language_select")
    select = Select(dropdown)
    select.select_by_value("ko")  # Select Korean
    time.sleep(1)
    header = python_org.find_element(By.CSS_SELECTOR, ".body h1")
    assert "문서" in header.text

    dropdown = python_org.find_element(By.CSS_SELECTOR, ".switchers #language_select")
    select = Select(dropdown)
    select.select_by_index(0)  # Select English
    time.sleep(1)
    header = python_org.find_element(By.CSS_SELECTOR, ".body h1")
    assert "documentation" in header.text

    dropdown = python_org.find_element(By.CSS_SELECTOR, ".switchers #language_select")
    select = Select(dropdown)
    select.select_by_visible_text("Spanish")
    time.sleep(1)
    header = python_org.find_element(By.CSS_SELECTOR, ".body h1")
    assert "documentación" in header.text # Select Spanish


def test_navigate_back_and_forward(python_org):
    # Click on Documentation
    python_org.find_element(By.LINK_TEXT, "Documentation").click()
    # Click on Python Docs
    python_org.find_element(By.LINK_TEXT, "Python Docs").click()

    time.sleep(1)
    python_org.back()  # Click on browser back button

    time.sleep(1)
    python_org.forward()  # Click on browser forward button


def test_switch_to_alert(driver):
    # Navigate to URL
    driver.get("http://the-internet.herokuapp.com/context_menu")

    # Right-click on the box
    box = driver.find_element(By.ID, "hot-spot")
    action = ActionChains(driver)
    action.context_click(box).perform()

    # Switch to alert
    alert = driver.switch_to.alert
    assert "You selected a context menu" in alert.text


def test_switch_to_iframe(driver):
    driver.get("http://the-internet.herokuapp.com/iframe")
    driver.switch_to.frame("mce_0_ifr")
    driver.find_element(By.CSS_SELECTOR, "#tinymce").send_keys("Hello World!")
    driver.switch_to.default_content()
    driver.find_element(By.LINK_TEXT, "Elemental Selenium").click()


def test_remove_popup(driver):
    driver.get("https://the-internet.herokuapp.com/")

    driver.find_element(By.CSS_SELECTOR, "#content li:nth-child(15) a").click()

    time.sleep(3)

    driver.find_element(By.CSS_SELECTOR, ".modal-footer p").click()
    # close = driver.find_element(By.CSS_SELECTOR, ".modal-footer p")
    # driver.execute_script("arguments[0].click();", close)

    time.sleep(1)

    driver.find_element(By.CSS_SELECTOR, "#restart-ad").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "#restart-ad").click()

    time.sleep(1)

    modal = driver.find_element(By.CSS_SELECTOR, "div#modal")
    assert modal.is_displayed()
    assert modal.value_of_css_property("display") == "block"


def test_drug_and_drop(driver):
    driver.get("http://the-internet.herokuapp.com/drag_and_drop")
    time.sleep(1)
    left = driver.find_element(By.CSS_SELECTOR, "#column-a")
    right = driver.find_element(By.CSS_SELECTOR, "#column-b")
    action = ActionChains(driver)
    action.drag_and_drop(left, right)
    action.perform()
    time.sleep(1)
    left = driver.find_element(By.CSS_SELECTOR, "#column-a")
    right = driver.find_element(By.CSS_SELECTOR, "#column-b")
    assert "A" in right.text
    assert "B" in left.text


def test_horizontal_slider(driver):
    driver.get("http://the-internet.herokuapp.com/horizontal_slider")
    time.sleep(1)
    slider = driver.find_element(By.CSS_SELECTOR, ".sliderContainer input")
    action = ActionChains(driver)
    action.drag_and_drop_by_offset(slider, 50, 0).perform()
    time.sleep(1)
    slider.send_keys(Keys.ARROW_LEFT)
    assert "4" in driver.find_element(By.ID, "range").text


def test_hover(driver):
    driver.get("http://the-internet.herokuapp.com/hovers")
    time.sleep(1)
    image = driver.find_element(By.CSS_SELECTOR, ".figure img")
    action = ActionChains(driver)
    action.move_to_element(image).perform()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "View profile").click()
