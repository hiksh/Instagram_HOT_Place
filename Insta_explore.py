from selenium import webdriver
import chromedriver_autoinstaller 
import time
import os
import csv
import pandas as pd
import datetime
from getpass import getpass

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from dotenv import load_dotenv

load_dotenv()
id=os.getenv("INSTA_ID")
password = os.getenv("INSTA_PW")

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.implicitly_wait(3) #wait until the program get content of the web browser

insta_url="https://www.instagram.com/"
driver.get(url=insta_url)
time.sleep(2)

driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(id)
driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button').send_keys(Keys.ENTER)
time.sleep(10)

explore_code="263599627329649"
explore_url=f"https://www.instagram.com/explore/locations/{explore_code}/"
driver.get(url=explore_url)
time.sleep(7)
a=driver.execute_script("return document.body.scrollHeight;")

while True:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(10)
    if driver.execute_script("return document.body.scrollHeight;")==a:
        print("break")
        break
    else:
        a=driver.execute_script("return document.body.scrollHeight;")

driver.execute_script("window.scrollTo(document.body.scrollHeight,0);")

print("-----------------------------------------------------")
print("Store ID and context")
print("-----------------------------------------------------")

ids=[]
Contexts=[]
trial=1
driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[2]/div/div[1]/div[1]/a/div[1]/div[2]').click()
time.sleep(10)
while True:
    print(f'{trial}')
    for i in [5,6,7,8]:
        try:
            id=driver.find_element(By.XPATH,f'/html/body/div[{i}]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[1]/div/div/span/span/div/a')
            ids.append(id.text)
            print(id.text)
            break
        except:
            print(f"error:{trial},{i}")
            if i==8:
                for x in [5,6,7,8]:
                    try:
                        id=driver.find_element(By.XPATH,f'/html/body/div[{x}]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/div/li/div/div/div[2]/h2/div/span/div/a')
                        ids.append(id.text)
                        i=x
                        break
                    except:
                        print("error")
                        pass
            continue
    try:
        Context=driver.find_element(By.XPATH,f'/html/body/div[{i}]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/div/li/div/div/div[2]/div[1]/h1')
        Contexts.append(Context.text)
        if trial==1:
            print(Context.text)
    except:
        print("there is no context")
        Contexts.append(None)
        pass
    try:
        driver.find_element(By.XPATH,f'/html/body/div[{i}]/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button').click()
        time.sleep(5)
        trial=trial+1
    except:
        print("This is the last post")
        break

    #try:
    #    id=driver.find_element(By.XPATH,'/html/body/div[7]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[1]/div/div/span/span/div/a')
    #    ids.append(id.text)
    #except:
    #    try:
    #        id=driver.find_element(By.XPATH,'/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[1]/div/div/span/span/div/a')
    #        ids.append(id.text)
    #    except:   
    #        print(f"id error {trial}")
    #        pass


print("Done!!")

ex_df=pd.DataFrame({'Id':ids,'Context':Contexts})
now=datetime.datetime.now()
date=now.strftime('%Y-%m-%d')
ex_df['Date']=date
ex_df.to_csv("ex_crawlingdata.csv")

time.sleep(10)
