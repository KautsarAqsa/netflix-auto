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
url_ya = 'https://www.netflix.com/YourAccount'
url_cc = 'https://www.netflix.com/clearcookies'

email_id = 'zokoid@netsneeze.com'
password = 'sneeze1'

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

driver.get(url_ya)
time.sleep(2)

#----------------------- Sign In ----------------------------

Filling(element = '/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[1]/div[1]/div/label/input', fill = email_id) #filling email

Filling(element = '/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[2]/div/div/label/input', fill = password) #filling password

time.sleep(1)

Click(element= '/html/body/div[1]/div/div[3]/div/div/div[1]/form/button') #click 'sign in'

time.sleep(3)

#---------------------- 

text = GetText(element = '//*[@id="automation-NextPlanItem"]')

print(text)








