#-*-coding=UTF-8 -*-
'''
Created on 2017年4月18日
委案流转模块
@author: HP
'''

from random import randint
import random
from time import sleep
import unittest

import  sys
sys.path.append(r'E:/Users/HP/PycharmProjects/ZiChan100/src')

from public import login
from public.autowebdriver import AutoWebdriver


class WeiAnLiuZhuan(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=AutoWebdriver()
        cls.driver.maximizeWindow()
        cls.driver.implicitWait(10)
        cls.driver.navigate(r'http://101.201.41.60:40080/platform/web/sys/login')
    def test_login(self):   
        try:
            login.login2(self,"lixingyu","123456")
            # username=input('请输入用户名：')
            # password=input('请输入密码：')
            # login.login2(self, username, password)

        except Exception: 
            print('登录失败')

    def test_weianliuhzhuan(self):
        '''进入委案管理页面'''
        self.caidanlists=self.driver.getElenments('css_selector,div[class="el-submenu__title"]')
        print("进入委案管理页面")
        print('div元素个数为'+str(len(self.caidanlists)))
        for i in range(0,len(self.caidanlists)):
            if self.caidanlists[i].text == '委案管理':
                self.caidanlists[i].click()
                break
        sleep(1)
        
        '''进入委案流转管理页面'''
        self.weianliuzhuan=self.driver.getElenments('css_selector,li[class="el-submenu is-opened"]>ul>li')
        #print('委案管理li元素个数为'+str(len(self.weianliuzhuan)))
        for i in range(0, len(self.weianliuzhuan)):
            if self.weianliuzhuan[i].text == '委案流转管理':
                self.weianliuzhuan[i].click()
                break
        sleep(1)

    def test_weianshenhe(self):
        '''获取标签页'''
        self.weian_biaoqian=self.driver.getElenments('css_selector,div[class="el-tabs__nav"]>div')
        print(len(self.weian_biaoqian))

        '''点击委案审核页面'''
        for i in range(0,len(self.weian_biaoqian)):
            if self.weian_biaoqian[i].text=='委案审核':
                self.weian_biaoqian[i].click()
                print(self.weian_biaoqian[i].text)
                break

        self.shenhezhuangtai=self.driver.getElenments('css_selector,div[class="el-radio-group"]>label>span')
        '''点击待审核状态'''
        for i in range(0,len(self.shenhezhuangtai)):
            if self.shenhezhuangtai[i].text=='待审核':
                self.shenhezhuangtai[i].click()
                print(self.shenhezhuangtai[i].text)
                break
        sleep(1)
        
        '''点击查询按钮'''
        def chaxun():
            '''点击查询按钮'''
            self.anniu_chaxun=self.driver.getElenments('css_selector,button[class="el-button el-button--success el-button--mini"]')
            self.driver.action_click1(self.anniu_chaxun,0)


    def test_weianfenpei(self):
        def chaxun(): 
            '''点击查询按钮'''
            self.anniu_chaxun=self.driver.getElenments('css_selector,button[class="el-button el-button--success el-button--mini"]')
            self.driver.action_click1(self.anniu_chaxun,0)
            
        '''获取标签页'''
        self.weian_biaoqian=self.driver.getElenments('css_selector,div[class="el-tabs__nav"]>div')
        
        '''点击委案分配页面'''
        self.driver.action_click1(self.weian_biaoqian,1)
        sleep(1)
        chaxun()
        sleep(1)
         
        '''获取委案状态'''
        self.weianzhuangtai=self.driver.getElenments('css_selector,span[class="el-radio-button__inner"]')
        '''点击待分配'''
        self.weianzhuangtai[1].click()
        chaxun()
        
        '''获取逾期时间'''
        self.yuqishijian=self.driver.getElenments('css_selector,div[class="el-checkbox-group"]>label')
        print(len(self.yuqishijian))
        
        for n in range(3):
            k=randint(1,15)
            print(k)
            M_list=["M0","M1","M2","M3","M4","M5","M6","M7","M8","M9","M10","M11","M12","M13-M24","M24+"]
            v_list=random.sample(M_list,k)
    
            i=0
            for Mvalue in self.yuqishijian:
                for v in v_list:
                    if Mvalue.text==v:
                        self.yuqishijian[i].find_element_by_css_selector('span[class="el-checkbox__inner"]').click()        
                print(Mvalue.text+"index"+str(i))
                i=i+1
                chaxun()
     

if __name__=='__main__':
    suite=unittest.TestSuite()
    suite.addTest(WeiAnLiuZhuan('test_login'))
    suite.addTest(WeiAnLiuZhuan('test_weianliuhzhuan'))
    suite.addTest(WeiAnLiuZhuan('test_weianshenhe'))
    suite.addTest(WeiAnLiuZhuan('test_weianfenpei'))
    
    runner=unittest.TextTestRunner()
    runner.run(suite)
    
