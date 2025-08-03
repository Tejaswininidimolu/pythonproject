from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
driver.find_element(By.ID, 'user-name').send_keys('standard_user')
driver.find_element(By.ID, 'password').send_keys('secret_sauce')
driver.find_element(By.XPATH, "//*[@id='login-button']").click()
driver.implicitly_wait(3)

driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']").click()
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
time.sleep(5)
driver.find_element(By.ID, "checkout").click()
driver.find_element(By.ID, "first-name").send_keys("John")
driver.find_element(By.ID, "last-name").send_keys("Mickel")
driver.find_element(By.ID, "postal-code").send_keys('543126')
driver.find_element(By.XPATH, "//*[@id='continue']").click()
driver.find_element(By.ID, "finish").click()
driver.implicitly_wait(5)
driver.find_element(By.ID, 'back-to-products').click()
time.sleep(5)
sort_dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
sort_dropdown.select_by_visible_text("Price (low to high)")
time.sleep(5)

driver.close()