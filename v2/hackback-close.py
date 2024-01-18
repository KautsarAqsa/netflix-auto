#//////////////////////// PACKAGES /////////////////////////////

import time
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

#/////////////////// INFO & DEPENDENCIES //////////////////////

t1 = time.time()

#--------------------- Selenium Conf --------------------------

ser = Service(r'C:\Users\finno\netflix-auto\chromedriver')
# ser = Service('/Users/kautsaraqsa/Code/netflix-automation/v2/chromedriver')
op = webdriver.ChromeOptions()
op.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service = ser, options = op)

#------------------------- URL -------------------------------

url_cp = 'https://www.netflix.com/password'
url_cc = 'https://www.netflix.com/clearcookies'
url_tp = 'https://www.netflix.com/DoNotTest'
url_dp = 'https://www.netflix.com/simpleSetup/newprofiles'
url_rp = 'https://www.netflix.com/settings/migration'
url_ch = 'https://www.netflix.com/settings/viewed/LNUIX7J2AFHJ7MS7RKSYCCRFJY'

#--------------------- Credentials -------------------------


pass_dict = {
'alami3': 'shake3',
'shake3': 'sekai3',
'sekai3': 'tisue3',
'tisue3': 'monde3',
'monde3': 'force3',
'force3': 'abbey3',
'abbey3': 'ayara3',
'ayara3': 'alami3',
'hutri78': 'tisue3',
'safar1': 'force3'
}

data = np.loadtxt('hackback.csv', delimiter= ',', skiprows= 1, dtype= str).T
email_list = data[0]
pass_list = data[1]
n_acc = len(email_list)

# email_list = ['lachas@sneezey.online']
# pass_list = ['safar1']

#--------------------- Logs -------------------------

log_file = open('hackback_log.txt', 'a')

#/////////////////////// FUNCTION ////////////////////////////

def Click(element):
    driver.find_element(by = 'xpath', value = element).click()

def Filling(element, fill):
    field = driver.find_element(by = 'xpath', value = element)
    field.send_keys(fill)

def GetText(element):
    return driver.find_element(by = 'xpath', value = element).text

def ClearField(element):
    field = driver.find_element(by = 'xpath', value = element)
    field.send_keys(Keys.CONTROL + "a")
    # field.send_keys(Keys.COMMAND + "a")
    field.send_keys(Keys.DELETE)

def ScrollDown(value = 1) :
    page = driver.find_element(by = 'tag name', value = 'html')  
    for i in range(value):  
        page.send_keys(Keys.ARROW_DOWN) 

def Logging(text):
    print(text)
    log_file.write(text)
    log_file.write('\n')

#///////////////////////// JOBS //////////////////////////////

Logging('------------------ JOB START ----------------')

