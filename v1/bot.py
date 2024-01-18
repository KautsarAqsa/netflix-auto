#//////////////////////// PACKAGES /////////////////////////////

import time
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

#/////////////////// INFO & DEPENDENCIES //////////////////////

t1 = time.time()

#--------------------- Selenium Conf --------------------------

ser = Service('/Users/kautsaraqsa/netflix-automation/chromedriver')
op = webdriver.ChromeOptions()
chromedriverpath = '/Users/kautsaraqsa/netflix-automation/chromedriver'
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
'sneeze1': 'admin1',
'admin1': 'layar1',
'layar1': 'layar123',
'layar123': 'stream1',
'stream1': 'watch1',
'watch1': 'loyal1',
'loyal1': '232323',
'232323': 'sneeze1'
}

data = np.loadtxt('account-test.csv', delimiter= ',', skiprows= 1, dtype= str).T
email_list = data[0]
pass_list = data[1]
n_acc = len(email_list)

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
    field.send_keys(Keys.COMMAND + "a")
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
    time.sleep(2)

    #----------------------- Sign In ---------------------------

    Logging('{} : Test-Participation'.format(email_id))
    
    Filling(element = '/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[1]/div[1]/div/label/input', fill = email_id) #filling email
    Filling(element = '/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[2]/div/div/label/input', fill = password) #filling password

    time.sleep(1)

    Click(element= '//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button') #click 'sign in'

    time.sleep(3)

    #----------------------- TP On/Off ---------------------------
    try:
        try:
            status = GetText(element = '/html/body/div[1]/div/div/div[3]/div/form/fieldset/label')
            if status == 'HIDUP' or status == 'ON':
                Click(element = '//*[@id="appMountPoint"]/div/div/div[3]/div/form/fieldset/label/button')
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

    Click(element = '//*[@id="appMountPoint"]/div/div/div[2]/div/form/div/button') #click on 'done' button

    time.sleep(2)

    #----------------------- Open URL DP ---------------------------

    Logging('{} : Delete-Profile'.format(email_id))

    driver.get(url_dp)
    time.sleep(3)

    #----------------------- Delete Profile ----------------------------

    try:
        ClearField(element= '//*[@id="id_ownerName"]') #clear main profile
        Filling(element= '//*[@id="id_ownerName"]', fill = '1') #fill main profile

        ClearField(element= '//*[@id="id_profile1Name"]') #clear profile 1
        ClearField(element= '//*[@id="id_profile3Name"]') #clear profile 2
        ClearField(element= '//*[@id="id_profile2Name"]') #clear profile 3
        ClearField(element= '//*[@id="id_profile4Name"]') #clear profile 4

        time.sleep(1)

        Click(element= '//*[@id="appMountPoint"]/div/div/div/div[2]/div/div/div[2]/form/button[2]') #click 'next'

        time.sleep(3)
    except:
        log = '{} : Failed on Deleting Profile'.format(email_id)
        Output = 'Failed on Deleting Profile'
        Logging(log)

    #----------------------- Open URL RP ---------------------------

    Logging('{} : Remove-Pin'.format(email_id))

    driver.get(url_rp)
    time.sleep(2)

    #------------------- Parental Password ----------------------

    Logging('{} : Parental-Password'.format(email_id))

    Filling(element = '//*[@id="input-account-content-restrictions"]', fill = password) #fill password in parental page

    time.sleep(1)

    Click(element = '//*[@id="appMountPoint"]/div/div/div[2]/div/div/div[2]/div[2]/button[1]') #click on 'continue'

    time.sleep(2)

    #-------------------- Unlock Profile ------------------------

    Logging('{} : Unlock-Profile'.format(email_id))

    try:
        ScrollDown(1)

        time.sleep(1)

        #try to find hidden element, then click
        try:
            driver.find_element(by = 'xpath', value = '//*[@id="appMountPoint"]/div/div/div[2]/div/div/div/div[1]/ul/li/div[2]/div[3]/div[2]')
            Click(element = '//*[@id="appMountPoint"]/div/div/div[2]/div/div/div/div[1]/ul/li/div[2]/div[3]/div[1]') 
        except:
            Logging('{} : Profile already has no PIN !'.format(email_id))    

        ScrollDown(5)

        time.sleep(1)

        Click(element = '//*[@id="appMountPoint"]/div/div/div[2]/div/div/div/div[1]/div[2]/button[1]')  #click on 'yes'

        time.sleep(2)
    except:
        log = '{} : Failed to unlock profile'.format(email_id)
        Output = 'Failed to unlock profile'
        Logging(log)

    #----------------------- Open URL ---------------------------

    Logging('{} : Clear-History'.format(email))

    driver.get(url_ch)
    time.sleep(2)

    #--------------------- Hide History -------------------------

    try:
        hide = driver.find_element(by = 'class name', value = "viewing-activity-footer-hide")
        hide.click()
        Click(element = '//*[@id="appMountPoint"]/div/div/div[2]/div/div/div[3]/div[3]/div/footer/div/button[1]')
    except:
        log = '{} : History already empty'.format(email_id)
        Logging(log)

    time.sleep(2)

    #----------------------- Open URL ---------------------------

    Logging('{} : Change-Password'.format(email_id))
    driver.get(url_cp)
    time.sleep(2)

    #--------------------- Change Password ----------------------

    Filling(element = '//*[@id="id_currentPassword"]', fill = password)

    time.sleep(1)

    Filling(element = '//*[@id="id_newPassword"]', fill = new_password)

    time.sleep(1)

    Filling(element = '//*[@id="id_confirmNewPassword"]', fill = new_password)

    time.sleep(1)

    Click(element = '//*[@id="btn-save"]')

    time.sleep(3)

    #----------------------- Clear Cookies ---------------------------

    Logging('{} : Clear-Cookies'.format(email_id))

    driver.get(url_cc)

    #------------------------ Finishing -----------------------------
    
    time.sleep(4)

    return Output

#////////////////////////////// RUN ////////////////////////////////////

results = []
list_email = []
for email, password in zip(email_list, pass_list):
    
    driver = webdriver.Chrome(service = ser, options = op)

    try:
        out = jobs(email_id= email, password= password)
        driver.close()
    except:
        log = '{} : DENIED!'.format(email)
        out = 'DENIED!'
        driver.close()
        Logging(log)
        break

    results.append(out)
    list_email.append(email)

t2 = time.time()

print("Running Time = ", t2-t1)

#//////////////////////////// CREATE RESULT TABLE /////////////////////

result_matrix = np.array([list_email, results]).T

np.savetxt('hackback-result.csv',result_matrix, delimiter=',', fmt='%s')




