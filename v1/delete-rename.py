#/////////////////// PACKAGES //////////////////////

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

#/////////////////// INFO & DEPENDENCIES //////////////////////

ser = Service('/Users/kautsaraqsa/netflix-automation/chromedriver')
op = webdriver.ChromeOptions()
chromedriverpath = '/Users/kautsaraqsa/netflix-automation/chromedriver'
driver = webdriver.Chrome(service = ser, options = op)
url_dp = 'https://www.netflix.com/simpleSetup/newprofiles'

email_id = 'wisdom@netsneeze.com'
password = 'admin1'

#/////////////////////// FUNCTION /////////////////////////////

def Click(element):
    driver.find_element(by = 'xpath', value = element).click()

def Filling(element, fill):
    field = driver.find_element(by = 'xpath', value = element)
    field.send_keys(fill)

def GetText(element):
    return driver.find_element(by = 'xpath', value = element).text

def ClearField(element):
    field = driver.find_element(by = 'xpath', value = element)
    field.send_keys(Keys.COMMAND + "a")
    field.send_keys(Keys.DELETE)

def ScrollDown():
    page = driver.find_element(by = 'tag name', value = 'html')    
    page.send_keys(Keys.ARROW_DOWN) 

#///////////////////////// JOBS //////////////////////////////

#----------------------- Open URL ---------------------------

driver.get(url_dp)
time.sleep(2)

#----------------------- Sign In ---------------------------

Click(element = '//*[@id="appMountPoint"]/div/div/div/div/div/div[1]/div/a') #click on 'sign in'

time.sleep(2)

Filling(element = '/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[1]/div[1]/div/label/input', fill = email_id) #filling email

Filling(element = '/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[2]/div/div/label/input', fill = password) #filling

time.sleep(1)

Click(element= '/html/body/div[1]/div/div[3]/div/div/div[1]/form/button') #click 'sign in'

time.sleep(2)

#----------------------- Open Second URL ---------------------------

driver.get(url_dp)
time.sleep(3)

#----------------------- Delete Profile ----------------------------

ClearField(element= '//*[@id="id_ownerName"]') #clear main profile
Filling(element= '//*[@id="id_ownerName"]', fill = '1') #fill main prfolie
ClearField(element= '//*[@id="id_profile1Name"]') #clear profile 1
ClearField(element= '//*[@id="id_profile3Name"]') #clear profile 2
ClearField(element= '//*[@id="id_profile2Name"]') #clear profile 3
ClearField(element= '//*[@id="id_profile4Name"]') #clear profile 4

time.sleep(1)

Click(element= '//*[@id="appMountPoint"]/div/div/div/div[2]/div/div/div[2]/form/button[2]') #click 'next'

time.sleep(2)

#----------------------- Kids Profile ------------------------------
ScrollDown()    #scroll down to generate unseen element
time.sleep(1)
Click(element= '//*[@id="appMountPoint"]/div/div/div/div[2]/div/div/div[2]/form/div[2]/div/button') #click 'next'
time.sleep(2)

#----------------------- Choose Language ---------------------------
ScrollDown()    #scroll down
time.sleep()
Click(element= '//*[@id="appMountPoint"]/div/div/div/div[2]/div/div/div[2]/form/div[2]/div/button') #click 'next'
time.sleep(2)

