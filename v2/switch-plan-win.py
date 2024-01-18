#//////////////////////// PACKAGES /////////////////////////////

import time
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

#/////////////////// INFO & DEPENDENCIES //////////////////////

t1 = time.time()

#-------------------- Selenium Conf. --------------------------

# ser = Service(r'C:\Users\Sneezetify\sneezetify-netflix-automation\chromedriver')
# op = webdriver.ChromeOptions()
# op.add_experimental_option('excludeSwitches', ['enable-logging'])
# chromedriverpath = r'C:\Users\Sneezetify\sneezetify-netflix-automation\chromedriver'
# driver = webdriver.Chrome(service = ser, options = op)

ser = Service('/users/kautsaraqsa/code/netflix-automation/v2/chromedriver_2')
op = webdriver.ChromeOptions()
op.add_experimental_option('excludeSwitches', ['enable-logging'])
chromedriverpath = 'chromedriver'

#------------------------- URL --------------------------------
url_sp = 'https://www.netflix.com/changeplan'
url_cc = 'https://www.netflix.com/clearcookies'

#---------------------- Credentials Testing ---------------------------

email_id = 'jadine@sneezey.online'   
password = 'layar1'
region = 'PHP'
email_list = [email_id]
pass_list = [password]

#---------------------- Credentials Prod ---------------------------

# data = np.loadtxt('change-plan.csv', delimiter= ',', skiprows= 1, dtype= str).T
# email_list = data[0]
# pass_list = data[1]
# region = str(data[2][0])
# n_acc = len(email_list)

#------------------------- Logs ------------------------------

log_file = open('test_log.txt', 'a')

#/////////////////////// FUNCTION /////////////////////////////

def Click(element):
    driver.find_element(by = 'xpath', value = element).click()

def Filling(element, fill):
    field = driver.find_element(by = 'xpath', value = element)
    field.send_keys(fill)

def GetText(element):
    time.sleep(2)
    return driver.find_element(by = 'xpath', value = element).text

def ClearField(element):
    field = driver.find_element(by = 'xpath', value = element)
    field.send_keys(Keys.CONTROL + "a")
    field.send_keys(Keys.DELETE)

def ScrollDown(value = 1) :
    page = driver.find_element(by = 'tag name', value = 'html')  
    for scroll in range(value):  
        page.send_keys(Keys.ARROW_DOWN) 

def logging(text):
    print(text)
    log_file.write(text)
    log_file.write('\n')

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

def ChangePlan(plan, mode):

    plan_dict = {
        'dasar': '//*[@id="appMountPoint"]/div/div/div[2]/div/div/div[2]/label[2]/h2',
        'standar': '//*[@id="appMountPoint"]/div/div/div[2]/div/div/div[2]/label[3]/h2',
        'premium': '//*[@id="appMountPoint"]/div/div/div[2]/div/div/div[2]/label[4]/h2',
        'ponsel': '//*[@id="appMountPoint"]/div/div/div[2]/div/div/div[2]/label[1]/h2'
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
        Click(element = plan_dict[plan]) #click plan  

    time.sleep(1)

    ScrollDown(value = 3)

    Click(element = '//*[@id="appMountPoint"]/div/div/div[2]/div/div/div[3]/button[1]') #click 'Lanjut'
    

    time.sleep(1)


    Click(element = '//*[@id="appMountPoint"]/div/div/div[2]/div/div/div[4]/div/footer/div/button[1]') #click 'confirm'

    if mode == 'Downgrade' or mode == 'Upgrade':
        text = '{} {} Successful !'.format(mode.title(), email)
    else:
        text = 'Changing plan to {}: {}'.format(plan, email)
    logging(text)
    
    time.sleep(3)
        

def ClearCookies():
    driver.get(url_cc)
    time.sleep(3)

def Upgrade(email, password):
    global driver
    mode = 'Upgrade'
    try:
        SignIn(email_id =  email, password = password)
    except:
        text = 'INCORRECT: {}'.format(email)
        logging(text)
        return()
    ChangePlan('premium', mode)
    try:
        next_bill_date = GetText(element= '//*[@id="appMountPoint"]/div/div/div[3]/div/div/div[4]/div[1]/section/div[2]/div/div/div[1]/div[2]')
    except:
        next_bill_date = GetText(element = '//*[@id="appMountPoint"]/div/div/div[2]/div/div/div[4]/div[1]/section/div[2]/div/div/div[1]/div[2]')
    text = '{} : {}'.format(email, next_bill_date)
    logging(text)
    ClearCookies()
    
    

def Downgrade(email, password):
    mode = 'Downgrade'
    SignIn(email_id =  email, password = password)
    ChangePlan('dasar', mode)
    global driver
    ClearCookies()

def Complete(email, password):
    mode = 'Complete'
    global driver
    try:
        SignIn(email_id =  email, password = password)
        ChangePlan('dasar', mode)
    except:
        text = 'INCORRECT: {}'.format(email)
        logging(text)
        return None
    driver.get(url_sp)
    ChangePlan('standar', mode)
    driver.get(url_sp)
    ChangePlan('premium', mode)
    driver.get(url_sp)
    ChangePlan('ponsel', mode)
    next_bill = GetText(element= '//*[@id="automation-NextPlanItem"]')
    text = '{} : {}'.format(email, next_bill)
    logging(text)
    ClearCookies()

#///////////////////////// JOBS //////////////////////////////

#------------------------- RUN -----------------------------

logging('           Switch - Plan Job Logs            ')

logging('--------------------------------------------')

logging('///////////////// JOB START ////////////////')

for email, password in zip(email_list, pass_list):
    
    log_file = open('test_log.txt', 'a')

    driver = webdriver.Chrome(service = ser, options = op)

    try:    
        Complete(email, password)
    except:
        text = 'FAILED: {}'.format(email)
        logging(text)

    driver.close()

    log_file.close()

t2 = time.time()

print("Running Time = ", t2-t1)