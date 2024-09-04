from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

# Setup
driver = webdriver.Firefox(executable_path='driver/geckodriver.exe')
driver.get("https://www.nopcommerce.com/en/contact-us")
driver.maximize_window()
time.sleep(1)

select_selenium_obj = driver.find_element_by_tag_name('select')
select_option = Select(select_selenium_obj)

select_option.select_by_visible_text('General questions')
time.sleep(2)
driver.execute_script("window.scrollBy(0,300)")

# Click on 'Contact us ' without entering (as an example of required field)
without_submit = driver.find_element_by_xpath(
    '/html/body/div[7]/section/div/div/div/div/div/div[2]/form/div/div[2]/div[7]/div/input')
without_submit.click()
time.sleep(2)

error_print = driver.find_element_by_xpath('//*[@id="FullName-error"]' )
print(error_print.text)
time.sleep(3)


# It checks for input constraints by entering an invalid email format and validating if the error message appears.
enter_name = driver.find_element_by_id('FullName').send_keys('test')
time.sleep(0.5)
enter_mail = driver.find_element_by_id('Email').send_keys('xyz')
time.sleep(0.5)
enter_enquiry = driver.find_element_by_id('Enquiry').send_keys('I want to you help me')
time.sleep(0.5)
without_submit = driver.find_element_by_xpath(
    '/html/body/div[7]/section/div/div/div/div/div/div[2]/form/div/div[2]/div[7]/div/input')
without_submit.click()

email_error = driver.find_element_by_id('Email-error')
print(email_error.text)

time.sleep(3)

# Enter valid details

name = driver.find_element_by_id('FullName').send_keys('test')
time.sleep(0.5)
valid_enter_mail = driver.find_element_by_id('Email').send_keys('sachintest@gmail.com')
time.sleep(0.5)
valid_enter_enquiry = driver.find_element_by_id('Enquiry').send_keys('I want to you help me')
time.sleep(0.5)
without_submit = driver.find_element_by_xpath(
    '/html/body/div[7]/section/div/div/div/div/div/div[2]/form/div/div[2]/div[7]/div/input')
without_submit.click()

time.sleep(3)
driver.close()