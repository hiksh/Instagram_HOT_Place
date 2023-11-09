# import
from selenium import webdriver
import chromedriver_autoinstaller
import time
from getpass import getpass

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

import os
import subprocess
import sys
from dotenv import load_dotenv

import datetime

chromedriver_autoinstaller.install()

# open csv to store
import csv


if os.path.isfile('crawlingdata.csv'):
    print("There is original file")
    f=open('crawlingdata.csv', 'a', newline='', encoding='utf-8-sig')
    wr = csv.writer(f)
else:
    print("Make new file")
    f=open('crawlingdata.csv', 'w', newline='',encoding='utf-8-sig')
    wr = csv.writer(f)
    wr.writerow(['date', 'img_alt', 'id', 'content'])
    
print("-----------------------------------------------------")
print("Opening the csv file")
print("-----------------------------------------------------")
time.sleep(1)

# login instagram
load_dotenv()
id = input("ID: ")
password = getpass("Password: ")
driver = webdriver.Chrome()
driver.implicitly_wait(5)

insta_url = 'https://www.instagram.com/'
driver.get(url=insta_url)
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(id)
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()
time.sleep(10)

# go hashtag page
hastag = "제주맛집"
hashtag_url = f"https://www.instagram.com/explore/tags/{hastag}/"
driver.get(url = hashtag_url)

print("-----------------------------------------------------")
print("Store date and img alt")
print("-----------------------------------------------------")
# finding all and store with date
time.sleep(5)
todayDatas =[]
now=datetime.datetime.now()
date=now.strftime('%Y-%m-%d')
print(date)

for c in range(3):
    for r in range(9):
        textImg = driver.find_element(By.XPATH, f'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div/div/div/div[{r+1}]/div[{c+1}]/a/div[1]/div[1]/img')
        data=[date, textImg.get_attribute('alt')]
        todayDatas.append(data)




print("-----------------------------------------------------")
print("Store id and content")
print("-----------------------------------------------------")
# store all content
time.sleep(5)
iter=0
for c in range(3):
    for r in range(9):
        print(f"Interation: {iter+1}")
        print("Click the post")
        click = driver.find_element(By.XPATH, f'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div/div/div/div[{r+1}]/div[{c+1}]/a/div[1]/div[2]')
        driver.execute_script("arguments[0].click();", click)
        time.sleep(5)
        print("Capture the id")
        # time.sleep(1000)
        try: 
            id= driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/div/li/div/div/div[2]/h2/div/span/div/a')
        except:
            try:
                id= driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/div/li/div/div/div[2]/h2/div/span/div/a')
            except:
                print("error")
                time.sleep(1000)
        todayDatas[iter].append(id.text)
        time.sleep(5)
        print("Capture the content")
        try:
            context=driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/div/li/div/div/div[2]/div[1]/h1')
        except:
            try:
                context=driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/div/li/div/div/div[2]/div[1]/h1')
            except:
                print("error")
                time.sleep(1000)
        todayDatas[iter].append(context.text)
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        time.sleep(10)
        iter+=1


#store in csv file
for row in todayDatas:
    wr.writerow(row)
    
f.close()
print("finish csv file")
time.sleep(5)

# github upload
sys.stderr.reconfigure(encoding='utf-8')

command = "git pull origin main"

result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

print("result:\n", result.stdout)
print("error:\n", result.stderr)

command = "git add crawlingdata.csv"

result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

print("result:\n", result.stdout)
print("error:\n", result.stderr)

command = f"git commit -m '{date}'"

result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

print("result:\n", result.stdout)
print("error:\n", result.stderr)

command = "git push origin main"

result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

print("result:\n", result.stdout)
print("error:\n", result.stderr)
