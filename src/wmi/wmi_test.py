import  wmi
import os
import time
import  sys
import  configparser


'''遍历所有进程'''
def win_pid():

    c=wmi.WMI()
    for process in c.Win32_Process():

        print('%s,%s'  %(process.ProcessId,process.Name))

'''遍历所有wmi的方法'''
def win_all():
    s=wmi.WMI()
    for sp in dir(s):
        print(s._getAttributeNames())

if __name__=='__main__':
    win_pid()
    win_all()

  




