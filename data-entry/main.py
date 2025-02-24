from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

load_dotenv()
sleeping_time = 0.5

def sleep():
    time.sleep(sleeping_time)

# global variables
link = os.getenv("form_url")

def clean_the_val(string):
    if "/" in string:
        string = string.split("/")[0].replace(",", "")
    if "+" in string:
        string = string.split("+")[0].replace(",", "")
    return string

# Request
response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
data = response.text

# Making soup
soup = BeautifulSoup(data, "html.parser")
containers = soup.find_all("li",class_="ListItem-c11n-8-84-3-StyledListCardWrapper")
address_list = [container.address.text.strip().replace("|", "") for container in containers]
price_list = [clean_the_val(container.find("span", class_="PropertyCardWrapper__StyledPriceLine").get_text()) for container in containers]
link_list = [container.find("a", class_="StyledPropertyCardDataArea-anchor").get("href") for container in containers]

print(len(address_list), end='')
print(len(price_list), end='')
print(len(link_list), end='')

# Keeping the window open / setting up selenium
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("window-size=1200x1000")
driver = webdriver.Chrome(options=chrome_options)
driver.get(link)

for i in range(len(address_list)):
    address = WebDriverWait(driver, timeout=60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    address.click()
    sleep()
    address.send_keys(address_list[i])
    sleep()
    price = WebDriverWait(driver, timeout=60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    price.click()
    sleep()
    price.send_keys(price_list[i])
    sleep()
    home_link = WebDriverWait(driver, timeout=60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    home_link.click()
    sleep()
    home_link.send_keys(link_list[i], Keys.TAB, Keys.ENTER)
    sleep()
    driver.refresh()

# Selenium quit
driver.quit()

