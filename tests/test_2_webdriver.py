from selenium import webdriver


def test_drivers():
    driver = webdriver.Chrome()
    driver.quit()

    driver = webdriver.Firefox()
    driver.quit()

    driver = webdriver.Edge()
    driver.quit()
