import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com")
driver.implicitly_wait(30)


# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
time.sleep(2)
driver.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(2)
driver.find_element(By.ID,"login-button").click()
time.sleep(2)

#Add to cart
driver.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-fleece-jacket"]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-backpack"]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-onesie"]').click()
time.sleep(2)

#Cart
driver.find_element(By.XPATH,'//*[@id="shopping_cart_container"]/a').click()
time.sleep(2)

#Checkout button
driver.find_element(By.ID,"checkout").click()
time.sleep(2)

#checkout information
driver.find_element(By.ID, "first-name").send_keys("Ope")
time.sleep(2)
driver.find_element(By.ID, "last-name").send_keys("Odogwu")
time.sleep(2)
driver.find_element(By.ID, "postal-code").send_keys("110011")
time.sleep(2)
driver.find_element(By.ID,"continue").click()
time.sleep(2)

#checkout review
driver.find_element(By.ID,"finish").click()
time.sleep(2)

#Back Home
driver.find_element(By.ID,"back-to-products").click()
time.sleep(5)

driver.quit()