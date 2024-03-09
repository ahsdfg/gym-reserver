from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

import time

information = []

with open('information.txt', 'r') as info:
    for line in info.readlines():
        information.append(line)

info_new = []

for info in information:
    info_new.append(info.replace('\n', ''))

name = info_new[0]
mail_address = info_new[1]
card_no = info_new[2]
division = info_new[3]

date = '2023-{}-{}'.format(str(info_new[4]), str(info_new[5]))
date_selection = '{}_td_cls'.format(date)

time_dict = {'09:15~10:30':575231, '10:30~11:30':576324, '12:30~13:45':576320,\
             '13:30~14:45':576326, '13:45~14:45':378408, '14:45~16:00':576327,\
             '15:15~16:30':576322, '16:00~17:15':576328, '16:30~17:30':576323,\
             '17:15~18:15':576329, '18:45~19:45':576330, '19:45~21:00':576332}
time_code = time_dict[info_new[6]]

driver = webdriver.Safari()

def auto_reserve():
    url = 'https://select-type.com/rsv/?id=KatPteH9vEg'
    driver.get(url)
    driver.maximize_window()
    action = ActionChains(driver)

    dropdown = driver.find_element(By.NAME, 'c_id')
    select = Select(dropdown)
    select.select_by_value('196393')

    time.sleep(2)

    driver.find_element(By.ID, date_selection).click()

    time.sleep(2)

    elements = driver.find_elements(By.CSS_SELECTOR, '[class^="res-label label-type4"]')
    times = [element.get_attribute("class") for element in elements]
    print(times)
    for t in times:
        print(t)
        if str(time_code) in t:
            rtime = t
            break
    driver.find_element(By.CLASS_NAME, rtime.replace(' ', '.')).click()

    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, '[type="button"]').click()

    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, '[name="name"]').click()
    (
    action.send_keys(name).key_down(Keys.TAB).key_up(Keys.TAB)
    .send_keys(mail_address).key_down(Keys.TAB).key_up(Keys.TAB)
    .send_keys(mail_address).key_down(Keys.TAB).key_up(Keys.TAB)
    .send_keys(card_no).key_down(Keys.TAB).key_up(Keys.TAB)
    .send_keys(division).key_down(Keys.TAB).send_keys(division)
    .perform()
    )
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    time.sleep(1)

    driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    time.sleep(2)

    driver.find_element(By.CLASS_NAME, 'btn.btn-primary.btn-xlarge.btn3_label.chg-btn2.g-recaptcha').click()

    time.sleep(4)

auto_reserve()
