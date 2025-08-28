from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com")
time.sleep(3)
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH, "//*[@id='header_container']//select").click()
time.sleep(3)
dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
dropdown.select_by_visible_text("Price (high to low)")
time.sleep(3)
driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-fleece-jacket']").click()
time.sleep(3)
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
time.sleep(3)

driver.close()

