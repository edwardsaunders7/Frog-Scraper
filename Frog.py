import os, random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chromeOptions = Options()
chromeOptions.headless = True #set headless so page does not pop up and disturb user

count = int(input("How many frog pictures would you like? ")); #Ask the user how many pictures they want
count2 = count #set this only for last line

while count > 0: #set up the while loop to count down from user's request
    PATH = "driver/chromedriver" # location of the chrome driver
    driver = webdriver.Chrome(PATH, options = chromeOptions) #applying headless setting above
    driver.get("http://allaboutfrogs.org/funstuff/randomfrog.html") #access the random frog generating page
    search = driver.find_element_by_css_selector('body > font > table > tbody > tr > td > img') #ind the image by css selector
    search.screenshot(f"Pics/Frog{count}.png") #save the image with appropiate filename
    count = count - 1 #count down by one to iterate to next picture

driver.quit() #close the chrome driver
print(f"Done! Collected {count2} frog pics!") #Print that all frogs have been collected
