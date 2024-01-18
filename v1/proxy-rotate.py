import requests
import random
import time
import numpy as np
import concurrent.futures
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

#/////////////////// INFO & DEPENDENCIES //////////////////////

#-------------------- Proxy List --------------------------
#opens a csv file of proxies and prints out the ones that work with the url in the extract function
proxylist = np.loadtxt('freeproxy.txt', dtype=str)

#-------------------- Selenium Conf. --------------------------

# PROXY = proxylist[1]
# print(PROXY)
ser = Service('/Users/kautsaraqsa/netflix-automation/chromedriver')
op = webdriver.ChromeOptions()
# op.add_argument('--proxy-server=%s' % PROXY)

chromedriverpath = '/Users/kautsaraqsa/netflix-automation/chromedriver'
driver = webdriver.Chrome(service = ser, options = op)

#------------------------- URL --------------------------------
url_lh = 'https://www.netflix.com/loginhelp'
url_cc = 'https://www.netflix.com/clearcookies'


#---------------------- Credentials ---------------------------

email_id = 'zokoid@netsneeze.com'
# email_id = 'darmawanandi121@gmail.com'

#/////////////////////// FUNCTION /////////////////////////////

def Click(element):
    driver.find_element(by = 'xpath', value = element).click()

def ClearCookies():
    driver.get(url_cc)
    time.sleep(3)

def Filling(element, fill):
    field = driver.find_element(by = 'xpath', value = element)
    field.send_keys(fill)

def GetText(element):
    time.sleep(2)
    return driver.find_element(by = 'xpath', value = element).text

#--------------------- TASKS --------------------------

def tasks():

    driver.get(url_lh)   

    time.sleep(2)

    Filling(element = '//*[@id="forgot_password_input"]', fill = email_id) #filling email

    time.sleep(1)

    Click(element= '//*[@id="appMountPoint"]/div/div[3]/div[1]/div/button') #click 'email me'

    time.sleep(2)

    text = GetText(element='//*[@id="appMountPoint"]/div/div[3]/div[1]/div/h2')

    print(text)
    

# def extract(proxy):
#     #this was for when we took a list into the function, without conc futures.
#     #proxy = random.choice(proxylist)
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'}
#     try:
#         #change the url to https://httpbin.org/ip that doesnt block anything
#         r = requests.get('https://httpbin.org/ip', headers=headers, proxies={'http' : proxy,'https': proxy}, timeout=2)
#         print(r.json(), ' | Works')
#     except:
#         pass
#     return proxy

# with concurrent.futures.ThreadPoolExecutor() as executor:
#         executor.map(extract, proxylist)

for i in range(10):
    try:
        tasks()
    except:
        print('Percobaan ke {} gagal...'.format(i+1))
        driver.get(url_cc) 

