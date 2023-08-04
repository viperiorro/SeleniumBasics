from selenium.webdriver.common.by import By


def test_selecting_nodes(driver):
    driver.get("https://www.python.org/")

    # root element
    elem = driver.find_element(By.XPATH, "/html")
    print(f"Found {elem.tag_name} by XPath")

    # body from html
    elem = driver.find_element(By.XPATH, "/html/body")
    print(f"Found {elem.tag_name} by XPath")

    # body in any place
    elem = driver.find_element(By.XPATH, "//body")
    print(f"Found {elem.tag_name} by XPath")

    # All elements
    elems = driver.find_elements(By.XPATH, "//*")
    print(f"Found {len(elems)} elements")

    # By tag name
    elem = driver.find_element(By.XPATH, "//input")
    print(f"Found {len(elem)} input elements")


def test_predicates(driver):
    driver.get("https://www.python.org/")

    # Find the 3rd element in control navigation menu
    elem =  driver.find_element(By.XPATH, "//ol[@class='flex-control-nav flex-control-paging']/li[3]/a")
    print(f"Found {elem.tag_name} by XPath")

    # Find the last element in control navigation menu
    elem =  driver.find_element(By.XPATH, "//ol[@class='flex-control-nav flex-control-paging']/li[last()]/a")
    print(f"Found {elem.tag_name} by XPath")

    # Find input with name attribute equal to q
    elem = driver.find_element(By.XPATH, "//input[@name='q']")
    print(f"Found {elem.tag_name} by XPath")


def test_selecting_several_path(driver):
    driver.get("https://www.python.org/")

    # Find 1st and last element in control navigation menu
    xpath = "//ol[@class='flex-control-nav flex-control-paging']/li[1]/a | //ol[@class='flex-control-nav flex-control-paging']/li[last()]/a"
    elems = driver.find_elements(By.XPATH, xpath)
    print(f"Found {len(elems)} elements by XPath")


def test_contains(driver):
    driver.get("https://www.python.org/")

    # Find all elements with class attribute containing 'menu'
    elems = driver.find_elements(By.XPATH, "//*[contains(@class, 'menu')]")
    print(f"Found {len(elems)} elements by XPath")


def test_using_or_and(driver):
    driver.get("https://www.python.org/")

    # Find all elements with class attribute containing 'menu' or 'flex'
    elems = driver.find_elements(By.XPATH, "//*[contains(@class, 'menu') or contains(@class, 'flex')]")
    print(f"Found {len(elems)} elements with class attribute containing 'menu' or 'flex'")

    # Find all elements with class attribute containing 'menu' and 'flex'
    elems = driver.find_elements(By.XPATH, "//*[contains(@class, 'menu') and contains(@class, 'flex')]")
    print(f"Found {len(elems)} elements with class attribute containing 'menu' and 'flex'")


def test_starts_with(driver):
    driver.get("https://www.python.org/")

    # Find all elements with class attribute starting with 'menu'
    elems = driver.find_elements(By.XPATH, "//*[starts-with(@class, 'menu')]")
    print(f"Found {len(elems)} elements with class attribute starting with 'menu'")


def test_text(driver):
    driver.get("https://www.python.org/")

    # Find all elements with text 'Python'
    elems = driver.find_elements(By.XPATH, "//*[text()='Python']")
    print(f"Found {len(elems)} elements with text 'Python'")


def test_axes_methods(driver):
    driver.get("https://www.python.org/")

    # Find all child elements of element with id 'top' (direct children only)
    elems = driver.find_elements(By.XPATH, "//*[@id='top']/child::*")
    print(f"Found {len(elems)} child elements of element with id 'top'")

    # Find all descendant elements of element with id 'top' (all children, grandchildren, etc.)
    elems = driver.find_elements(By.XPATH, "//*[@id='top']//descendant::*")
    print(f"Found {len(elems)} descendant elements of element with id 'top'")
