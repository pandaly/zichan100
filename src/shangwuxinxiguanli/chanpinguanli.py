#-*-coding=UTF-8 -*-
'''
Created on 2017年4月6日

@author: HP
'''
import time
from datetime import date
from random import random, choice
from test.test_tools.test_unparse import try_except_finally
from time import sleep
import unittest

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from public import login


class ChanPinGuanLi(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()
        cls.driver.get('http://101.201.41.60:60/platform/web/site/index')
        print("111")
      
    def test_denglu(self):
        '''登录主界面'''
        login.login(self,"lixingyu","123456")
        self.seach_dengluxinxi=WebDriverWait(self.driver,5,1).until\
        (expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,"div.demo-block")),message='时间超时').text
        print(self.seach_dengluxinxi)
       
    def test_shangwuxinxi(self):
        '''进入商务信息管理页面
        #页面通过CSS选择器难以定位，所以获取所有DIV标签，先通过输出的文本判断是全部获得了div元素，再加个参数n，获取系统管理所在的div标签索引，得到一个div元素''' 
#        self.driver = self.driver
        self.shangwuguanli=self.driver.find_elements_by_css_selector('div[class="el-submenu__title"]')
        print("进入商务信息管理页面")
        print('div元素个数为'+str(len(self.shangwuguanli)))
        i=0
        for itema in self.shangwuguanli:
            print(itema.text+'index'+str(i))
            i=i+1
        ActionChains(self.driver).click(self.shangwuguanli[2]).perform()
        #print(self.shangwuguanli[2].get_attribute('innerHTML'))
        print(self.shangwuguanli[2].get_attribute('outerHTML'))
        
    def test_ChanPinguanli(self):
        '''进入产品管理页面'''
        self.ChanPinguanli=self.driver.find_elements_by_css_selector('li[class="el-submenu is-opened"]>ul>li') 
        print('商务信息li元素个数为'+str(len(self.ChanPinguanli)))
        a=0
        for itemc in self.ChanPinguanli:
            print(itemc.text+'index'+str(a))
            a=a+1
        ActionChains(self.driver).click(self.ChanPinguanli[2]).perform()   
    def test_chaxun_weiangongsi(self):
        '''根据委案公司查询'''
        self.weiangongsi=self.driver.find_element_by_css_selector('input[placeholder="请选择"]')
        ActionChains(self.driver).click(self.weiangongsi).perform()
        self.weiangongsi.clear()
#        self.weiangongsi.send_keys(Keys.TAB)
        self.weiangongsi.send_keys('阿里')
        sleep(1)
        
        '''查看委案公司列表内容'''
#         items=self.driver.find_elements_by_css_selector('li[class="el-select-dropdown__item"]')
#         n=0
#         for item in items:
#             print(item.text+"index"+str(n))
        self.yemian=self.driver.find_elements_by_css_selector('ul[class="el-scrollbar__view el-select-dropdown__list"]')[0]
        items=self.yemian.find_elements_by_css_selector('ul[class="el-scrollbar__view el-select-dropdown__list"]>li')
        print('公司列表元素个数为'+str(len(items)))
       
        '''根据输入的信息，选中委案公司'''
        n=0
        for item in items:
            if "阿里" in item.text:
                print(item.text+"index"+str(n))
                self.driver.find_element_by_css_selector('ul[class="el-scrollbar__view el-select-dropdown__list"]>li:nth-child('+str(n-1)+')').click()
                #item=self.driver.find_element_by_xpath('//*[@id="layout"]/div[2]/div/div[1]/ul/li['+str(n)+']')
#                 sleep(2)  item=
#                 ActionChains(self.driver).click(item).perform()   
                break
                print("跳出")
            print(str(n))    
            n=n+1 
        '''定位查询按钮'''        
        self.chasunbutton=self.driver.find_elements_by_css_selector('button[class="el-button el-button--success el-button--mini"]')[0]
      
        '''点击查询按钮'''
        self.chasunbutton.click()
#        lis=self.driver.find_elements_by_css_selector('div[class="el-select-dropdown__wrap el-scrollbar__wrap"]>ul>li')
        sleep(2)
        items=self.driver.find_elements_by_css_selector('label[class="el-checkbox"]')
        n=0
        for item in items:
            print(item.text+"index"+str(n))
            n=n+1
#            item.click()
        '''定位产品类型复选框和产品状态复选框'''
        divs=self.driver.find_elements_by_css_selector('div[class="el-checkbox-group"]')
        print(len(divs))
        print(divs[0].text)
        '''定位产品类型复选框'''
        inputs=divs[0].find_elements_by_css_selector('span[class="el-checkbox__inner"]')
#        inputs=self.driver.find_elements_by_css_selector('span[class="el-checkbox__inner"]')
        print(len(inputs))
        '''获取列表的第4列，委案公司名'''
        column4s=self.driver.find_elements_by_css_selector('td[class="el-table_1_column_4"]')
        print(len(column4s))
        '''判断委案公司是否是查询的公司'''
        gongsi_tu=1
        for column4 in column4s:
            try:
                '''添加断言'''
                self.assertEqual("阿里巴巴", column4.text, "委案公司查询出错")
            except:
                '''截图保存'''
                self.driver.get_screenshot_as_file(r'e:/gongsi'+str(gongsi_tu)+r'.png')
                gongsi_tu=gongsi_tu+1
        '''点击融资租赁对结果进一步查询'''
        inputs[0].click()
        self.chasunbutton.click()
        sleep(2)
        '''获取列表的第5列，产品名'''
        column5s=self.driver.find_elements_by_css_selector('td[class="el-table_1_column_5"]')
        print(len(column5s))
        '''判断产品名是否是融资租赁'''
        chanpin_tu=1
        for column5 in column5s:
            try:
                '''添加断言'''
                self.assertEqual("融资租赁", column5.text, "产品查询出错")
            except:
                '''截图保存'''
                self.driver.get_screenshot_as_file(r'e:/chanpin'+str(chanpin_tu)+r'.png')
                chanpin_tu=chanpin_tu+1
         
    def test_chaxun_chanpinleixing(self):
        '''页面的刷新操作'''
        self.driver.refresh();
        sleep(2)
        '''查找页面所有复选框'''
        items=self.driver.find_elements_by_css_selector('label[class="el-checkbox"]')
        n=0
        for item in items:
            print(item.text+"index"+str(n))
            n=n+1
