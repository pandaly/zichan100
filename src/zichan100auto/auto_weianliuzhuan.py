# -*-coding=UTF-8 -*-
'''
Created on 2017年7月4日
委案流转模块
@author: HP
'''

from random import randint
import random
from time import sleep
import unittest
import  win32ui
import sys
import wx
sys.path.append(r'E:/Users/HP/PycharmProjects/ZiChan100/src')
from public import login
from public.autowebdriver import AutoWebdriver


class My_frame(wx.Frame):
    def __init__(self,parent):
        wx.Frame.__init__(self,parent,-1,"选择",size=(300,300))
        panel=wx.Panel(self)
        sizer=wx.BoxSizer(wx.VERTICAL)
        panel.SetSizer(sizer)

    def dialog_num(self):
        while True:
            '''弹出一个对话框，获取用户输入'''
            num_dialog = wx.TextEntryDialog(None, '请输入要审核的案件数：', '输入框', '0')
            '''获取用户点击确定或取消按钮'''
            if num_dialog.ShowModal() == wx.ID_OK:
                dia_value = num_dialog.GetValue()
                try:
                    num = int(num_dialog.GetValue())
                    print('用户输入的案件数为：' + str(num))
                    return num
                except Exception as e:
                    print(e)
                    print('输入错误，请重新输入')

                num_dialog = wx.TextEntryDialog(None, '请输入要审核的案件数：', '输入框', '0')
            else:
                '''用户取消时，取默认返回值0'''
                dia_value = num_dialog.GetValue()
                num = int(num_dialog.GetValue())
                print('用户取消，输入的案件数为：' + str(num))
                return num


def create_frame():
    app=wx.App()
    frame=My_frame(None)
    frame.Show(True)
    num=frame.dialog_num()
    frame.Destroy()
    app.MainLoop()
    print('中间返回值为：'+str(num))
    return num

