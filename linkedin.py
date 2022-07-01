from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

MY_USER = "***"
MY_PASS = "***"

URL = "https://www.linkedin.com/jobs/search/?distance=25.0&f_AL=true&" \
      "f_WT=2&geoId=105769538&keywords=python%20developer&sortBy=R"
URL2 = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=marketing%20intern&" \
       "location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"


chrome = "chromedriver_win32/chromedriver.exe"
browser = webdriver.Chrome(executable_path=chrome)
browser.get(URL)
browser.maximize_window()

time.sleep(2)
sign_in = browser.find_element_by_xpath("/html/body/div[1]/header/nav/div/a[2]")
sign_in.click()

time.sleep(2)
username = browser.find_element_by_id("username")
username.send_keys(MY_USER)
password = browser.find_element_by_id("password")
password.send_keys(MY_PASS)
button = browser.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
button.click()

time.sleep(2)
# jobs = browser.find_elements(value=".job-card-container--clickable", by=By.CSS_SELECTOR)
jobs = browser.find_elements(value=".jobs-search-results__list .job-card-list__title",
                             by=By.CSS_SELECTOR)

jobs = [item for item in jobs if len(item.text) > 0]
jobs_text = [item.text for item in jobs if len(item.text) > 0]
print(jobs_text)

for item in jobs:
    item.click()

    time.sleep(2)
    save_btn = browser.find_element(value=".jobs-save-button", by=By.CSS_SELECTOR)

    try:
        save_btn.click()
        time.sleep(2)

    except NoSuchElementException:
        print(f"{item.text} has been skipped due to NoSuchElementException")
    else:
        print(f"{item.text} saved ")
