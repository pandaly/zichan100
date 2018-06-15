#-*-coding=UTF-8 -*-
'''
Created on 2017年12月4日

@author: HP
'''
import time
import  sys
from datetime import datetime,timedelta
from random import random, choice
from time import sleep
import unittest
from selenium import webdriver
import  random
sys.path.append(r'E:/Users/HP/PycharmProjects/ZiChan100/src')
from public import login
from public.autowebdriver import AutoWebdriver

class CuiShouXiTong(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = AutoWebdriver()
        cls.driver.implicitWait(10)
        cls.driver.navigate(r'http://101.201.41.60:41303/collect/#/login')
        cls.driver. maximizeWindow()
        cls.driver.refreshBrowser()
    def test_logincuishou(self):
        try:
            login.login_cuishoufang1(self,"cuishoua","123456")
        except Exception:
            print("登录失败")
            print(Exception.__traceback__)


    @classmethod
    def test_caidan(self,index):
        '因为类中直接调用方法，所以需要将该法设为类方法，caidanlists返回菜单，caidanlists索引从0开始，处置方管理员的列表如下：\
        [0:委案管理,1：催记管理，2：业务对接管理，3：还款管理，4：业务稽核，5：系统设置] \
        催收员的列表如下：[0:委案管理,1：催记管理，2：还款管理]'
        caidanlists=self.driver.getElenments('css_selector,div.el-submenu__title')
        print('菜单元素canlists个数为' + str(len(caidanlists)))
        return  caidanlists[index]

    @classmethod
    def test_chuzhiwenanguanli(self):
        '因为类中直接调用方法，所以需要将该法设为类方法，返回处置方管理员或催收员的委案管理菜单元素，点击展开该菜单'
        self.driver.click1(CuiShouXiTong.test_caidan(0))
    def test_rengongcuishou(self):
        #调用类方法获取菜单
        CuiShouXiTong.test_chuzhiwenanguanli()
        el_wenanguanli = CuiShouXiTong.test_caidan(0)
        #获取元素WebElement的可用API
        print(dir(webdriver.remote.webelement.WebElement))
        #调用WebElement的tag_name方法获取标签名
        print(el_wenanguanli.tag_name)
        #因为菜单人工催收和案件管理的ul元素与菜单委案管理的div元素为同级元素，所以采用兄弟的方法获取ul元素
        el_wenanguanlisublist =self.driver.getElenment1(el_wenanguanli,'css_selector+,ul.el-menu')
        print(el_wenanguanlisublist.tag_name)
        print(el_wenanguanlisublist.get_attribute("class"))
        print(el_wenanguanlisublist.get_property("class"))

        el_regongcuishou=self.driver.getElenments1(el_wenanguanlisublist,'css_selector,a li')
        print(el_regongcuishou)
        print(el_regongcuishou[0].tag_name)
        print(len(el_regongcuishou))
        for a in el_regongcuishou:
            print(a.text)
        self.driver.click1(el_regongcuishou[0])

    @classmethod
    def test_ArtificialCollectionLists(self):
        '获取人工催收页面多元素列表方便后续调用'
        #债务人和通讯录为是相同的div类型
        obligor_CommunationLists=self.driver.getElenments('css_selector,div.sider-list')
        return obligor_CommunationLists
    @classmethod
    def test_Obligorlist(cls):
        #调用函数获取债务人div类型
        lists_Obligor=cls.test_ArtificialCollectionLists()
        #获取债务人列表,返回的是元素
        Obligor_lists=cls.driver.getElenments1(lists_Obligor[0], 'css_selector,section >h5')
        print("债务人列表的长度为："+str(len(Obligor_lists)))
        #获取债务人姓名
        for name in Obligor_lists:
            print(name.text)
        return  Obligor_lists


    def test_AddCollection(self):
        tel_CommunationLists=CuiShouXiTong.test_ArtificialCollectionLists()
        #获取通讯录列表
        CommunationLists = self.driver.getElenments1(tel_CommunationLists[1], 'css_selector,section span>i')
        print(len(CommunationLists))
        #获取通讯录姓名
        record_name_lists=self.driver.getElenments1(tel_CommunationLists[1], 'css_selector,section h5')
        #print(str(len(record_name_lists)))

        if len(CommunationLists)>0:
            print("通讯录页面加载成功，通讯录的个数为"+str(len(CommunationLists))+"个")
            n=random.randint(0,len(CommunationLists)-1)
            #print("生成随机数为"+str(n))
            #这个webDriverWait()第一个参数为字符串，需要加引号，否则报错
            self.driver.webDriverWait('By.CSS_SELECTOR','section span>i')
            #将滚动条移动页面底部,有些元素如果不移动滚动条会报元素不可见错误
            js = "var q=document.documentElement.scrollTop=100000"
            self.driver.execute_Script(js)
            self.driver.click1(CommunationLists[n])
            print("弹出第"+str(n+1)+"个添加催记弹窗")
        else:
            print("通讯录页面加载失败或系统异常")
        el_form=self.driver.getElenment('css_selector,div.record-form>form')
        #record_lists1=self.driver.getElenments1(el_form,'css_selector,div.el-form-item ')
        #record_lists获取需要填写催记的所有输入框
        record_lists= self.driver.getElenments1(el_form, 'css_selector,div.el-form-item__content')
        #print("催记填写个数为"+str(len(record_lists)))
        #record_requied_lists = self.driver.getElenments1(el_form, 'css_selector,div.el-form-item.is-required')
        #print("必填个数为"+str(len(record_requied_lists)))
        #获取并输入PTP金额
        el_ptpmoney=self.driver.getElenment1(record_lists[0],'css_selector,input.el-input__inner')
        self.driver.type1(el_ptpmoney,random.randint(1,100))
        #获取并输入PTP时间
        el_ptptime = self.driver.getElenment1(record_lists[1], 'css_selector,input.el-input__inner')
        current_time=datetime.now()
        print(current_time)
        ptptime=datetime.strftime(current_time,r'%Y-%m-%d %H:%M')
        #以下是通过输入时间，切换tab键的方式
        # self.driver.type1(el_ptptime,ptptime)
        # self.driver.send_Keys(el_ptptime,"TAB")
        #点击时间弹窗
        self.driver.click1(el_ptptime)
        #time.sleep(3)
        #点击此刻,点击时间弹窗，加入等待，直到元素可见
        el_ptptime_current=self.driver.webDriverWait('By.CSS_SELECTOR', 'button.el-picker-panel__btn')
        self.driver.click1(el_ptptime_current)
        #获取催收姓名文本框，并输入催收姓名
        el_record_name = self.driver.getElenment1(record_lists[2], 'css_selector,input.el-input__inner')
        record_name = record_name_lists[n].text
        self.driver.type1(el_record_name,record_name)
        # print(record_name)
        #获取下次催收时间文本框并输入内容
        el_record_next_time= self.driver.getElenment1(record_lists[5], 'css_selector,input.el-input__inner')
        next_time=current_time+timedelta(days=2,hours=3)
        reocord_next_time=datetime.strftime(next_time, r'%Y-%m-%d %H:%M')
        print("currenttime is "+ptptime)
        print("nexttime is "+reocord_next_time)
        # 以下是通过输入时间，切换tab键的方式
        self.driver.type1(el_record_next_time,reocord_next_time)
        self.driver.send_Keys(el_record_next_time,"TAB")
        #获取拔结果文本框
        el_call=self.driver.getElenment1(record_lists[6], 'css_selector,input.el-input__inner')
        self.driver.send_Keys(el_call, "TAB")
        el_call_result=self.driver.getElenment1(record_lists[7], 'css_selector,input.el-input__inner')
        self.driver.send_Keys(el_call_result, "ARROW_DOWN")
        self.driver.send_Keys(el_call_result, "ENTER")
        self.driver.send_Keys(el_call_result, "TAB")
        collectioin_result=self.driver.getElenment1(record_lists[8], 'css_selector,input.el-input__inner')
        self.driver.send_Keys(collectioin_result, "ARROW_DOWN")
        self.driver.send_Keys(collectioin_result, "ENTER")
        collection_remark = self.driver.getElenment1(record_lists[10], 'css_selector,textarea.el-textarea__inner')
        self.driver.type1(collection_remark, "自动化测试"+str(current_time))
        self.driver.send_Keys(collection_remark,"TAB")
        collection_button_lists=self.driver.getElenments('css_selector,button.el-button.el-button--primary')
        #self.driver.click1(collection_button_lists[1])
        self.driver.action_Click(collection_button_lists[1])
        #关闭催记弹窗
        collection_close = self.driver.getElenment('css_selector,i.el-picker-panel__btn')
        self.driver.action_Click(collection_close)
        #self.driver.click1(collection_close)
        #显示债务人列表
        toggleButton_lists=self.driver.getElenments('css_selector,button[class="toggleButton"]')
        self.driver.click1(toggleButton_lists[0])
    def test_AddCollectionLists(self):
        #Obligorlists接收到是一个元素列表
        Obligorlists=self.test_Obligorlist()
        if len(Obligorlists)>3:
            ObligorSamples=random.sample(Obligorlists,3)
            n=0
            for i,Obligor in enumerate(Obligorlists):
                if n!=3:
                    self.test_AddCollection()
                    #self.driver.refreshBrowser()
                    sleep(1)
                    self.driver.click1(Obligorlists[i+1])
                    n=n+1
                    print("n的值为："+str(n))
        elif len(Obligorlists)>0:
            for j,Obligor in enumerate(Obligorlists):
                self.test_AddCollection()
                sleep(1)
                self.driver.click1(Obligorlists[j + 1])
                #self.driver.refreshBrowser()
        else:
            print("债务人列表为空")






        '''
        #以下代码报错，此处el_ul_lists列表顺序不规律，多次运行时会出问题
        {
        #获取并点击拨打结果元素，弹出列表
        #el_call_result = self.driver.getElenment1(record_lists[7], 'css_selector,input.el-input__inner')
        #el_call_result = self.driver.getElenment1(record_lists[7], 'css_selector,i.el-input__icon.el-icon-caret-top')
        #print(el_call_result.tag_name)
        #self.driver.click1(el_call_result)
        #self.driver.action_Click(el_call_result)
        print("aaaaaaaaaaaaaaaaaaaa")
          #获取拨打结果列表元素ul
        el_ul_lists=self.driver.webDriverWait('By.CSS_SELECTOR','ul.el-scrollbar__view.el-select-dropdown__list')
        #el_ul_lists=self.driver.getElenments('css_selector,body > div.el-select-dropdown > div > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul')
        print('el_ul_lists'+str(len(el_ul_lists)))
        #获取接听元素列表
        el_result_lists=self.driver.getElenments1(el_ul_lists[0],'li.el-select-dropdown__item> span')
        print('el_result_lists的长度为'+str(len(el_result_lists)))
        for answer in el_result_lists:
            print(answer.text)
        #点击接听
        self.driver.click1(el_result_lists[0])
        }
        '''







if __name__ == '__main__':

    suite = unittest.TestSuite()
    suite.addTest(CuiShouXiTong('test_logincuishou'))
    #suite.addTest(CuiShouXiTong('test_caidan'))
    #suite.addTest(CuiShouXiTong('test_cuizhiwenanguanli'))
    suite.addTest(CuiShouXiTong('test_rengongcuishou'))
    #suite.addTest(CuiShouXiTong('test_AddCollection'))
    #suite.addTest(CuiShouXiTong('test_Obligorlist'))
    suite.addTest(CuiShouXiTong('test_AddCollectionLists'))


    # print(CuiShouXiTong.__doc__)
    # print(CuiShouXiTong.test_caidan.__doc__)
    runner = unittest.TextTestRunner()
    runner.run(suite)