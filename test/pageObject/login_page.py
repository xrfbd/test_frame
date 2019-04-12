#  -*- coding:utf-8 -*-
import time

class LoginPage():
    def __init__(self, driver):
        self.base_url = 'http://www.ablesky.com/'
        self.dr = driver

    def open_logindo(self):
        url = "%slogin.do" % (self.base_url)
        self.dr.get(url)

    def click_accounts(self):
        time.sleep(1)
        self.dr.find_element_by_class_name('login-switch').click()

    def input_username(self, user_name):
        time.sleep(1)
        self.dr.find_element('id', 'J_loginUsername').send_keys(user_name)

    def input_pwd(self, user_psw):
        self.dr.find_element('id', 'login_password').send_keys(user_psw)

    def click_login_btn(self):
        self.dr.find_element('css selector', 'span.greenbtn35_text.text').click()