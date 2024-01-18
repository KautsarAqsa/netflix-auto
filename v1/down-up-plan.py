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

# email_id = 'zokoid@netsneeze.com'
# password = 'sneeze1'

data = np.loadtxt('change-plan.csv', delimiter= ',', skiprows= 1, dtype= str).T
email_list = data[0]
pass_list = data[1]
region = str(data[2][0])
n_acc = len(email_list)

#------------------------- Logs ------------------------------

log_file = open('test_log.txt', 'a')

#/////////////////////// FUNCTION /////////////////////////////

def Click(element):
    driver.find_element(by = 'xpath', value = element).click()

def Filling(element, fill):
    field = driver.find_element(by = 'xpath', value = element)
    field.send_keys(fill)

def GetText(element, method = 'xpath'):
    time.sleep(2)
    return driver.find_element(by = method, value = element).text

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

    try:
        Filling(element = '/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[1]/div[1]/div/label/input', fill = email_id) #filling email
        Filling(element = '/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[2]/div/div/label/input', fill = password) #filling password
        
        time.sleep(1)
        
        Click(element= '/html/body/div[1]/div/div[3]/div/div/div[1]/form/button') #click 'sign in'
        
        time.sleep(3)

    except:
        text = 'DENIED: {}'.format(email)
        logging(text)

def ChangePlan(plan, mode):

    global email

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

    try:
        inco = GetText(element = '//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/div/div[2]')
        output = 'INCORRECT : {}'.format(email)

    except:
    
        global region

        if region == 'BRL' or region == 'COP':
            Click(element= plan_dict_brl[plan])
        else :
            try:
                Click(element = plan_dict[plan]) #click plan
            except:
                Click(element= plan_dict_2[plan])    

        time.sleep(1)

        ScrollDown(value = 3)

        try:
            Click(element = '//*[@id="appMountPoint"]/div/div/div[3]/div/div/div[2]/button[1]')
        except:
            Click(element = '//*[@id="appMountPoint"]/div/div/div[2]/div/div/div[2]/button[1]') #click 'Lanjut'
        
        time.sleep(1)
        try:
            try:
                Click(element = '//*[@id="appMountPoint"]/div/div/div[3]/div/div/div[3]/div/footer/div/button[1]') #click 'confirm'
            except:
                Click(element = '//*[@id="appMountPoint"]/div/div/div[2]/div/div/div[3]/div/footer/div/button[1]')
        except:
            current = GetText(element = '//*[@id="appMountPoint"]/div/div/div[2]/div/div/ul/li[3]/div[1]/h2/div/div')
            output = email + ' : ' + current
        
        time.sleep(3)
        
        return output


def ClearCookies():
    driver.get(url_cc)
    time.sleep(3)


def Upgrade(email, password):
    global driver
    Mode = 'Upgrade'
    SignIn(email_id =  email, password = password)
    Output = ChangePlan('premium', Mode)
    try:
        try:
            next_bill_date = GetText(element= '//*[@id="appMountPoint"]/div/div/div[3]/div/div/div[4]/div[1]/section/div[2]/div/div/div[1]/div[2]')
        except:
            next_bill_date = GetText(element = '//*[@id="appMountPoint"]/div/div/div[2]/div/div/div[4]/div[1]/section/div[2]/div/div/div[1]/div[2]')
        text = '{} : {}'.format(email, next_bill_date)
        logging(text)
    except:
        Output = Output
    ClearCookies()
    return Mode, Output
    
    
def Downgrade(email, password):
    global driver
    Mode = 'Downgrade'
    SignIn(email_id =  email, password = password)
    Output = ChangePlan('dasar', Mode)
    ClearCookies()
    return Mode, Output

#///////////////////////// JOBS //////////////////////////////

#------------------------- RUN -----------------------------

logging('           Switch - Plan Job Logs            ')

logging('--------------------------------------------')

logging('///////////////// JOB START ////////////////')

for email, password in zip(email_list, pass_list):
    
    log_file = open('test_log.txt', 'a')

    driver = webdriver.Chrome(service = ser, options = op)
    

    Mode, Output = Upgrade(email, password)
    logging('{} : {}'.format(email, Output))
    
    driver.close()

log_file.close()

t2 = time.time()

print("Running Time = ", t2-t1)