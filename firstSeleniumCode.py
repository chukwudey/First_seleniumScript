import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the Chrome WebDriver using WebDriver manager
driver = webdriver.Chrome()


# Open a website
driver.maximize_window()
driver.get("https://www.bet9ja.com")
driver.get("https://www.get440.com")
driver.get("https://www.Facebook.com")
driver.get("https://www.instagram.com")
driver.get("https://www.jumia.com")
driver.get("https://www.clan.ng")


time.sleep(10)

# Close the browser
driver.quit()
