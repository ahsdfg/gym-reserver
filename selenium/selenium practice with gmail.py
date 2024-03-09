from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time

driver = webdriver.Safari()
url = 'https://google.com'
driver.get(url)
driver.maximize_window() # 창 크기 max로 엶
action = ActionChains(driver) # action 변수로 driver를 제어할 수 있도록 지정

driver.find_element(By.CLASS_NAME, 'gb_Md').click()

action.send_keys('ahsdfg30@gmail.com').perform()
# driver.find_element(By.CLASS_NAME, 'FliLIb DL0QTb').send_keys(Keys.ENTER)
driver.find_element(By.CSS_SELECTOR, '.FliLIb.DL0QTb').click()
