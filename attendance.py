#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass
from email_att import sendEmail

if __name__ == '__main__':
    # default values can be set
    user_input = input("Enter register number: ")
    pass_input = getpass.getpass("Eduserve password: ")

    PATH = "C:\Program Files (x86)\chromedriver.exe"

    driver = webdriver.Chrome(PATH)

    driver.get("https://eduserve.karunya.edu/")

    print(f"Retrieving {driver.title}")

    user = driver.find_element_by_id("mainContent_Login1_UserName")
    user.send_keys(user_input)

    password = driver.find_element_by_id("mainContent_Login1_Password")
    password.send_keys(pass_input, Keys.RETURN)

    name = driver.find_element_by_id("mainContent_LBLNAME")
    print(f"Attendance details of {name.text}")

    class_attend = driver.find_element_by_id("mainContent_LBLCLASS")
    print(f"Class Attendance % : {class_attend.text}")

    assembly_attend = driver.find_element_by_id("mainContent_LBLASSEMBLY")
    print(f"Assembly Attendance % : {assembly_attend.text}")

    SENDER_EMAIL = "yourmail@xyz.com"
    PASSWORD = getpass.getpass("Email password: ")
    TO = "yourmail@karunya.edu.in"
    SUBJECT = f"Attendance Details of {name.text}"
    MESSAGE = f'''
    Attendance details of {name.text}:
    Class Attendance % : {class_attend.text}
    Assembly Attendance % : {assembly_attend.text}
    '''

    sendEmail(SENDER_EMAIL, PASSWORD, TO, SUBJECT, MESSAGE)

    driver.close()
    