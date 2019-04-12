#  -*- coding:utf-8 -*-
from selenium import webdriver
import unittest
from login_manage import login_by_logindo


class LoginTest():
    def setUp(self):
        self.dr = webdriver.Firefox()
        self.user_name = 'count11'
        self.user_password = '2017nltk'


    def test_login(self):
      login_by_logindo(self.dr,self.user_name,self.user_password)

if __name__ == "__main__":
    unittest.main()
    #test_case1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    #suite = unittest.TestSuite(test_case1)
    #unittest.TextTestRunner(verbosity=2).run(suite)
