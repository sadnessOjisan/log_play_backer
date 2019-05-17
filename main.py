#coding:utf-8

import time
from selenium import webdriver
import chromedriver_binary
import json

LOCAL_HOST = 'http://localhost:8080'

f = open('./log.json', 'r')
jsonData = json.load(f)
f.close()
logArray = jsonData['log']
driver = webdriver.Chrome()
for log in logArray:
    if log['eventType'] == 'LOAD': 
        if driver.current_url != LOCAL_HOST + log['url']: 
            driver.get(LOCAL_HOST + log['url'])
    elif log['eventType'] == 'CLICK': 
        try: 
            target = driver.find_element_by_xpath("//*[@data-testid='"+log['target']+"']")
            target.click()
        except: 
            driver.get(LOCAL_HOST + log['url'])
    elif log['eventType'] == 'BLUR':
        try: 
            inputValue = log['property']['inputValue']
            target = driver.find_element_by_xpath("//*[@data-testid='"+log['target']+"']")
            target.send_keys(inputValue)
        except: 
            driver.get(LOCAL_HOST + log['url'])
    elif log['eventType'] == 'SUBMIT': 
        try:
            driver.find_element_by_xpath("//*[@data-testid='"+log['target']+"']")
            target = driver.find_element_by_xpath("//*[@data-testid='"+log['target']+"']")
            target.click()
        except: 
            driver.get(LOCAL_HOST + log['url'])
    else: 
        driver.get(LOCAL_HOST + log['url'])
    time.sleep(1)