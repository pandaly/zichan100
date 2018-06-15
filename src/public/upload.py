#-*-coding=UTF-8 -*-
'''
Created on 2017年4月12日

@author: HP
'''
import os
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


def upload(self,file_name):  
    '''定位选择文件按钮'''
    self.driver.find_element_by_id('picker').click()  
    '''需要将upload.exe的绝对路径，添加到环境变量path中，为了方便直接将upload.exe复制到D:\Python36-32下，D:\Python36-32在PATH中'''
    os.system(r'upload.exe  '+file_name)  #注意单引号中间不要再加双引号，空格区分即可，否则会报错 
    sleep(2)
    self.driver.find_element_by_css_selector('button[class="el-button el-button--success el-button--small"]').click()
    message=self.driver.find_element_by_css_selector('div[class="el-message-box__message"]').text
    print(message)
    if "成功上传" in message:      #self.assertTrue("成功上传" in message, "断言出现问题 "):
        print('上传成功')
    else:
        print('上传失败')
    sleep(0.5)
    self.driver.find_element_by_css_selector('button[class="el-button el-button--default el-button--primary "]').click()
    
    
def gongsichanpin(self,gongsi,chanpin):    
    '''选择委案公司'''
    self.weiangongsi=self.driver.find_element_by_css_selector('input[placeholder="请选择委案公司"]')
    ActionChains(self.driver).click(self.weiangongsi).perform()
    self.weiangongsi.clear()
#        self.weiangongsi.send_keys(Keys.TAB)
    self.weiangongsi.send_keys(gongsi)
    sleep(1)
    
    '''查看委案公司列表内容'''
    self.yemian=self.driver.find_elements_by_css_selector('ul[class="el-scrollbar__view el-select-dropdown__list"]')[1]
    items=self.yemian.find_elements_by_css_selector('ul[class="el-scrollbar__view el-select-dropdown__list"]>li')
    print('公司列表元素个数为'+str(len(items)))
   
    '''根据输入的信息，选中委案公司'''
    n=0
    for item in items:
        if gongsi in item.text:
            print(item.text+"index"+str(n))
            self.driver.find_element_by_css_selector('ul[class="el-scrollbar__view el-select-dropdown__list"]>li:nth-child('+str(n+2)+')').click()
            break
            print("跳出")
        print(str(n))    
        n=n+1 
        
    '''定位产品文本框，选择产品'''
    self.chanpinming=self.driver.find_element_by_css_selector('input[placeholder="请选择产品名"]')
    ActionChains(self.driver).click(self.chanpinming).perform()
    
    '''目前产品名文本框，不可编辑，不能发送文本'''
#         self.chanpinming.clear()
#         self.chanpinming.send_keys('test')
    sleep(1)   
    
    '''查看产品列表内容'''
    self.chanpinmingl=self.driver.find_elements_by_css_selector('ul[class="el-scrollbar__view el-select-dropdown__list"]')[1]
    chanpin_items=self.chanpinmingl.find_elements_by_css_selector('ul[class="el-scrollbar__view el-select-dropdown__list"]>li')
    print('产品列表元素个数为'+str(len(items)))
   
    '''根据输入的信息，选中产品'''
    n=0
    for chanpin1 in chanpin_items:
        if chanpin in chanpin1.text:
            print(chanpin1.text+"index"+str(n))
            
            '''此处查询到两个元素，选取第二个'''
            self.driver.find_elements_by_css_selector('ul[class="el-scrollbar__view el-select-dropdown__list"]>li:nth-child('+str(n+2)+')')[1].click()
            break
            print("跳出")
        print(str(n))    
        n=n+1    