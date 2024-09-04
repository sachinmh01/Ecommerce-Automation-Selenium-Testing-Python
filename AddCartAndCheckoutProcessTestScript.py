from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# Setup
driver = webdriver.Firefox(executable_path='C:\\Users\\helan\\Desktop\\python_selenium\\driver\\geckodriver.exe')
driver.get("https://www.flipkart.com/")
driver.maximize_window()
time.sleep(1)

# Search for a product
search_box = driver.find_element(By.CLASS_NAME, "Pke_EE")
search_box.click()
time.sleep(1)
search_box.send_keys("T-shirt")
search_box.send_keys(Keys.ENTER)

time.sleep(2)
# Validate product search results
driver.get('https://www.flipkart.com/dyrectdeals-colorblock-men-polo-neck-green-t-shirt/p/itm4cd804c879d03?pid=TSHGMG9ZQFASKXUF&lid=LSTTSHGMG9ZQFASKXUFQLLDWI&marketplace=FLIPKART&q=T-shirt&store=clo%2Fash%2Fank&spotlightTagId=BestsellerId_clo%2Fash%2Fank&srno=s_1_4&otracker=search&otracker1=search&fm=Search&iid=e4e12a5d-6e92-46a7-9c04-34b9b64ab43b.TSHGMG9ZQFASKXUF.SEARCH&ppt=sp&ppn=sp&ssid=1z8v6me1bffayakg1725431522072&qH=a19377ffbff77ed1')
driver.execute_script("window.scrollBy(0,200)")
time.sleep(2)

# Validate that the product is correctly added to the cart.
click_add = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[1]/button')
click_add.click()
time.sleep(2)

# Validate that the checkout process works as expected
place_order = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/form/button')
place_order.click()

time.sleep(2)
driver.close()