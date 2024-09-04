from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup
driver = webdriver.Firefox(executable_path='driver/geckodriver.exe')
driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26useRedirectOnSuccess%3D1%26signIn%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
driver.maximize_window()
time.sleep(2)

# Enter invalid credentials
driver.find_element(By.NAME, "email").send_keys("xyndcod")
time.sleep(1)
driver.find_element_by_class_name('a-button-input').click()

# Envalid error message
error = driver.find_element_by_xpath('//*[@id="auth-email-invalid-claim-alert"]')
print(error.text)
time.sleep(2)
driver.refresh()
time.sleep(2)

# Enter valid credentials
driver.find_element(By.NAME, "email").send_keys("helange2020@gmail.com")
time.sleep(2)
driver.find_element_by_class_name('a-button-input').click()

driver.find_element(By.NAME, "password").send_keys("Sachin@123")
driver.find_element(By.CLASS_NAME, "a-button-input").click()

# Validate login success
page_title = driver.title
assert page_title == 'Your Amazon.in'


# Cleanup
time.sleep(2)
driver.quit()
