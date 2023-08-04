from selenium.webdriver.common.by import By


def test_basic_css_selector(driver):
    driver.get("https://www.python.org/")
    # Tag name
    elem = driver.find_element(By.CSS_SELECTOR, "input")  # input is a tag name
    print(f"Found {elem.tag_name} by CSS selector using tag name")

    # ID (#)
    elem = driver.find_element(By.CSS_SELECTOR, "#id-search-field")  # id-search-field is an ID
    print(f"Found {elem.tag_name} by CSS selector using ID")

    # Class name (.)
    elem = driver.find_element(By.CSS_SELECTOR, ".search-field")  # search-field is a class name
    print(f"Found {elem.tag_name} by CSS selector using class name")

    # Attribute ([attribute='value'])
    elem = driver.find_element(By.CSS_SELECTOR, "[placeholder='Search']")  # name is an attribute name and q is an attribute value
    print(f"Found {elem.tag_name} by CSS selector using attribute name")

    # Descendant combinator ( )
    elem = driver.find_element(By.CSS_SELECTOR, "form input")  # input is a descendant of form
    print(f"Found {elem.tag_name} by CSS selector using descendant combinator")

    # Child combinator (>)
    elem = driver.find_element(By.CSS_SELECTOR, "fieldset > input")  # input is a child of form
    print(f"Found {elem.tag_name} by CSS selector using child combinator")

    # Adjacent sibling combinator (+)
    elem = driver.find_element(By.CSS_SELECTOR, "label + input")  # input is an adjacent sibling of label
    print(f"Found {elem.tag_name} by CSS selector using adjacent sibling combinator")

    # General sibling combinator (~)
    elem = driver.find_element(By.CSS_SELECTOR, "span ~ input")  # input is a sibling of span
    print(f"Found {elem.tag_name} by CSS selector using general sibling combinator")


def test_css_selector_combination(driver):
    driver.get("https://www.python.org/")

    # Tag name and ID
    elem = driver.find_element(By.CSS_SELECTOR, "input#id-search-field")  # input is a tag name and id-search-field is an ID
    print(f"Found {elem.tag_name} by CSS selector using tag name and ID")

    # Tag name and class name
    elem = driver.find_element(By.CSS_SELECTOR, "input.search-field")  # input is a tag name and search-field is a class name
    print(f"Found {elem.tag_name} by CSS selector using tag name and class name")

    # Tag name, id, and class name
    elem = driver.find_element(By.CSS_SELECTOR, "input#id-search-field.search-field")  # input is a tag name, id-search-field is an ID, and search-field is a class name
    print(f"Found {elem.tag_name} by CSS selector using tag name, ID, and class name")


def test_pseudo_class_search_field(driver):
    # selector:pseudo-class
    driver.get("https://www.python.org/")

    # input is a tag name,
    # :placeholder-shown is a pseudo class that selects elements that have a placeholder attribute with a non-empty value
    elem = driver.find_element(By.CSS_SELECTOR, "input:placeholder-shown")
    print(f"Found {elem.tag_name} by CSS selector using pseudo class")


def test_pseudo_class_3rd_elem_in_control_panel(driver):
    # selector:pseudo-class
    driver.get("https://www.python.org/")

    # ol.flex-control-nav li:nth-child(3) is a CSS selector that selects the third element in the list
    elem = driver.find_element(By.CSS_SELECTOR, "ol.flex-control-nav li:nth-child(3)")
    print(f"Found {elem.tag_name} by CSS selector using pseudo class")
