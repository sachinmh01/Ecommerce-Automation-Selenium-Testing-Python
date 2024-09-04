from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup
driver = webdriver.Firefox(executable_path='driver/geckodriver.exe')
driver.get("https://www.amazon.in/")
driver.maximize_window()
time.sleep(1)


# Search for a product
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.click()
time.sleep(2)
search_box.send_keys("T-shirt")
click_on = driver.find_element_by_xpath('//*[@id="nav-search-submit-button"]')
click_on.click()
time.sleep(2)
page_title = driver.title
assert page_title == 'Amazon.in : T-shirt'
driver.back()
time.sleep(2)

# Check navigation menu
nav_menu = driver.find_element(By.LINK_TEXT, "Mobiles")
time.sleep(2)
nav_menu.click()
time.sleep(2)
page_title = driver.title
assert page_title == 'Mobile Phones: Buy New Mobiles Online at Best Prices in India | Buy Cell Phones Online - Amazon.in'
driver.back()

time.sleep(2)
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
time.sleep(2)

# Check footer
footer = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div/div[1]/ul/li[1]/a")
time.sleep(2)
footer.click()
time.sleep(2)
page_title = driver.title
assert page_title == 'About Amazon India - About Amazon India'
driver.back()

time.sleep(1)
driver.close()