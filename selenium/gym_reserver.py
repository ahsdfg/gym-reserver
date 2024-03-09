from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from tkinter import *
import tkinter.ttk as ttk
import os
import datetime
import time



def auto_reserve():

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
    for t in times:
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

file_path = 'information.txt'
information = []

if os.path.exists(file_path):
    with open('information.txt', 'r') as info:
        for line in info.readlines():
            information.append(line)

times_sat = ['12:30~13:45', '13:45~14:45', '15:15~16:30', \
             '16:30~17:30']

times = ['09:15~10:30', '10:30~11:30', '13:30~14:45', '14:45~16:00', \
         '16:00~17:15', '17:15~18:15', '18:45~19:45', '19:45~21:00']

def save():
    with open('information.txt', 'w') as info:
        info.write(name.get() + '\n')
        info.write(email.get() + '\n')
        info.write(card_no.get() + '\n')
        info.write(division.get() + '\n')
        info.write(mc.get() + '\n')
        info.write(dc.get() + '\n')
        info.write(tc.get())

# 일요일에는 짐이 안 열어서 따로 설정
def sunday_popup():
        popup = Toplevel(root)
        popup.title("Sunday")
        msg = Label(popup, text="You have selected Sunday")
        msg.pack()
        popup.geometry("300x200")

def set_date():
    date = datetime.date(2023, int(mc.get()), int(dc.get()))
    day = date.weekday()
    if day == 6:
        tc['values'] = []
        pass # sunday_popup
    elif day == 5:
        tc["values"] = times_sat
    else:
        tc["values"] = times

info_new = []

for info in information:
    info_new.append(info.replace('\n', ''))

root = Tk()
root.title = ("Gym Reservation")
root.geometry("640x240+400+300")
root.resizable(False, False)

nl = Label(root, text = "name")
nl.grid(row = 0, column = 0, sticky = N+E+S, padx = 3, pady = 3)

name = Entry(root, width = 20)
name.grid(row = 0, column = 1)
if len(information) >= 1:
    name.insert(0, info_new[0])

el = Label(root, text = "email address")
el.grid(row = 1, column = 0, sticky = N+E+S, padx = 3, pady = 3)

email = Entry(root, width = 20)
email.grid(row = 1, column = 1)
if len(information) >= 1:
    email.insert(0, info_new[1])

cl = Label(root, text = "card number")
cl.grid(row = 2, column = 0, sticky = N+E+S, padx = 3, pady = 3)

card_no = Entry(root, width = 20)
card_no.grid(row = 2, column = 1)
if len(information) >= 1:
    card_no.insert(0, info_new[2])

cl = Label(root, text = "division")
cl.grid(row = 3, column = 0, sticky = N+E+S, padx = 3, pady = 3)

division = Entry(root, width = 20)
division.grid(row = 3, column = 1)
if len(information) >= 1:
    division.insert(0, info_new[3])

dl = Label(root, text = "date")
dl.grid(row = 4, column = 0, sticky = N+E+S, padx = 3, pady = 3)

months = [str(i) for i in range(1, 13)]
mc = ttk.Combobox(root, height = 5, values = months, state = "readonly")
mc.grid(row = 4, column = 1)
if len(information) >= 1:
    mc.set(info_new[4])

days = [str(i) for i in range(1, 32)]
dc = ttk.Combobox(root, height = 10, values = days, state = "readonly")
dc.grid(row = 4, column = 2)
if len(information) >= 1:
    dc.set(info_new[5])

s_date = Button(root, text = "set the date", command = set_date)
s_date.grid(row = 4, column = 3)

tl = Label(root, text = "time")
tl.grid(row = 5, column = 0, sticky = N+E+S, padx = 3, pady = 3)

tc = ttk.Combobox(root, height = 10, values = times, state = "readonly")
tc.grid(row = 5, column = 1)
# 전에 했던 타임이 저절로 들어가게 설정해보기
# if len(information) >= 1:
#     dc.set(info_new[6])

save_btn = Button(root, text = "save", command = save)
save_btn.grid(row = 5, column = 2)

reserve_btn = Button(root, text = "reserve", command = auto_reserve)
reserve_btn.grid(row = 6, column = 2)

root.mainloop()