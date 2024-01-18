#//////////////////////// PACKAGES /////////////////////////////

import time
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

#/////////////////// INFO & DEPENDENCIES //////////////////////

t1 = time.time()

#-------------------- Selenium Conf. --------------------------

ser = Service('/Users/kautsaraqsa/netflix-automation/chromedriver')
op = webdriver.ChromeOptions()
chromedriverpath = '/Users/kautsaraqsa/netflix-automation/chromedriver'
driver = webdriver.Chrome(service = ser, options = op)

#------------------------- URL --------------------------------
url_sp = 'https://www.netflix.com/changeplan'
url_cc = 'https://www.netflix.com/clearcookies'

#---------------------- Credentials ---------------------------

email_id = 'gi@sneezey.online'
password = 'layar1'

email_list = [email_id]
pass_list = [password]

# data = np.loadtxt('change-plan.csv', delimiter= ',', skiprows= 1, dtype= str).T
# email_list = data[0]
# pass_list = data[1]
# region = data[2][0].astype(str)
# n_acc = len(email_list)

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

#--------------------- Change Plan --------------------------

def SignIn(email_id, password):
    
    global driver 
    
    driver.get(url_sp)   

    time.sleep(2)

    Filling(element = '/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[1]/div[1]/div/label/input', fill = email_id) #filling email
    Filling(element = '/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[2]/div/div/label/input', fill = password) #filling password
    
    time.sleep(1)
    
    Click(element= '/html/body/div[1]/div/div[3]/div/div/div[1]/form/button') #click 'sign in'
    
    time.sleep(3)

def ChangePlan(plan):

    plan_dict = {
        'dasar': '//*[@id="appMountPoint"]/div/div/div[3]/div/div/ul/li[2]',
        'standar': '//*[@id="appMountPoint"]/div/div/div[3]/div/div/ul/li[3]',
        'premium': '//*[@id="appMountPoint"]/div/div/div[3]/div/div/ul/li[4]',
        'ponsel': '//*[@id="appMountPoint"]/div/div/div[3]/div/div/ul/li[1]'
        }
    
    plan_dict_2 = {
        'dasar': '//*[@id="appMountPoint"]/div/div/div[2]/div/div/ul/li[2]',
        'standar': '//*[@id="appMountPoint"]/div/div/div[2]/div/div/ul/li[3]',
        'premium': '//*[@id="appMountPoint"]/div/div/div[2]/div/div/ul/li[4]',
        'ponsel': '//*[@id="appMountPoint"]/div/div/div[2]/div/div/ul/li[1]'
        }

    plan_dict_brl = {
        'dasar': '//*[@id="appMountPoint"]/div/div/div[2]/div/div/ul/li[1]',
        'standar': '//*[@id="appMountPoint"]/div/div/div[2]/div/div/ul/li[2]',
        'premium': '//*[@id="appMountPoint"]/div/div/div[2]/div/div/ul/li[3]',
        }

    global region

    if region == 'BRL' or region == 'COP':
        Click(element= plan_dict_brl[plan])
    else :
        try:
            Click(element = plan_dict[plan]) #click plan
        except:
            Click(element= plan_dict_2[plan])    

    time.sleep(3)

    ScrollDown(value = 3)

    try:
        Click(element = '//*[@id="appMountPoint"]/div/div/div[3]/div/div/div[2]/button[1]')
    except:
        Click(element = '//*[@id="appMountPoint"]/div/div/div[2]/div/div/div[2]/button[1]') #click 'Lanjut'
    

    time.sleep(3)

    try:
        Click(element = '//*[@id="appMountPoint"]/div/div/div[3]/div/div/div[3]/div/footer/div/button[1]') #click 'confirm'
    except:
        Click(element = '//*[@id="appMountPoint"]/div/div/div[2]/div/div/div[3]/div/footer/div/button[1]')

    time.sleep(3)

    print(plan)

def Upgrade(email, password):
    SignIn(email_id =  email, password = password)
    ChangePlan('premium')
    global driver
    driver.get(url_cc)
    print('Upgrade: ', email, 'successful !')

def Downgrade(email, password):
    SignIn(email_id =  email, password = password)
    ChangePlan('dasar')
    global driver
    driver.get(url_cc)
    print('Downgrade: ', email, 'successful !')

def Complete(email, password):
    global driver
    SignIn(email_id =  email, password = password)
    ChangePlan('dasar')
    driver.get(url_sp)
    ChangePlan('standar')
    driver.get(url_sp)
    ChangePlan('premium')
    driver.get(url_sp)
    ChangePlan('ponsel')
    driver.get(url_cc)
    print('Complete: ', email, 'successful !')

#///////////////////////// JOBS //////////////////////////////

#------------------------- RUN -----------------------------

for email, password in zip(email_list, pass_list):
    Complete(email, password)

t2 = time.time()

print("Running Time = ", t2-t1)