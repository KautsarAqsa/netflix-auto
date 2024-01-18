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

email_id = 'wisdom@netsneeze.com'
password = 'admin1'

url_tp = 'https://www.netflix.com/DoNotTest'

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

driver.get(url_tp)
time.sleep(2)

#----------------------- Sign In ---------------------------

Filling(element = '/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[1]/div[1]/div/label/input', fill = email_id) #filling email

Filling(element = '/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[2]/div/div/label/input', fill = password) #filling

time.sleep(1)

Click(element= '/html/body/div[1]/div/div[3]/div/div/div[1]/form/button') #click 'sign in'

time.sleep(3)

#----------------------- TP On/Off ---------------------------

try:
    status = GetText(element = '/html/body/div[1]/div/div/div[3]/div/form/fieldset/label')
    if status == 'HIDUP' or status == 'ON':
        Click(element = '//*[@id="appMountPoint"]/div/div/div[3]/div/form/fieldset/label/button')
except:
    status = GetText(element = '/html/body/div[1]/div/div/div[2]/div/form/fieldset/label')
    if status == 'HIDUP' or status == 'ON':
        Click(element = '//*[@id="appMountPoint"]/div/div/div[2]/div/form/fieldset/label/button')

print(status)
time.sleep(1)

Click(element = '//*[@id="appMountPoint"]/div/div/div[2]/div/form/div/button') #click on 'done' button