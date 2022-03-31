from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

product = input("Enter product name:")
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.flipkart.com/")
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()
time.sleep(1)
driver.find_element_by_name("q").send_keys(product)
time.sleep(1)
driver.find_element_by_class_name("L0Z3Pu").submit()
time.sleep(50)
driver.close()
