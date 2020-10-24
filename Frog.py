import os, random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chromeOptions = Options()
chromeOptions.headless = True

count = int(input("How many frog pictures would you like? "));
count2 = count

while count > 0:
    PATH = "driver/chromedriver"
    driver = webdriver.Chrome(PATH, options = chromeOptions)
    driver.get("http://allaboutfrogs.org/funstuff/randomfrog.html")
    search = driver.find_element_by_css_selector('body > font > table > tbody > tr > td > img')
    search.screenshot(f"Pics/Frog{count}.png")
    count = count - 1

print(f"Done! Collected {count2} frog pics!")
driver.quit()
