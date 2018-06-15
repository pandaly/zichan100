# -*- coding: utf-8 -*-
'''
Created on 2017年3月20日

@author: HP
'''


from selenium.webdriver.common.action_chains import ActionChains
 
# #     def test_yonghu(self):
#         print('进入首页用户名修改密码')
#         self.yonghu=self.driver.find_element_by_css_selector('div[class="el-dropdown"]')
#         self.yonghu.click()
# #        ActionChains(self.driver).click(self.yonghu).perform()
#         self.contracts=self.driver.find_elements_by_css_selector('ul[class="el-dropdown-menu"]>li:first-child')
#         print(len(self.contracts))
# #        ActionChains(self.driver).click(self.contracts[0]).perform()
# #        self.contracts[0].click()
#         print(self.contracts[0].text)
#         print('----------运行结束-----------')
def login2(self,username,password):
    driver = self.driver
    driver.getElenment('css_selector,input[type="text"]').clear()
    driver.getElenment('css_selector,input[type="text"]').send_keys(username)
    driver.getElenment('css_selector,input[type="password"]').clear()
    driver.getElenment('css_selector,input[type="password"]').send_keys(password)
    driver.getElenment('css_selector,div.el-form-item__content>button').click()
  




def login(self,username,password):
    driver = self.driver
    driver.find_element_by_css_selector('input[type="text"]').clear()
    driver.find_element_by_css_selector('input[type="text"]').send_keys(username)
    driver.find_element_by_css_selector('input[type="password"]').clear()
    driver.find_element_by_css_selector('input[type="password"]').send_keys(password)
    driver.find_element_by_css_selector('div.el-form-item__content>button').click()    

def login1(self,username,password):
    driver = self.driver
    driver.find_element_by_id('account').clear()
    driver.find_element_by_id('account').send_keys(username)
    driver.find_element_by_id('password').clear()
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_css_selector('button[class="ant-btn ant-btn-primary"]').click()
def login_cuishoufang(self,username,password):
    print("登录开始")
    driver = self.driver
    print("登录开始11111111")
    driver.find_element_by_css_selector('div[class ="el-input"] > input[type="text"]').clear()
    print("登录开始222221")
    driver.find_element_by_css_selector('div[class ="el-input"] > input[type="text"]').send_keys(username)
    driver.find_element_by_css_selector('div[class ="el-input"] > input[type="password"]').clear()
    driver.find_element_by_css_selector('div[class ="el-input"] > input[type="password"]').send_keys(password)
    driver.find_element_by_css_selector('button[type="button"]').click()
    print("登录结束")
#因为在cuishouxitong.py文件中导入autowebdriver类，所有定位元素时，要用autowebdriver类的方法，不能直接用driver.find_element_by_css_selector(...)会报错
def login_cuishoufang1(self,username,password):
    driver = self.driver
    print("登录开始")
    driver.getElenment('css_selector,div[class ="el-input"] > input[type="text"]').clear()
    driver.getElenment('css_selector,div[class ="el-input"] > input[type="text"]').send_keys(username)
    driver.getElenment('css_selector,div[class ="el-input"] > input[type="password"]').clear()
    driver.getElenment('css_selector,div[class ="el-input"] > input[type="password"]').send_keys(password)
    driver.getElenment('css_selector,button[type="button"]').click()
    print("登录结束")


