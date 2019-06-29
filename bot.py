from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
import os
import time
import sys

class InstagramBot:

    def __init__(self, username, password):
        
        self.username = username
        self.password = password
        self.base_url = 'https://www.instagram.com'
        self.driver = webdriver.Chrome('chromedriver.exe')

      

        self.login()
        
        
    def login(self):    
        self.driver.get('{}/accounts/login/'.format(self.base_url))
        time.sleep(1)
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        time.sleep(1)
        self.driver.find_elements_by_xpath("//div[contains(text(), 'Log In')]")[0].click()
        time.sleep(3)
        ui.WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".aOOlW.HoLwm"))).click()
       
        #https://www.instagram.com/tonyrobbins/
        time.sleep(15)

    def nav_user(self, user):
        self.driver.get('{}/{}/'.format(self.base_url, user))

    


if __name__ == '__main__':
    ig_bot = InstagramBot('kelsiketo@gmail.com','u00m840@#')
    ig_bot.nav_user('tonyrobbins')
    time.sleep(30)
    