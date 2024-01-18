#//////////////////////// PACKAGES /////////////////////////////

import time
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from threading import Thread

#/////////////////// INFO & DEPENDENCIES //////////////////////

t1 = time.time()

#--------------------- Selenium Conf --------------------------

ser = Service('/Users/kautsaraqsa/netflix-automation/chromedriver')
op = webdriver.ChromeOptions()
chromedriverpath = '/Users/kautsaraqsa/netflix-automation/chromedriver'
driver_1 = webdriver.Chrome(service = ser, options = op)
driver_2 = webdriver.Chrome(service = ser, options = op)

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
n = len(email_list)
sep = int(n/2)
email_list_1 = email_list[:sep]
email_list_2 = email_list[sep:]
pass_list_1 = pass_list[:sep]
pass_list_2 = pass_list[sep:]

#--------------------- Logs -------------------------

log_file = open('hackback_log.txt', 'a')

#/////////////////////// FUNCTION ////////////////////////////

def Click(element, driver):
    driver.find_element(by = 'xpath', value = element).click()

def Filling(element, fill, driver):
    field = driver.find_element(by = 'xpath', value = element)
    field.send_keys(fill)

def GetText(element, driver):
    return driver.find_element(by = 'xpath', value = element).text

def ClearField(element, driver):
    field = driver.find_element(by = 'xpath', value = element)
    field.send_keys(Keys.COMMAND + "a")
    field.send_keys(Keys.DELETE)

def ScrollDown(driver, value = 1) :
    page = driver.find_element(by = 'tag name', value = 'html')  
    for i in range(value):  
        page.send_keys(Keys.ARROW_DOWN) 

def Logging(text):
    print(text)
    log_file.write(text)
    log_file.write('\n')

#///////////////////////// JOBS //////////////////////////////

Logging('------------------ JOB START ----------------')

def jobs(email_id, password, driver_n):

    Output = 'SUCCESSFUL!'

    #--------------------- generate new password -------------------------

    new_password = pass_dict[password]
            
    #--------------------- Open URL TP -------------------------

    driver_n.get(url_tp)
    time.sleep(4)

    #----------------------- Sign In ---------------------------

    Logging('{} : Test-Participation'.format(email_id))
    
    Filling(element = '/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[1]/div[1]/div/label/input', fill = email_id) #filling email
    Filling(element = '/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[2]/div/div/label/input', fill = password) #filling password

    time.sleep(1)

    Click( driver = driver_n, element= '//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button') #click 'sign in'

    time.sleep(3)

    #----------------------- Clear Cookies ---------------------------

    Logging('{} : Clear-Cookies'.format(email_id))

    driver.get(url_cc)

    #------------------------ Finishing -----------------------------
    
    time.sleep(4)

    return Output

#////////////////////////////// RUN ////////////////////////////////////

results_1, results_2 = [], []
list_email_1, list_email_2 = [], []

def run(results_list, list_email, email_list, pass_list, driver):
    for email, password in zip(email_list, pass_list):

        try:
            out = jobs(email_id= email, password = password, driver = driver)
            driver.close()
        except:
            log = '{} : DENIED!'.format(email)
            out = 'DENIED!'
            driver.close()
            Logging(log)

        results_list.append(out)
        list_email.append(email)


x1 = Thread(target = run, args=(results_1, list_email_1, email_list_1, pass_list_1, driver_1))
x2 = Thread(target = run, args=(results_2, list_email_2, email_list_2, pass_list_2, driver_2))

x1.start()
x2.start()

x1.join()
x2.join()

t2 = time.time()
print("Running Time = ", t2-t1)

#//////////////////////////// CREATE RESULT TABLE /////////////////////

# result_matrix = np.array([list_email, results]).T

# np.savetxt('hackback-result.csv',result_matrix, delimiter=',', fmt='%s')




