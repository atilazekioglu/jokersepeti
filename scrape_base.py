from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys


browser = webdriver.Firefox(executable_path='/Users/atilazekioglu/Documents/Webdriver/geckodriver')
browser.implicitly_wait(10) # seconds
browser.get('https://yemeksepeti.com/istanbul')
print("Browser Type:" + str(type(browser)))

username = "your_username"
password = "your_password"


usernamefield=browser.find_element_by_id("UserName")
passwordfield=browser.find_element_by_id("password")
giriselem = browser.find_element_by_class_name('ys-btn-lg')

def login():
    usernamefield.send_keys(username)
    passwordfield.send_keys(password)
    giriselem.click()
    return print("Login Credentials Submitted!")





def logincheck():
    if browser.find_elements_by_id("ysUserName"):
        print("Login Successful.")
    elif browser.find_elements_by_class_name("confirmation-dialog"):
        dialog = browser.find_element_by_class_name("ys-xl.inner")
        print(dialog.text)
        sys.exit()
    else:
        print("Something went wrong in the code.")
        sys.exit()

   
       

login()
logincheck()

#Home Page

userinfo = browser.find_element_by_class_name("ys-user-info-container.withPoint")

print(userinfo.text)




