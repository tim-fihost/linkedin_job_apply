from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
LINK = "https://www.linkedin.com/jobs/search/?currentJobId=3682066626&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom"
GMAIL = ""
PW = "XXXXXXXX"
PHONE = "XXXXXXXX"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)


driver = webdriver.Chrome()
driver.get(LINK)
sing_in = driver.find_element(By.XPATH, value="/html/body/div[1]/header/nav/div/a[2]")
sing_in.click()

user_name = driver.find_element(By.NAME, value='session_key')
user_password = driver.find_element(By.NAME, value='session_password')
sing_in2 = driver.find_element(By.CSS_SELECTOR,value='button ')
user_name.send_keys(GMAIL)
user_password.send_keys(PW)
sing_in2.click()
div_elements = driver.find_element(By.XPATH, value='//*[@id="main"]/div/div[1]/div/ul')
jobs = div_elements.find_elements(By.CSS_SELECTOR, value='a')
i = 0
for job in jobs:
    i += 1
    print(i,job.text)
    print("Clicked Easy_apply confirmed")
    job.click()
    time.sleep(3)
    try:
        # apply button field
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)

        # phone number field
        phone_number = driver.find_element(by=By.CLASS_NAME, value="fb-single-line-text__input")
        if phone_number.text == "":
            phone_number.send_keys(PHONE)

        # Cancel and discard button
        cancel_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        cancel_button.click()

        discard_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")
        discard_button.click()

    except NoSuchElementException:
        print("No Application button available, skipped")
        continue
