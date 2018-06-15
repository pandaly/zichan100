from random import randint
import random
from time import sleep
import unittest
import csv

import  sys
sys.path.append(r'E:/Users/HP/PycharmProjects/ZiChan100/src')

import login
from  autowebdriver import AutoWebdriver


class ZhangHuGuanLi(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=AutoWebdriver()
        cls.driver.maximizeWindow()
        cls.driver.implicitWait(10)
        cls.driver.navigate(r'http://101.201.41.60:60/platform/web/sys/login')
    def test_login(self):
        try:
            login.login2(self,"lixingyu","123456")
            sleep(1)
        except Exception:
            print('登录失败')


    def test_zhanghu(self):
        '''点击系统管理菜单'''
        self.caidanlists = self.driver.getElenments('css_selector,div[class="el-submenu__title"]')
        print("进入系统管理页面")
        print('div元素个数为' + str(len(self.caidanlists)))
        i = 0
        for itema in self.caidanlists:
            print(itema.text + 'index' + str(i))
            i = i + 1
        self.caidanlists[0].click()
        sleep(1)

        '''进入帐户管理页面'''
        self.zhanghu= self.driver.getElenments('css_selector,li[class="el-submenu is-opened"]>ul>li')
        print('系统管理li元素个数为' + str(len(self.zhanghu)))
        a = 0
        for itemc in self.zhanghu:
            print(itemc.text + 'index' + str(a))
            a = a + 1
        self.driver.action_click1(self.zhanghu, 0)
        sleep(1)
    def test_newuser(self):
        '''csv文本要excel文件另存为csv文件，不要选择csv utf-8文件 会报错'''
        file_user = r'C:\Users\HP\Desktop\测试数据\自动化数据\user.csv'
        '''csv.reader(file(file_city,'rb')),用file的话需要加上参数b,用open的话直接r就可以'''
        users = csv.reader(open(file_user, 'r'))
        '''用户名'''
        for user in users:
            print(user)
            '''获取按钮'''
            self.buttons=self.driver.getElenments('css,button[class ="el-button el-button--primary el-button--mini"]')
            '''点击新增按钮'''
            self.buttons[0].click()
            sleep(1)
            '''获所有文本框'''
            self.inputs=self.driver.getElenments('css,div[class="el-input el-input--mini"]>input')
            '''输入登录帐号'''
            self.driver.type1(self.inputs[1],user)
            '''输入用户名'''
            self.driver.type1(self.inputs[2],user)
            '''输入密码'''
            self.driver.type1(self.inputs[3], '123456')
            '''选择权限'''
            self.inputs[6].click()
            '''获怪权限列表'''
            self.lis=self.driver.getElenments('css,li[class="el-select-dropdown__item"]')
            for i in self.lis:
                print(i.text)
            self.lis[3].click()
            sleep(1)
            self.inputs[1].click()
            sleep(1)
            self.newbuttons = self.driver.getElenments('css,button[class ="el-button el-button--primary el-button--mini"]')
            self.driver.action_click1(self.newbuttons,2)
            sleep(1)
            self.driver.refreshBrowser()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(ZhangHuGuanLi('test_login'))
    suite.addTest(ZhangHuGuanLi('test_zhanghu'))
    suite.addTest(ZhangHuGuanLi('test_newuser'))

    runner = unittest.TextTestRunner()
    runner.run(suite)