class WeiAnLiuZhuan():
    @classmethod
    def __init__(cls):
        cls.driver = AutoWebdriver()
        cls.driver.maximizeWindow()
        cls.driver.implicitWait(10)
        cls.driver.navigate(r'http://101.201.41.60:40080/platform/web/sys/login')
        cls.test_login(cls)
    def test_login(self):
        try:
            login.login2(self, "lixingyu", "123456")
            # username=input('请输入用户名：')
            # password=input('请输入密码：')
            # login.login2(self, username, password)

        except Exception:
            print('登录失败')


    '''进入委案管理页面'''
    def test_weianliuhzhuan(self):
        self.caidanlists = self.driver.getElenments('css_selector,div[class="el-submenu__title"]')
        print("进入委案管理页面")
        print('div元素个数为' + str(len(self.caidanlists)))
        for i in range(0, len(self.caidanlists)):
            if self.caidanlists[i].text == '委案管理':
                self.caidanlists[i].click()
                break
        sleep(1)

        '''进入委案流转管理页面'''
        self.weianliuzhuan = self.driver.getElenments('css_selector,li[class="el-submenu is-opened"]>ul>li')
        # print('委案管理li元素个数为'+str(len(self.weianliuzhuan)))
        for i in range(0, len(self.weianliuzhuan)):
            if self.weianliuzhuan[i].text == '委案流转管理':
                self.weianliuzhuan[i].click()
                break
        sleep(1)


    '''委案分配'''
    def test_weianfenpei(self):
        ''' 获取标签页'''
        self.weian_biaoqian = self.driver.getElenments('css_selector,div[class="el-tabs__nav"]>div')
        print(len(self.weian_biaoqian))

        '''点击委案分配页面'''
        for i in range(0, len(self.weian_biaoqian)):
            if self.weian_biaoqian[i].text == '委案分配':
                self.weian_biaoqian[i].click()
                print(self.weian_biaoqian[i].text)
                break

        self.shenhezhuangtai = self.driver.getElenments('css_selector,div[class="el-radio-group"]>label>span')

        '''点击待分配状态'''
        for i in range(0, len(self.shenhezhuangtai)):
            if self.shenhezhuangtai[i].text == '待分配':
                self.shenhezhuangtai[i].click()
                print(self.shenhezhuangtai[i].text)
                break
        # tiaojian_input_weiangongsi=input('请输入委案公司：')
        # self.driver.type('css_selector,input[placeholder = "请选择委案公司"]',tiaojian_input_weiangongsi)
        # sleep(10)
        # tiaojian_el_lists=self.driver.getElenments('css_selector,ul[class="el-scrollbar__view el-select-dropdown__list"]')
        # print(len(tiaojian_el_lists))
        '''用户选择查询条件，点击弹框的确定或取消按钮，获得返回值'''
        returnvalue=win32ui.MessageBox('请选择查询条件,选择完查询条件后，再点击本弹框的确定按钮','选择条件框',1)
        if returnvalue==1:
            '''点击查询按钮'''
            self.chaxun_weianliuzhuan()
            sleep(2)
        else:
            pass
        sleep(1)
        '''获得要用户要分配的案件数量'''
        anjian_num=create_frame()
        print('最终返回值为'+str(anjian_num))
        if anjian_num>100:
            num_int=anjian_num//100 #取整数
            num_mod=anjian_num%100  #取余数
            #num_cishu=num_int+1
            print('需要翻页'+str(num_int)+'次，每面显示100条')
        elif anjian_num>50:
            num_int = anjian_num // 50  # 取整数
            num_mod = anjian_num % 50  # 取余数
            #num_cishu = num_int + 1
            print('需要翻页' + str(num_int) + '次，每面显示50条')
        elif anjian_num>10:
            num_int = anjian_num // 10  # 取整数
            num_mod = anjian_num % 10  # 取余数
            #num_cishu = num_int + 1
            print('需要翻页' + str(num_int) + '次，每面显示10条')
        elif anjian_num>=0:
            pass
        else:
            print('输入有误，请重新输入')

        el_table=self.driver.webdriverwait('By.CSS_SELECTOR','div[class="el-table__fixed-body-wrapper"]')
        print(el_table.text)

    def chaxun_weianliuzhuan(self):
        '''点击查询按钮'''
        self.anniu_chaxun = self.driver.getElenments(
            'css_selector,button[class="el-button el-button--success el-button--mini"]')
        self.driver.action_click1(self.anniu_chaxun, 0)
        print('s查询执行')


    def test_weianfenpei1(self):
        def chaxun():
            '''点击查询按钮'''
            self.anniu_chaxun = self.driver.getElenments(
                'css_selector,button[class="el-button el-button--success el-button--mini"]')
            self.driver.action_click1(self.anniu_chaxun, 0)
            print('查询....')
        '''获取标签页'''
        self.weian_biaoqian = self.driver.getElenments('css_selector,div[class="el-tabs__nav"]>div')

        '''点击委案分配页面'''
        self.driver.action_click1(self.weian_biaoqian, 1)
        sleep(1)
        chaxun()
        sleep(1)

        '''获取委案状态'''
        self.weianzhuangtai = self.driver.getElenments('css_selector,span[class="el-radio-button__inner"]')
        '''点击待分配'''
        self.weianzhuangtai[1].click()
        chaxun()

        '''获取逾期时间'''
        self.yuqishijian = self.driver.getElenments('css_selector,div[class="el-checkbox-group"]>label')
        print(len(self.yuqishijian))

        for n in range(3):
            k = randint(1, 15)
            print(k)
            M_list = ["M0", "M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8", "M9", "M10", "M11", "M12", "M13-M24",
                      "M24+"]
            v_list = random.sample(M_list, k)

            i = 0
            for Mvalue in self.yuqishijian:
                for v in v_list:
                    if Mvalue.text == v:
                        self.yuqishijian[i].find_element_by_css_selector('span[class="el-checkbox__inner"]').click()
                print(Mvalue.text + "index" + str(i))
                i = i + 1
                chaxun()



def test_start():
    weian = WeiAnLiuZhuan()
    weian.test_weianliuhzhuan()
    weian.test_weianfenpei()


if __name__ == '__main__':
    # suite = unittest.TestSuite()
    # suite.addTest(WeiAnLiuZhuan('test_login'))
    # suite.addTest(WeiAnLiuZhuan('test_weianliuhzhuan'))
    # suite.addTest(WeiAnLiuZhuan('test_weianshenhe'))
    # #suite.addTest(WeiAnLiuZhuan('test_weianfenpei'))
    #
    # runner = unittest.TextTestRunner()
    # runner.run(suite)

    test_start()