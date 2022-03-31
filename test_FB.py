import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


@pytest.fixture
def setup():
    global username, password, driver
    username = input("Enter username")
    password = input("Enter password")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    print("Test case started")
    driver.maximize_window()
    yield
    time.sleep(5)
    driver.close()


def test_searchProducts(setup):
    driver.get("https://www.facebook.com/")
    time.sleep(1)
    driver.find_element_by_name("email").send_keys(username)
    driver.find_element_by_name("pass").send_keys(password)
    time.sleep(1)
    driver.find_element_by_name("login").click()