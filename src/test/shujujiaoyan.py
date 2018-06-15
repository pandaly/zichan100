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
            num_dialog=wx.TextEntryDialog(None,'请输入要审核的案件数：','输入框','0')
            '''获取用户点击确定或取消按钮'''
            if num_dialog.ShowModal()==wx.ID_OK:
                dia_value=num_dialog.GetValue()
                try:
                    num = int(num_dialog.GetValue())
                    print('用户输入的案件数为：' + str(num))
                    return  num
                except Exception as e:
                    print(e)

                    print('输入错误，请重新输入')

                num_dialog = wx.TextEntryDialog(None, '请输入要审核的案件数：', '输入框', '0')
            else:
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

def msgbox():
        '''用户选择查询条件，点击弹框的确定或取消按钮，获得返回值'''
        returnvalue=win32ui.MessageBox('请选择查询条件','选择条件框',1)
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

        elif anjian_num>50:
            num_int = anjian_num // 50  # 取整数
            num_mod = anjian_num % 50  # 取余数
        elif anjian_num>10:
            num_int = anjian_num // 10  # 取整数
            num_mod = anjian_num % 10  # 取余数
        elif anjian_num>0:
            pass
        else:
            print('输入有误，请重新输入')


if __name__ == '__main__':
    create_frame()