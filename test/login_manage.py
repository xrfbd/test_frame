#  -*- coding:utf-8 -*-
import time
from pageObject.login_page import  LoginPage
def login_by_logindo(driver,user_name, user_psw):
    loginpage = LoginPage(driver)
    loginpage.open_logindo()
    #loginpage.save_screenshot()
    loginpage.click_accounts()
    loginpage.input_username(user_name)
    loginpage.input_pwd(user_psw)
    loginpage.click_login_btn()
    #loginpage.save_screenshot()
    time.sleep(2)