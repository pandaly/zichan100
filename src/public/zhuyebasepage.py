# -*- coding: utf-8 -*-
'''
Created on 2017年4月14日

@author: HP
'''

class zhuyeBasePage():
    def __init__(self,driver,baseurl):
        '''主页面'''
        self.driver=driver
        self.baseurl=baseurl
        
    def openPgae(self,url):
        self.driver.navigate(self.baseurl+url)
        
    ''' 
    def login(self,username,password):
        self.loginurl='/sys/login'
        self.openPgae(self.loginurl)
        self.driver.type('css_selector,input[type="text"]',username)
        self.driver.type('css_selector,input[type="password"]',password)
        self.driver.click('css_selector,div.el-form-item__content>button')
    '''
    def denglu(self):
        '''登录主界面'''
        self.zhuye=zhuyeBasePage(self.driver,'http://101.201.41.60:60/platform/web')
        self.zhuye.login("lixingyu","123456")
        