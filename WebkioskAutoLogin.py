import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import os

enrollmentNumber = ""
dateOfBirth = ''
passWord = os.environ.get('WEBKIOSK LOGIN PASSWORD')

WINDOW_SIZE = "1920,1080"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
# chrome_options.binary_location = PATH

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH, chrome_options=chrome_options)

driver.get("https://webkiosk.jiit.ac.in/")
print(driver.title)
time.sleep(3)

enrollment = driver.find_element_by_id("MemberCode")
enrollment.send_keys(enrollmentNumber)

dob = driver.find_element_by_id('DATE1')
dob.send_keys(dateOfBirth)

password = driver.find_element_by_id('Password101117')
password.send_keys(passWord)

captcha = driver.find_element_by_xpath(
    '/html/body/form/table/tbody/tr[3]/td[1]/table/tbody/tr/td[2]/table/tbody/tr[1]/td/div/s/i/font')

# print("HI my name is: ", captcha.text)
enterCaptcha = driver.find_element_by_id('txtcap')
enterCaptcha.send_keys(captcha.text)

link = driver.find_element_by_id('BTNSubmit')
link.click()
time.sleep(3
           )
# attendanceFirst = driver.find_element_by_xpath(
#     '/html/body/table/tbody/tr[3]/td/div/div[4]')
# attendanceFirst = driver.find_element_by_link_text('Academic Info.')
# attendanceFirst.click()

# time.sleep(1)
# attendance = driver.find_elements_by_link_text('My Attendance')
# attendance.click()
driver.get(
    'https://webkiosk.jiit.ac.in/StudentFiles/Academic/StudentAttendanceList.jsp')

time.sleep(2)
for i in range(1, 11):
    if i == 3 or i == 4 or i == 9:
        continue
    sno = driver.find_element_by_xpath(
        "/html/body/table[2]/tbody/tr["+str(i)+"]/td[1]")
    subject = driver.find_element_by_xpath(
        "/html/body/table[2]/tbody/tr["+str(i)+"]/td[2]")
    try:
        att = driver.find_element_by_xpath(
            '/html/body/table[2]/tbody/tr['+str(i)+']/td[3]/a')
        print(sno.text, " ", subject.text, " ", att.text)
    except:
        att = " "
        print(sno.text, " ", subject.text, " ", att)
# driver.quit()

# search = driver.find_element_by_name("s")
# search.send_keys("test")
# search.send_keys(Keys.RETURN)

# try:
#     main = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "main"))
#     )
#     print(main.text)
# except:
#     driver.quit()

# main = driver.find_element_by_id("main")

# time.sleep(5)

# /html/body/table[2]/tbody/tr[1]/td[3]/a
