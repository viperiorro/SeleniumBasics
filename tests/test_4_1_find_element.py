# write a guideline how to find an element on the site.
from selenium.webdriver.common.by import By


def test_find_element(driver):
    driver.get("https://www.python.org/")
    # By ID
    elem = driver.find_element(By.ID, "id-search-field")
    print(f"Found {elem.tag_name} by ID")

    # By name
    elem = driver.find_element(By.NAME, "q")
    print(f"Found {elem.tag_name} by name")

    # By class name
    elem = driver.find_element(By.CLASS_NAME, "search-field")
    print(f"Found {elem.tag_name} by class name")

    # By tag name
    elem = driver.find_element(By.TAG_NAME, "input")
    print(f"Found {elem.tag_name} by tag name")

    # By link text
    elem = driver.find_element(By.LINK_TEXT, "Python")
    print(f"Found {elem.tag_name} by link text")

    # By partial link text
    elem = driver.find_element(By.PARTIAL_LINK_TEXT, "Pyth")
    print(f"Found {elem.tag_name} by partial link text")

    # By CSS selector
    elem = driver.find_element(By.CSS_SELECTOR, "[name='q']")
    print(f"Found {elem.tag_name} by CSS selector")

    # By XPath
    elem = driver.find_element(By.XPATH, "//input[@name='q']")
    print(f"Found {elem.tag_name} by XPath")


def test_find_search_field(driver):
    driver.get("https://www.python.org/")

    # Find search field in different ways
    elem_by_id = driver.find_element(By.ID, "id-search-field")
    elem_by_name = driver.find_element(By.NAME, "q")
    elem_by_class_name = driver.find_element(By.CLASS_NAME, "search-field")
    elem_by_tag_name = driver.find_element(By.TAG_NAME, "input")
    elem_by_css_selector = driver.find_element(By.CSS_SELECTOR, "[name='q']")
    elem_by_xpath = driver.find_element(By.XPATH, "//input[@name='q']")

    # Assert that all found elements are the same element
    assert elem_by_id == elem_by_name == elem_by_class_name == elem_by_tag_name == elem_by_css_selector == elem_by_xpath

