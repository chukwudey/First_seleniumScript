import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(30)

# Login page....
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("Admin")
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys("admin123")
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
time.sleep(5)

# Admin page....
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a').click()
time.sleep(5)

# PIM page...
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a').click()
time.sleep(5)

# Leave page...
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a').click()
time.sleep(5)

# Time page...
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a').click()
time.sleep(5)

#Recruitment page...
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a').click()
time.sleep(5)

#My info page
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a').click()
time.sleep(5)

#Performance page
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a').click()
time.sleep(5)

#Dashboard page...
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a').click()
time.sleep(5)


# Directory page...
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a').click()
time.sleep(5)
# Maintenance page...
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[10]/a').click()
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/form/div[3]/div/div[2]/input').send_keys("admin123")
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/form/div[4]/button[2]').click()
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a').click()
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div[1]/form/div[1]/div/div/div/div[2]/div/div/input').send_keys("John")
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div[1]/form/div[1]/div/div/div/div[2]/div/div/input').send_keys("joker john selvam")
time.sleep(5)
# Claim page...
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[11]/a').click()
time.sleep(5)
# Buzz page...
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[12]/a').click()


time.sleep(14)


driver.quit()


