from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pass_gen import *


def login(user):
    old_pass = return_latest_pass()[1]
    username = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.NAME  ,
                                        "username")))
    username.send_keys(user)

    password = driver.find_element_by_name("password")
    password.send_keys(old_pass)    

    try:
        login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        login.click()
    except:
        driver.quit()
        print("login unsuccessful")

def popups():
    try:
        info = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH  ,
                                            '//*[@id="react-root"]/section/main/div/div/div/div/button')))
        info.click()
    except:
        pass

    try:
        notif = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH  ,
                                            '/html/body/div[4]/div/div/div/div[3]/button[1]')))
        notif.click()
    except:
        pass

def navigate():
    profile = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH  ,
                                            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img')))
    profile.click()


    settings = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH  ,
                                            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[3]')))

    settings.click()

    change_pass = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.LINK_TEXT  ,
                                            'Change Password')))

    change_pass.click()

def enter():
    old_box = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.NAME  ,
                                            'cppOldPassword')))

    new_box1 = driver.find_element_by_name("cppNewPassword")
    new_box2 = driver.find_element_by_name("cppConfirmPassword")

    old_pass = return_latest_pass()[1]
    new_pass = generate()

    add_entry(new_pass)

    old_box.send_keys(old_pass)
    new_box1.send_keys(new_pass)
    new_box2.send_keys(new_pass)

    confirm = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/form/div[4]/div/div/button')

    confirm.click()
    time.sleep(10)
    
    if old_box.get_attribute("value") == "":
        print("Password changed successfully")
    else:
        print("Password change failed")


    

PATH = 'C:\Program Files (x86)\chromedriver.exe'

driver = webdriver.Chrome(PATH)

driver.get("https://www.instagram.com/")
login('flamerten')
popups()
navigate()
enter()
#driver.quit()