def jobs(email_id, password):

    Output = 'SUCCESSFUL!'

    global driver

    #--------------------- generate new password -------------------------

    new_password = pass_dict[password]
            
    #--------------------- Open URL TP -------------------------

    driver.get(url_tp)
    time.sleep(1)

    #----------------------- Sign In ---------------------------

    Logging('{} : Test-Participation'.format(email_id))
    
    Filling(element = '/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[1]/div[1]/div/label/input', fill = email_id) #filling email
    Filling(element = '/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[2]/div/div/label/input', fill = password) #filling password

    time.sleep(1)

    Click(element= '//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button') #click 'sign in'

    time.sleep(8)

    #----------------------- TP On/Off ---------------------------
    try:
        try:
            status = GetText(element = '/html/body/div[1]/div/div/div/div[3]/div/form/fieldset/label')
            if status == 'HIDUP' or status == 'ON':
                Click(element = '//*[@id="appMountPoint"]/div/div/div/div[3]/div/form/fieldset/label/button')
        except:
            status = GetText(element = '/html/body/div[1]/div/div/div[2]/div/form/fieldset/label')
            if status == 'HIDUP' or status == 'ON':
                Click(element = '//*[@id="appMountPoint"]/div/div/div[2]/div/form/fieldset/label/button')
    except:
        inco = GetText(element = '//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/div/div[2]')
        log = '{} : INCORRECT'.format(email_id)
        Output = 'INCORRECT' 
        Logging(log)
        return Output

    time.sleep(1)
    
    try:
        Click(element = '//*[@id="appMountPoint"]/div/div/div[2]/div/form/div/button') #click on 'done' button
    except:
        Click(element = '//*[@id="appMountPoint"]/div/div/div/div[3]/div/form/div/button') 

    time.sleep(1)

    #----------------------- Open URL DP ---------------------------

    Logging('{} : Delete-Profile'.format(email_id))

    driver.get(url_dp)
    time.sleep(2)

    #----------------------- Delete Profile ----------------------------

    try:
        ClearField(element= '//*[@id="id_ownerName"]') #clear main profile
        Filling(element= '//*[@id="id_ownerName"]', fill = '1') #fill main profile

        ClearField(element= '//*[@id="id_profile1Name"]') #clear profile 1

        ClearField(element= '//*[@id="id_profile2Name"]') #clear profile 2
        
        ClearField(element= '//*[@id="id_profile3Name"]') #clear profile 3

        ClearField(element= '//*[@id="id_profile4Name"]') #clear profile 4

        time.sleep(1)

        Click(element= '//*[@id="appMountPoint"]/div/div/div/div/div[2]/div/div/div[2]/form/button[2]') #click 'next'

        time.sleep(1)

    except:
        log = '{} : Failed on Deleting Profile'.format(email_id)
        Output = 'Failed on Deleting Profile'
        Logging(log)
    
    driver.get(url_dp)
    time.sleep(1)

    # Fill new profile

    Filling(element= '//*[@id="id_profile1Name"]', fill = '2')

    Filling(element = '//*[@id="id_profile2Name"]', fill = '3')
    
    Filling(element = '//*[@id="id_profile3Name"]', fill = '4')

    Filling(element = '//*[@id="id_profile4Name"]', fill = '5')

    time.sleep(1)

    Click(element= '//*[@id="appMountPoint"]/div/div/div/div/div[2]/div/div/div[2]/form/button[2]') #click 'next'

    time.sleep(1)

    #----------------------- Open URL RP ---------------------------

    Logging('{} : Remove-Pin'.format(email_id))

    driver.get(url_rp)
    #time.sleep(1)

    #------------------- Parental Password ----------------------

    Logging('{} : Parental-Password'.format(email_id))

    Filling(element = '//*[@id="input-account-content-restrictions"]', fill = password) #fill password in parental page

    time.sleep(5)

    try:
        Click(element = '//*[@id="appMountPoint"]/div/div/div[2]/div/div/div[2]/div[2]/button[1]') #click on 'continue'
    except:
        Click(element = '//*[@id="appMountPoint"]/div/div/div/div[3]/div/div/div[2]/div[2]/button[1]') #click on 'continue'
        
    time.sleep(1)

    #-------------------- Unlock Profile ------------------------

    Logging('{} : Unlock-Profile'.format(email_id))

    try:
        ScrollDown(1)

        time.sleep(1)

        #try to find hidden element, then click
        try:
            driver.find_element(by = 'class name', value = 'pin-input-container')
            try:
                Click(element = '//*[@id="appMountPoint"]/div/div/div[2]/div/div/div/div[1]/ul/li/div[2]/div[3]/div[1]') 
            except:
                Click(element = '//*[@id="appMountPoint"]/div/div/div/div[3]/div/div/div/div[1]/ul/li/div[2]/div[3]/div[1]')
        except:
            Logging('{} : Profile already has no PIN !'.format(email_id))    

        ScrollDown(5)

        time.sleep(1)

        try:
            Click(element = '//*[@id="appMountPoint"]/div/div/div[2]/div/div/div/div[1]/div[2]/button[1]')  #click on 'yes'
        except:
            Click(element = '//*[@id="appMountPoint"]/div/div/div/div[3]/div/div/div[2]/div[2]/button[1]')

        time.sleep(1)
    except:
        # raise KeyError
        log = '{} : Failed to unlock profile'.format(email_id)
        Output = 'Failed to unlock profile'
        Logging(log)

    #----------------------- Open URL ---------------------------

    Logging('{} : Clear-History'.format(email))

    driver.get(url_ch)
    time.sleep(1)

    #--------------------- Hide History -------------------------

    try:
        hide = driver.find_element(by = 'class name', value = "viewing-activity-footer-hide")
        hide.click()
        time.sleep(3)

        try:
            Click(element = '//*[@id="appMountPoint"]/div/div/div[2]/div/div/div[2]/div[3]/div/footer/div/button[1]')
        except:
            Click(element = '//*[@id="appMountPoint"]/div/div/div/div[3]/div/div/div[2]/div[3]/div/footer/div/button[1]')

    except:
        log = '{} : History already empty'.format(email_id)
        Logging(log)

    time.sleep(1)

    #----------------------- Open URL ---------------------------

    Logging('{} : Change-Password'.format(email_id))
    driver.get(url_cp)
    #time.sleep(1)

    #--------------------- Change Password ----------------------

    Filling(element = '//*[@id="id_currentPassword"]', fill = password)

    #time.sleep(1)

    Filling(element = '//*[@id="id_newPassword"]', fill = new_password)

    #time.sleep(1)

    Filling(element = '//*[@id="id_confirmNewPassword"]', fill = new_password)

    time.sleep(2)

    Click(element = '//*[@id="btn-save"]')

    time.sleep(3) #semula 3

    #----------------------- Clear Cookies ---------------------------

    Logging('{} : Clear-Cookies'.format(email_id))

    driver.get(url_cc)
    time.sleep(4)

    #------------------------ Finishing -----------------------------
    

    return Output

#////////////////////////////// RUN ////////////////////////////////////

results = []
list_email = []
for email, password in zip(email_list, pass_list):
    
    driver = webdriver.Chrome(service = ser, options = op)

    log_file = open('hackback_log.txt', 'a')

    try:
        out = jobs(email_id= email, password= password)
        driver.close()
    except:
        log = '{} : DENIED!'.format(email)
        out = 'DENIED!'
        driver.close()
        Logging(log)

    results.append(out)
    list_email.append(email)
    
    log_file.close()

t2 = time.time()

print("Running Time = ", t2-t1)

#//////////////////////////// CREATE RESULT TABLE /////////////////////

result_matrix = np.array([list_email, results]).T

np.savetxt('hackback-result.csv',result_matrix, delimiter=',', fmt='%s')