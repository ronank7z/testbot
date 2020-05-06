import os, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By #Element Finder
from selenium.webdriver.common.keys import Keys #Keyboard keys
from selenium.webdriver.support.ui import WebDriverWait #Idle
from selenium.webdriver.support.expected_conditions import presence_of_element_located

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome("env/chromedriver/chromedriver.exe", options=chrome_options)

wait = WebDriverWait(driver, 10)
driver.get("https://www.bareksa.com/id/member/login")
driver.find_element(By.NAME, "email").send_keys(os.environ['bareksa_email'])
driver.find_element(By.NAME, "password").send_keys(os.environ['bareksa_pwd'] + Keys.RETURN)

time.sleep(10)

def get_investment_info():
    total_investasi = driver.find_element_by_class_name("total-value")
    total_keuntungan = driver.find_element_by_class_name("total-profit")
    persentase_keuntungan = driver.find_element_by_css_selector(".data-user__item div p div")
    result = "Total Investasi : Rp. {}\nTotal Keuntungan : Rp. {}\nPersentase Keuntungan : {}".format(total_investasi.text, total_keuntungan.text, persentase_keuntungan.text)
    return result