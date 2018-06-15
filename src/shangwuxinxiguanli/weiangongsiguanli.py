# -*-coding=UTF-8 -*-
'''
Created on 2017年4月5日

@author: HP
'''
from _io import open
import csv
import random
from time import sleep
import unittest
import sys

sys.path.append(r'E:/Users/HP/PycharmProjects/ZiChan100/src')

from public import login
from public.autowebdriver import AutoWebdriver


class WeiAnGongSi(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = AutoWebdriver()
        cls.driver.maximizeWindow()
        cls.driver.implicitWait(10)
        cls.driver.navigate(r'http://101.201.41.60:60/platform/web/sys/login')

    def test_login(self):
        try:
            login.login2(self, "lixingyu", "123456")
        except Exception:
            print('登录失败')

    def test_weiangongsiguanli(self):
        '''进入商务信息管理页面'''
        self.caidanlists = self.driver.getElenments('css_selector,div[class="el-submenu__title"]')
        print("进入商务信息管理页面")
        print('div元素个数为' + str(len(self.caidanlists)))
        i = 0
        for itema in self.caidanlists:
            print(itema.text + 'index' + str(i))
            i = i + 1
        self.caidanlists[2].click()
        sleep(1)

        self.weianliuzhuan = self.driver.getElenments('css_selector,li[class="el-submenu is-opened"]>ul>li')
        print('商务信息管理页面li元素个数为' + str(len(self.weianliuzhuan)))

        '''进入委案公司管理页面'''
        a = 0
        for itemc in self.weianliuzhuan:
            print(itemc.text + 'index' + str(a))
            a = a + 1
        self.driver.action_click1(self.weianliuzhuan, 0)
        sleep(1)
        self.clickchaxun()
        sleep(1)


    def test_chaxun_gongsiming(self):
        '''打开文本文件'''
        file_name = open(r'C:\Users\HP\Desktop\测试数据\自动化数据\委案公司.txt', 'r')

        '''按行读取文件,全部读取并存到一个列表里，注意换行字符\n也读取到的'''
        weiannames = file_name.readlines()

        '''文件关闭'''
        file_name.close()

        print(weiannames)
        for nam in weiannames:
            nam = nam.strip('\n')
            print(nam)
        '''从文本中随机获取一个公司名'''
        name = random.choice(weiannames).strip('\n')

        '''定位公司名称文本框'''
        self.driver.refreshBrowser()
        sleep(2)
        els = self.driver.getElenments('css_selector,div[class="el-input el-input--mini"]>input')
        '''输入刚获取的公司名并查询'''
        self.driver.type1(els[0], name)
        self.clickchaxun()
        sleep(1)

        '''获取table中有多少行'''
        trs = self.driver.getElenments('css_selector,div[class="el-table__body-wrapper"]>table>tbody>tr')
        print(len(trs))

        '''从每行中获取第四列公司名称并判断'''
        weiangongsi_tu = 0
        for tr in trs:
            try:
                td = tr.find_element_by_css_selector('td[class="el-table_1_column_4 is-left"]>div')
                gongsiming_text = self.driver.getText1(td)
            except:
                print('获取列表中的公司名称失败')

            if name not in gongsiming_text:
                print(name)
                print('查询结果有误')
                '''截图保存'''
                self.driver.getscreenshot(r'e:\weiangongsiguanli', str(weiangongsi_tu))
                weiangongsi_tu = weiangongsi_tu + 1

    def test_chaxun_city(self):
        '''csv文本要excel文件另存为csv文件，不要选择csv utf-8文件 会报错'''
        file_city = r'C:\Users\HP\Desktop\测试数据\自动化数据\城市列表2.csv'
        '''csv.reader(file(file_city,'rb')),用file的话需要加上参数b,用open的话直接r就可以'''
        cities = csv.reader(open(file_city, 'r'))
        '''获取省份'''
        procitylist = []
        for procity in cities:
            procitylist.append(procity)
        print(procitylist)
        choice = random.choice(procitylist)
        province = choice[0]
        print(province)

        '''获取城市'''
        city = choice[1]
        print(city)
        '''获取省份文本框并输入省份'''
        shengshidivlist = self.driver.getElenments('css_selector,div[class="el-input el-input--mini"]>input')
        self.driver.type1(shengshidivlist[1], province)
        sleep(1)

        # '''输入不存在的省份时，获取无区配数元素'''
        # empty_list=self.driver.getElenments('css_selector,p[class="el-select-dropdown__empty"]')
        # if empty_list[1].is_displayed():
        #     raise  Exception ('主动引发异常：省份'+empty_list[1].text)


        '''选择省份,城市，换页元素列表，城市为0，省份为2，换页为1'''
        divlists=self.driver.getElenments('css_selector,ul[class="el-scrollbar__view el-select-dropdown__list"]')
        provincelist=divlists[2].find_elements_by_css_selector('li')
        print('列表中共有'+str(len(provincelist))+'个省')

        '''选择省份,此处注意一下，省份列表provincelist中的元素如果没有显示时，其文本内容为空;
        如输入广东时，关联提示中只有广东省是显示的，其shengfen.text的值为广东省，其他省份的shengfen.text为null'''
        for shengfen in provincelist:
            if province in shengfen.text:
                shengfen.click()
                print(shengfen.text)
                break
            elif shengfen.text is None or shengfen.text=='':
                continue
            else:
                print('省份输入有误，重新输入')


        '''获取城市文本框并输入城市'''
        shengshidivlist = self.driver.getElenments('css_selector,div[class="el-input el-input--mini"]>input')
        self.driver.type1(shengshidivlist[2], city)
        citylist = divlists[0].find_elements_by_css_selector('li')
        print(province+'共有'+str(len(citylist))+'个城市')
        '''选择城市'''
        for chengshi in citylist:
            if city in chengshi.text:
                chengshi.click()
            elif chengshi.text is None or chengshi.text=='':
                continue
            else:
                print('城市输入有误，重新输入')
                break
        self.clickchaxun()
        sleep(1)
        '''获取table中有多少行'''
        trs = self.driver.getElenments('css_selector,div[class="el-table__body-wrapper"]>table>tbody>tr')
        print('查询结果列表中共有'+str(len(trs))+'行'+'trs='+str(len(trs)))

        '''从每行中获取第16列城市名并判断'''
        chengshi_tu = 0
        for tr in trs:
            if tr.is_displayed():
                try:
                    td = tr.find_element_by_css_selector('td[class="el-table_1_column_16 is-left"]>div')
                    city_text = self.driver.getText1(td)
                except:
                    print('获取列表中的城市名失败')
                    #print(tr.is_displayed())
                if city not in city_text:
                    print(city)
                    print('查询结果有误')
                    '''截图保存'''
                    # self.driver.get_screenshot_as_file(r'e:\weiangongsiguanli'+str(weiangongsi_tu)+r'.png')
                    self.driver.getscreenshot(r'e:\weiangongsiguanli城市',str(chengshi_tu))
                    chengshi_tu= chengshi_tu + 1
            else:
                print('不在查询结果中')
        self.hezuozhuangtai()

    def test_function(self):
        self.hezuozhuangtai()
        self.gongsijibie()

    def clickchaxun(self):
            '''点击查询按钮'''
            self.anniu_chaxun = self.driver.getElenments(
                'css_selector,button[class="el-button el-button--success el-button--mini"]')
            try:
                self.driver.action_click1(self.anniu_chaxun, 0)
            except Exception as e:
                print(Exception, ":", e)
    def hezuozhuangtai(self):
        el=self.driver.getElenments('css_selector,div[class="el-checkbox-group"]')[0]
        hezuolist=self.driver.getElenments1(el,'css_selector,label')
        k=random.randrange(1,5)
        my_hezuoist=['试案','合作中','暂停','中止']
        v_hezuolist=random.sample(my_hezuoist,k)

        for hezuo in hezuolist:
            for v in v_hezuolist:
                if v==hezuo.text:
                    self.driver.getElenment1(hezuo,'css_selector,span[class="el-checkbox__input"]>span').click()

    def gongsijibie(self):
        el = self.driver.getElenments('css_selector,div[class="el-checkbox-group"]')[1]
        jibielist = self.driver.getElenments1(el, 'css_selector,label')
        k = random.randrange(1, 4)
        my_jibielist = ['初级', '高级', '大客户']
        v_jibielist = random.sample(my_jibielist, k)

        for jibie in jibielist:
            for v in v_jibielist:
                if v == jibie.text:
                    self.driver.getElenment1(jibie, 'css_selector,span[class="el-checkbox__input"]>span').click()




if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(WeiAnGongSi('test_login'))
    suite.addTest(WeiAnGongSi('test_weiangongsiguanli'))
    #suite.addTest(WeiAnGongSi('test_chaxun_gongsiming'))
    #suite.addTest(WeiAnGongSi('test_chaxun_city'))
    suite.addTest(WeiAnGongSi('test_function'))

    runner = unittest.TextTestRunner()
    runner.run(suite)
