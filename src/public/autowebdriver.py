# -*- coding: utf-8 -*-
'''
Created on 2017年4月14日

@author: HP

参考：http://www.jianshu.com/p/b5957c487350

'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class AutoWebdriver():
    def __init__(self):
        '''启动浏览器'''
        driver=webdriver.Chrome()
        try:
            self.driver=driver
            print("浏览器启动成功")
        except Exception:
            raise NameError('浏览器未成正常启动。。')

        
    def clearCookies(self):
        '''启动后删除cookies'''
        self.driver.delete_all_cookies()
        
    def refreshBrowser(self):
        '''刷新页面'''
        self.driver.refresh()
        print("浏览器刷新成功")
        
    def maximizeWindow(self):
        '''最大化浏览器'''
        print("浏览器最大化前")
        self.driver.maximize_window()
        print("浏览器最大化后")
        
    def navigate(self,url):
        '''打开页面'''
        self.driver.get(url)
        
    def quitBrowser(self):
        '''退出浏览器'''
        self.driver.quit()  
        
    def closeBrowser(self):
        '''关闭浏览器'''
        self.driver.close()
        
    def getElenment(self,selector):
        '''
        ;定位单个元素
        ;selector参数以 'x,//*[@id='langs']/button' 形式传入
        ;其中，前面的x表示选择元素的方式，id,css_selector,xpath,name等等
        ;，后面的表示元素定位的属性值 
        '''
        if ',' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by=selector.split(',')[0]
        selector_value=selector.split(',')[1]
        
        if selector_by=='id':
            element=self.driver.find_element_by_id(selector_value)
        elif selector_by=='css_selector' or selector_by=='css':
            element=self.driver.find_element_by_css_selector(selector_value)
        elif selector_by=='tag_name' or selector_by=='tag':
            element=self.driver.find_element_by_tag_name(selector_value)
        elif selector_by=='class_name' or selector_by=='class':
            element=self.driver.find_element_by_class_name(selector_value)
        elif selector_by=='xpath':
            element=self.driver.find_element_by_xpath(selector_value)
        elif selector_by=='link_text' or selector_by=='link':
            element=self.driver.find_element_by_link_text(selector_value)
        elif selector_by=='partial_link_text' or selector_by=='partial':
            element=self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by=='name':
            element=self.driver.find_element_by_name(selector_value)
        else:
            raise NameError ('请输入有效的元素选择器类型')
        return element

    def getElenment1(self, el,selector):
        '''
        ;定位单个元素
        ;selector参数以 'x,//*[@id='langs']/button' 形式传入
        ;其中，前面的x表示选择元素的方式，id,css_selector,xpath,name等等
        ;，后面的表示元素定位的属性值 
        '''
        if ',' not in selector:
            return el.find_element_by_id(selector)
        selector_by = selector.split(',')[0]
        selector_value = selector.split(',')[1]

        if selector_by == 'id':
            element = el.find_element_by_id(selector_value)
        elif selector_by == 'css_selector' or selector_by == 'css':
            element = el.find_element_by_css_selector(selector_value)
        elif selector_by == 'css_selector+' or selector_by == 'css+':
            #获取兄弟元素，先获取元素的标签名，再获取该 元素的兄弟元素，注意中间的"+"
            element = self.driver.find_element_by_css_selector(el.tag_name+"+"+selector_value)
        elif selector_by == 'tag_name' or selector_by == 'tag':
            element = el.find_element_by_tag_name(selector_value)
        elif selector_by == 'class_name' or selector_by == 'class':
            element = el.find_element_by_class_name(selector_value)
        elif selector_by == 'xpath':
            element = el.find_element_by_xpath(selector_value)
        elif selector_by == 'link_text' or selector_by == 'link':
            element = el.find_element_by_link_text(selector_value)
        elif selector_by == 'partial_link_text' or selector_by == 'partial':
            element = el.find_element_by_partial_link_text(selector_value)
        elif selector_by == 'name':
            element = el.find_element_by_name(selector_value)
        else:
            raise NameError('请输入有效的元素选择器类型')
        return element
    
    def getElenments(self,selector):
        '''
        ;定位一组元素
        ;selector参数以 'x,//*[@id='langs']/button' 形式传入
        ;其中，前面的x表示选择元素的方式，id,css_selector,xpath,name等等
        ;，后面的表示元素定位的属性值 
        '''
        if ',' not in selector:
            return self.driver.find_elements_by_id(selector)
        selector_by=selector.split(',')[0]
        selector_value=selector.split(',')[1]
        
        if selector_by=='id':
            elements=self.driver.find_elements_by_id(selector_value)
        elif selector_by=='css_selector' or selector_by=='css':
            elements=self.driver.find_elements_by_css_selector(selector_value)
        elif selector_by=='tag_name' or selector_by=='tag':
            elements=self.driver.find_elements_by_tag_name(selector_value)
        elif selector_by=='class_name' or selector_by=='class':
            elements=self.driver.find_elements_by_class_name(selector_value)
        elif selector_by=='xpath':
            elements=self.driver.find_elements_by_xpath(selector_value)
        elif selector_by=='link_text' or selector_by=='link':
            elements=self.driver.find_elements_by_link_text(selector_value)
        elif selector_by=='partial_link_text' or selector_by=='partial':
            elements=self.driver.find_elements_by_partial_link_text(selector_value)
        elif selector_by=='name':
            elements=self.driver.find_elements_by_name(selector_value)

        else:
            raise NameError ('请输入有效的元素选择器类型')
        return elements

    def getElenments1(self, el,selector):
        '''
        ;定位一组元素
        ;selector参数以 'x,//*[@id='langs']/button' 形式传入
        ;其中，前面的x表示选择元素的方式，id,css_selector,xpath,name等等
        ;，后面的表示元素定位的属性值 
        '''
        if ',' not in selector:
            return el.find_elements_by_id(selector)
        selector_by = selector.split(',')[0]
        selector_value = selector.split(',')[1]

        if selector_by == 'id':
            elements = el.find_elements_by_id(selector_value)
        elif selector_by == 'css_selector' or selector_by == 'css':
            elements = el.find_elements_by_css_selector(selector_value)
        elif selector_by == 'tag_name' or selector_by == 'tag':
            elements = el.find_elements_by_tag_name(selector_value)
        elif selector_by == 'class_name' or selector_by == 'class':
            elements = el.find_elements_by_class_name(selector_value)
        elif selector_by == 'xpath':
            elements = el.find_elements_by_xpath(selector_value)
        elif selector_by == 'link_text' or selector_by == 'link':
            elements = el.find_elements_by_link_text(selector_value)
        elif selector_by == 'partial_link_text' or selector_by == 'partial':
            elements = el.find_elements_by_partial_link_text(selector_value)
        elif selector_by == 'name':
            elements = el.find_elements_by_name(selector_value)
        else:
            raise NameError('请输入有效的元素选择器类型')
        return elements
    def webDriverWait(self,method,selector):
        '''EC.visibility_of_element_located((By.method, selector)))参数为一个，所以(By.method, selector)须用（）括起来，否则会报错       
        '''
        try:
            if method=='By.CSS_SELECTOR':
                el=WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.CSS_SELECTOR,selector)))
                print('webdriverwait 函数已运行')
                return el
            elif method=='ID'or method=='id':
                el = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.ID, selector)))
                print('webdriverwait 函数已运行')
                return el
            elif method=='LINK_TEXT':
                el = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.LINK_TEXT, selector)))
                print('webdriverwait 函数已运行')
                return el
            elif method=='NAME':
                el = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.NAME, selector)))
                print('webdriverwait 函数已运行')
                return el
            elif method == 'TAG_NAME':
                el = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.TAG_NAME, selector)))
                print('webdriverwait 函数已运行')
                return el
            elif method=='CLASS_NAME':
                el = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.CLASS_NAME, selector)))
                print('webdriverwait 函数已运行')
                return el
            elif method=='PARTIAL_LINK_TEXT':
                el = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, selector)))
                print('webdriverwait 函数已运行')
                return el
            else:
                print('By定位元素方式错误')
        except Exception as e:
            print(e)
            raise NameError('请输入有效的元素选择器类型')
    def type(self,selector,text):
        '''文本框输入值'''
        el=self.getElenment(selector)
        el.clear()
        el.send_keys(text)
    def type1(self,el,text):
        '''文本框输入值'''
        el.clear()
        el.send_keys(text)   
    def click(self,selector):
        '''点击操作'''
        el=self.getElenment(selector)
        el.click()
    def click1(self,el):
        '''点击操作'''
        el.click()
    def action_click(self,selector,n):
        elements=self.getElenments(selector)
        el=elements[n]
        ActionChains(self.driver).click(el).perform()   
        
    def action_click1(self,elements,n):
        ActionChains(self.driver).click(elements[n]).perform()
    def getscreenshot(self,path,name):
        self.driver.get_screenshot_as_file(path+name+r'.png')
        
    def selectByIndex(self,selector,index):
        '''选择下拉列表'''
        el=self.getElenment(selector)
        Select(el).select_by_index(index)
        
    def clickText(self,text):
        '''点击超链接'''
        self.getElenment('partial_text,'+text).click()
        
    def submit(self,selector):
        '''提交按钮'''
        el=self.getElenment(selector)
        el.click()
    
    def executeJS(self,script):
        '''运行js脚本程序'''
        self.driver.execute_script(script)
        
    def getAttribute(self,selector,attribute):
        '''获取属性值'''
        el=self.getElenment(selector)
        return el.get_attribute(attribute)
    def getAttribute1(self,el,attribute):
        '''获取属性值'''
        print( el.get_attribute(attribute))
        return el.get_attribute(attribute)
    
    def getText(self,selector):
        '''获取元素的文本值'''
        el=self.getElenment(selector)
        return el.text
    
    def getText1(self,el):
        '''获取元素的文本值'''
        print(el.text)
        return el.text
    
    def getDisplay(self,selector):
        '''显示元素'''
        el=self.getElenment(selector)        
        return el.is_displayed()
    
    def getTitle(self):
        '''获得页面标题'''
        return self.driver.title
    
    def getUrl(self):
        '''获取当前页面的网址'''
        return self.driver.current_url
    
    def acceptAlert(self):
        '''接受弹窗警告'''
        self.driver.switch_to_alert().accept()
    
    def dismissAlert(self):
        '''取消警告'''
        self.driver.switch_to_alert().dismiss()
        
    def implicitWait(self,sec):
        '''等待时间'''
        self.driver.implicitly_wait(sec)
        
    def switchFrame(self,selector):
        '''切换Frame'''
        el=self.getElenment(selector)
        self.driver.switch_to.frame(el)
        
    def switchDefaultFrame(self):
        '''切换到默认Frame'''
        self.driver.switch_to_default_content()
        
    def openNewWindow(self,selector):
        '''打开新窗口'''
        original_window=self.driver.current_window_handle
        el=self.getElenment(selector)
        el.click()
        all_handlers=self.driver.window_handles
        for handler in all_handlers:
            if handler !=original_window:
                self.driver.switch_to_window(handler)

    def execute_Script(self,js):
        '移动滚动条，使页面元素显示出来'
        self.driver.execute_script(js)
        #print("移动滚动条到底部")

    def send_Keys(self,el,key):
        if key=="TAB" or key=="tab":
            el.send_keys(Keys.TAB)
        elif key=="ENTER" or key=="enter" or key=="Enter":
            el.send_keys(Keys.ENTER)
        elif key=="ARROW_DOWN":
            el.send_keys(Keys.ARROW_DOWN)
        else:
            print("请输入有效的单键")

    def action_Click(self,el):
        ActionChains(self.driver).click(el).perform()

                

        
