#//////////////////////// PACKAGES /////////////////////////////

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

#/////////////////// INFO & DEPENDENCIES //////////////////////

ser = Service('/Users/kautsaraqsa/netflix-automation/chromedriver')
op = webdriver.ChromeOptions()
chromedriverpath = '/Users/kautsaraqsa/netflix-automation/chromedriver'
driver = webdriver.Chrome(service = ser, options = op)
url_rp = 'https://www.netflix.com/settings/migration'

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

def ScrollDown(value = 1) :
    page = driver.find_element(by = 'tag name', value = 'html')  
    for i in range(value):  
        page.send_keys(Keys.ARROW_DOWN) 

#///////////////////////// JOBS //////////////////////////////

#----------------------- Open URL ---------------------------

driver.get(url_rp)
time.sleep(2)

#----------------------- Sign In ----------------------------

Filling(element = '/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[1]/div[1]/div/label/input', fill = email_id) #filling email

Filling(element = '/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[2]/div/div/label/input', fill = password) #filling password

time.sleep(1)

Click(element= '/html/body/div[1]/div/div[3]/div/div/div[1]/form/button') #click 'sign in'

time.sleep(3)

#------------------- Parental Password ----------------------

Filling(element = '//*[@id="input-account-content-restrictions"]', fill = password) #fill password in parental page

time.sleep(1)

Click(element = '//*[@id="appMountPoint"]/div/div/div[2]/div/div/div[2]/div[2]/button[1]') #click on 'continue'

time.sleep(2)

#-------------------- Unlock Profile ------------------------

#try to find hidden element, then click
try:
    driver.find_element(by = 'xpath', value = '//*[@id="appMountPoint"]/div/div/div[2]/div/div/div/div[1]/ul/li/div[2]/div[3]/div[2]')
    Click(element = '//*[@id="appMountPoint"]/div/div/div[2]/div/div/div/div[1]/ul/li/div[2]/div[3]/div[1]') 
except:
    print('Profile already has no PIN !')    

ScrollDown(5)

time.sleep(1)

Click(element = '//*[@id="appMountPoint"]/div/div/div[2]/div/div/div/div[1]/div[2]/button[1]')  #click on 'yes'