#            item.click()
        '''定位产品类型复选框和产品状态复选框'''
        divs=self.driver.find_elements_by_css_selector('div[class="el-checkbox-group"]')
        print(len(divs))
        print(divs[0].text)
        '''定位产品类型复选框'''
        inputs=divs[0].find_elements_by_css_selector('span[class="el-checkbox__inner"]')
#        inputs=self.driver.find_elements_by_css_selector('span[class="el-checkbox__inner"]')
 
        print(len(inputs))
#         k=0
        '''选中所有产品类型复选框'''
        for inpu in inputs:
#             print(inpu.text+"index"+str(k))
#             k=k+1
            inpu.click()
#            inpu.send_keys(Keys.SPACE)
        '''取消选中'''
        inputs[5].click()
    
    def test_xinzeng(self):
        '''定位新增按钮'''        
        self.xinzengbutton=self.driver.find_elements_by_css_selector('button[class="el-button el-button--primary el-button--mini"]')[0]
        '''点击新增按钮'''
        self.xinzengbutton.click()
        '''定位新增页面的div元素,方便页面其他元素的定位'''
        self.xinzeng_divs=self.driver.find_elements_by_css_selector('div[class="el-col el-col-24"]')
        for a in self.xinzeng_divs:
            print(a.get_attribute('innerHTML'))
        '''定位产品名称并输入信息'''
        self.xinzeng_chanpinming=self.xinzeng_divs[0].find_element_by_css_selector('input[placeholder="请输入产品名称"]')
        self.xinzeng_chanpinming.click()
        self.xinzeng_chanpinming.clear()
        self.xinzeng_chanpinming.send_keys('testa8')
        
        '''定位委案公司'''
        self.xinzeng_gongsiming=self.xinzeng_divs[1].find_element_by_css_selector('input[placeholder="请选择"]')
        self.xinzeng_gongsiming.click()
        '''定位委案公司列表'''
        self.xinzeng_gongsilists=self.driver.find_elements_by_css_selector('ul[class="el-scrollbar__view el-select-dropdown__list"]')
        print('ul列表元素个数为'+str(len(self.xinzeng_gongsilists)))
       
        '''根据输入的信息，选中委案公司'''
        items=self.xinzeng_gongsilists[3].find_elements_by_css_selector('li')
        n=0
        for item in items:
            if "BBB" in item.text:
                print(item.text+"index"+str(n))
                item.click()
                break
                print("跳出")
            print(str(n))    
            n=n+1 
        '''定位新增产品类型'''
        #self.xinzeng_leixing=self.xinzeng_divs[2].find_element_by_css_selector('input[placeholder="请选择"]')
        sleep(1)
        self.xinzeng_leixing=self.xinzeng_divs[2].find_element_by_css_selector('div[class="el-input el-input--mini"]')
        self.xinzeng_leixing.click()
        sleep(1)
        '''定位产品类型列表'''
        self.xinzeng_leixinglists=self.driver.find_elements_by_css_selector('ul[class="el-scrollbar__view el-select-dropdown__list"]')
    
        lilists=self.xinzeng_leixinglists[3].find_elements_by_css_selector('li')
        print('产品类型列表元素个数为'+str(len(lilists)))
        '''随机选择产品类型并点击'''
        random=choice(["融资租赁","企业经营贷款","个人房产","消费贷","汽车金融","供应链贷款"])
        k=0
        for li in lilists: 
            print(li.text+"index"+str(k))
            if random in li.text:
                li.click()
            k=k+1
        '''定位确定按钮'''
        self.quedingbutton=self.driver.find_elements_by_css_selector('button[class="el-button el-button--primary el-button--mini"]')[4]
        self.quedingbutton.click()
#         '''定位取消按钮'''
#         self.quxiaobutton=self.driver.find_element_by_css_selector('button[class="el-button el-button--default el-button--mini"')
#         self.quxiaobutton.click()

        sleep(0.5)  
        self.alert=self.driver.find_element_by_css_selector('div[class="el-notification__content"]')
        print(self.alert.text)
        
        '''添加断言判断是否成功'''
        try:
            self.assertEqual("保存成功", self.alert.text, "断言出现问题，元素定位失败或时间超时")
            shijian=time.ctime(time.time())
            
            '''失败时截图保存'''
        except:
            self.driver.get_screenshot_as_file(r'e:\chanpintianjiashibai'+str(shijian))
        print(r'e:\chanpintianjiashibai'+str(shijian))
# if __name__=='__main__':
#     #unittest.main()
#     
#     suite=unittest.TestSuite()
#     suite.addTest(ChanPinGuanLi('test_denglu'))
#     suite.addTest(ChanPinGuanLi('test_shangwuxinxi'))
#     suite.addTest(ChanPinGuanLi('test_ChanPinguanli'))
#     #suite.addTest(ChanPinGuanLi('test_chaxun_weiangongsi'))
#     #suite.addTest(ChanPinGuanLi('test_chaxun_chanpinleixing'))
#     suite.addTest(ChanPinGuanLi('test_xinzeng'))
#     runner=unittest.TextTestRunner()
#     runner.run(suite)

