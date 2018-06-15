import win32com
import win32ui
import tkinter
import os
import re
from tkinter import filedialog
#导入win32com第三方库
from win32com import client
def open_file():
    #创建 tkinter顶层容器
    root =tkinter.Tk()
    #顶层容器标题
    root.title('test')
    #创建一个框器（也是一个容器）
    f = tkinter.Frame(root,width=10)
    f.pack()
    win32ui.MessageBox('请选择文件')
    # 使用tkinter库中的filedialog类的askdirectroy()方法
    dialog = filedialog.askdirectory(initialdir =r'C:\Users\HP\Desktop',mustexist= False,parent=f,title= 'Please select directory')
    #打印选择的文件名
    print(dialog)
    #销毁容器
    root.destroy()
    print(os.listdir(dialog))
    print('11111111111')
    for file in os.listdir(dialog):
        if file.endswith(".xlsx") or file.endswith('.xls'):
            filepath=os.path.join(dialog,file)
            filesize=round(os.path.getsize(filepath)/1024)
            print(file+'   大小：'+str(filesize)+ 'KB' )
            excel_open(filepath)


def open_file_old():
    win32ui.MessageBox('请选择文件')
    # dialog= win32ui.CreateFileDialog(1, ".xlsx", "default.xlsx", 0, "Text Files (*.xlsx)|*.xlsx|All Files (*.*)|*.*|")# 1表示打开文件对话框,0表示保存对话框，只显示xlsx格式的文件，默认为default.xlsx文件
    dialog = win32ui.CreateFileDialog(1, ".xlsx", None, 0,
                                      "Text Files (*.xlsx)|*.xlsx|All Files (*.*)|*.*|")  # 1表示打开文件对话框,只显示xlsx格式的文件
    # dialog= win32ui.CreateFileDialog(1, ".xlsx|.xls", "default.xlsx", 0, "Text Files (*.xlsx,*.xls)|*.xlsx|*.xls|All Files (*.*)|*.*|")#这个有问题 ，不显示.xls的文件

    dialog.SetOFNInitialDir(r'C:\Users\HP\Desktop')  # 设置打开文件对话框中的初始显示目录
    dialog.DoModal()  # 设为模态模式
    filename = dialog.GetPathName()  # 获取选择的文件名称
    print(filename)

def excel_test():
    #启动excel程序
    excel=client.Dispatch('Excel.Application')
    print(excel)
    #新增一个excel工作薄
    excel_work=excel.Workbooks.Add()
    #激活Sheet表
    excel_sheet=excel_work.ActiveSheet
    #启动excel程序默认是不可见的，设置为可见
    excel.Visible=True
    #设置表中单元格的值
    excel_sheet.Cells(1,1).value="赵亚运是超级无敌神经病"
    #工作蒲另存到桌面tesa
    excel_work.SaveAs(r'C:\Users\HP\Desktop\tesa.xlsx')
    #关闭excelt程序
    excel_work.Close()


def excel_open1():
    #启动excel程序
    excel_application=client.Dispatch('Excel.Application')
    #打开一个excel工作薄
    #excel_work=excel_application.Workbooks.Open(r'C:\Users\HP\Desktop\前端页面切换排期.xlsx')
    excel_work = excel_application.Workbooks.Open(r'C:\Users\HP\Desktop\tesa.xlsx')

    #激活Sheet表
    #excel_sheet=excel_work.Worksheets('前端框架切换')
    excel_sheet = excel_work.Worksheets('Sheet1')
    #启动excel程序默认是不可见的，设置为可见
    excel_application.Visible=True
    #设置表中单元格的值
    excel_sheet.Cells(1, 1).Value = "赵亚运是超级无敌神经病"
    excel_sheet.Cells(7, 1).NumberFormatLocal = "@"
    excel_sheet.Cells(7, 1).Value = "371327198806232661"
    print("B1的值为："+excel_sheet.Cells(1, 2).Value)
    excel_sheet.Range("B1").Copy()
    excel_sheet.Paste(excel_sheet.Cells(8, 1))
    excel_sheet.Cells(8, 1).NumberFormatLocal = "yyyy/m/d"
    print("A8的值为："+excel_sheet.Cells(8, 1).Value)
    #输出单元格中的值
    print(excel_sheet.Cells(1,1).Value)

    #复制A1:A3区域
    excel_sheet.Range("A1:A3").Copy()
    #粘贴到D1
    excel_sheet.Paste(excel_sheet.Range("D1"))
    #保存  另存为为SaveAs()
    excel_work.Save()
    #关闭
    excel_work.Close()

def excel_open2():
    #启动excel程序
    excel_application=client.Dispatch('Excel.Application')
    # 启动excel程序默认是不可见的，设置为可见
    excel_application.Visible = True

    #打开一个excel工作薄
    excel_work = excel_application.Workbooks.Open(r'C:\Users\HP\Desktop\催收-百分百委外20170519（原委案表）.xlsx')
    #获取表名及表的个数
    sheets=excel_work.Worksheets
    print(len(sheets))
    for sheet in sheets:
        print(sheet.name)
    #激活Sheet表
    excel_sheet = excel_work.Worksheets(1)


    #获取有数据的行数和列数
    rows=excel_sheet.UsedRange.Rows.Count
    columns=excel_sheet.UsedRange.Columns.Count
    print('行数为：'+str(rows)+";列数为："+str(columns))
    #输出一行的数据
    print(excel_sheet.Range("A1:G1").Value)

    #关闭
    excel_work.Close()

def excel_open(filepath):
    #启动excel程序
    excel_application=client.Dispatch('Excel.Application')
    # 启动excel程序默认是不可见的，设置为可见
    excel_application.Visible = True

    #打开一个excel工作薄
    excel_work = excel_application.Workbooks.Open(filepath)
    #获取表名及表的个数
    sheets=excel_work.Worksheets
    print(len(sheets))
    for sheet in sheets:
        print(sheet.name)
    #激活Sheet表
    excel_sheet = excel_work.Worksheets(1)


    #获取有数据的行数和列数
    rows=excel_sheet.UsedRange.Rows.Count
    columns=excel_sheet.UsedRange.Columns.Count
    print('行数为：'+str(rows)+";列数为："+str(columns))
    #输出一行的数据
    print(excel_sheet.Range("A1:G1").Value)

    #关闭
    excel_work.Close()

def excel_new():
    # 启动excel程序
    excel_application = client.Dispatch('Excel.Application')
    # 启动excel程序默认是不可见的，设置为可见
    excel_application.Visible = True

    # 打开一个excel工作薄 s source的缩写，d destination的缩写
    excel_work_s = excel_application.Workbooks.Open(r'C:\Users\HP\Desktop\测试数据\0811测试数据\副本M4案件委案明细0810资产百分百.xlsx')
    excel_work_d = excel_application.Workbooks.Open(r'C:\Users\HP\Desktop\testa.xlsx')
    # 获取表的个数
    s_sheets = excel_work_s.Worksheets
    print(len(s_sheets))
    # 获取表名
    for sheet in s_sheets:
        print(sheet.Name)
    # 激活Sheet表
    excel_sheet_s = excel_work_s.Worksheets(1)
    excel_sheet_d = excel_work_d.Worksheets(1)

    # 获取有数据的行数和列数
    rows_s = excel_sheet_s.UsedRange.Rows.Count
    columns_s = excel_sheet_s.UsedRange.Columns.Count
    print('行数为：' + str(rows_s) + ";列数为：" + str(columns_s))
    # 输出一行数据,输出结果为元组
    excel_sheet_stuple=excel_sheet_s.Range(excel_sheet_s.Cells(1,1),excel_sheet_s.Cells(1,columns_s)).Value
    excel_sheet_dtuple=excel_sheet_d.Range(excel_sheet_d.Cells(1,1),excel_sheet_d.Cells(1,30)).Value
    print(excel_sheet_stuple[0])
    print(excel_sheet_dtuple[0])
    #将元组转为列表
    excel_sheet_slist=list(excel_sheet_stuple[0])
    print(len(excel_sheet_slist))
    excel_sheet_dlist = list(excel_sheet_dtuple[0])
    print(len(excel_sheet_dlist))
    #获取列表的前十个字段，方便查找债务人和业务流水号
    excel_sheet_slist_1=excel_sheet_slist[0:20]
    print(excel_sheet_slist_1)
    copy_ObligorName(excel_sheet_s,excel_sheet_d,rows_s,excel_sheet_slist_1)
    copy_BizSerialNumber(excel_sheet_s,excel_sheet_d, rows_s, excel_sheet_slist_1)
    copy_ObligorID(excel_sheet_s,excel_sheet_d, rows_s, excel_sheet_slist_1)
    copy_PhoneNumber(excel_sheet_s,excel_sheet_d, rows_s, excel_sheet_slist_1)
    copy_RepaySum(excel_sheet_s,excel_sheet_d, rows_s, excel_sheet_slist)
    copy_RepayDate(excel_sheet_s,excel_sheet_d, rows_s, excel_sheet_slist)
    copy_RepayDateNumNum(excel_sheet_s,excel_sheet_d, rows_s, excel_sheet_slist)
    copy_RepayDeadLineNum(excel_sheet_s,excel_sheet_d, rows_s, excel_sheet_slist)

    # 保存  另存为为SaveAs()
    excel_work_d.SaveAs(r'C:\Users\HP\Desktop\test2.xlsx')
    # excel_work_s.SaveAs(r'C:\Users\HP\Desktop\test1.xlsx')
    #取消原表中是否需要保存的提示框，还有是否复制的的提示框
    excel_application.DisplayAlerts = False
    excel_application.CutCopyMode = win32com.client.constants.xlCut  # 清除剪贴板内容
    # 关闭
    excel_work_s.Close()
    excel_work_d.Close()
    excel_application.Visible = False
'''
    # 获取债务人在列表中的位置，即在第几列
    if '姓名' in excel_sheet_slist_1:
        ObligorName_index=excel_sheet_slist_1.index('姓名')
        print(ObligorName_index)
        # 复制源表姓名列内容
        excel_sheet_s.Range(excel_sheet_s.Cells(2,ObligorName_index+1),excel_sheet_s.Cells(rows_s,ObligorName_index+1)).Copy()
        # 粘贴模板表债务人姓名列
        excel_sheet_d.Paste(excel_sheet_d.Cells(2,ObligorName_index))
    elif "借款人" in  excel_sheet_slist_1:
        ObligorName_index=excel_sheet_slist_1.index('姓名')
        print(ObligorName_index)
        # 复制源表姓名列内容
        excel_sheet_s.Range(excel_sheet_s.Cells(2,ObligorName_index+1),excel_sheet_s.Cells(rows_s,ObligorName_index+1)).Copy()
        # 粘贴模板表债务人姓名列
        excel_sheet_d.Paste(excel_sheet_d.Cells(2,ObligorName_index))
    elif  "借款人姓名" in  excel_sheet_slist_1:
        ObligorName_index=excel_sheet_slist_1.index('姓名')
        print(ObligorName_index)
        # 复制源表姓名列内容
        excel_sheet_s.Range(excel_sheet_s.Cells(2,ObligorName_index+1),excel_sheet_s.Cells(rows_s,ObligorName_index+1)).Copy()
        # 粘贴模板表债务人姓名列
        excel_sheet_d.Paste(excel_sheet_d.Cells(2,ObligorName_index))
    else:
        print("未找到借款人的相关列内容")
    # if '*债务人姓名' in excel_sheet_dlist:
    #     print("存在")
    # else:
    #     print("不存在")
'''
def copy_BizSerialNumber(s_sheet,d_sheet,rows_s,excel_sheet_slist_1):
    #s_sheet委案方源文件表，d_sheet上传模板表，rows_s委案方源文件表共多少行，excel_sheet_slist_1是s_sheet部分列名
    # 获取序列号在列表中的位置，即在第几列
    pattern_serial1=re.compile('.*用户ID.*?')
    pattern_serial2 = re.compile('.*loanid.*?')
    pattern_serial3 = re.compile('.*借款编号.*?')
    pattern_serial4 = re.compile('.*案件编号.*?')
    flagserial=False
    for BizSerialNumber_index,serial in enumerate(excel_sheet_slist_1):
        if re.search(pattern_serial1,serial):
            flagserial = True
            print('BizSerialNumber所在列为：'+str(BizSerialNumber_index))
            # 复制源表序列内容
            s_sheet.Range(s_sheet.Cells(2, BizSerialNumber_index + 1),
                                s_sheet.Cells(rows_s, BizSerialNumber_index + 1)).Copy()
            # 粘贴模板表业务流水号列
            d_sheet.Paste(d_sheet.Cells(2,1))
            return BizSerialNumber_index
        elif re.search(pattern_serial2,serial):
            flagserial = True
            print('BizSerialNumber所在列为：' + str(BizSerialNumber_index))
            # 复制源表序列内容
            s_sheet.Range(s_sheet.Cells(2, BizSerialNumber_index + 1),
                          s_sheet.Cells(rows_s, BizSerialNumber_index + 1)).Copy()
            # 粘贴模板表业务流水号列
            d_sheet.Paste(d_sheet.Cells(2, 1))
            return BizSerialNumber_index
        elif re.search(pattern_serial3,serial):
            flagserial = True
            print('BizSerialNumber所在列为：' + str(BizSerialNumber_index))
            # 复制源表序列内容
            s_sheet.Range(s_sheet.Cells(2, BizSerialNumber_index + 1),
                          s_sheet.Cells(rows_s, BizSerialNumber_index + 1)).Copy()
            # 粘贴模板表业务流水号列
            d_sheet.Paste(d_sheet.Cells(2, 1))
            return BizSerialNumber_index
        elif re.search(pattern_serial4,serial):
            flagserial = True
            print('BizSerialNumber所在列为：' + str(BizSerialNumber_index))
            # 复制源表序列内容
            s_sheet.Range(s_sheet.Cells(2, BizSerialNumber_index + 1),
                          s_sheet.Cells(rows_s, BizSerialNumber_index + 1)).Copy()
            # 粘贴模板表业务流水号列
            d_sheet.Paste(d_sheet.Cells(2, 1))
            return BizSerialNumber_index
    if flagserial== False:
        print("业务流水号没有匹配项")
def copy_ObligorName(s_sheet,d_sheet,rows_s,excel_sheet_slist_1):
    # s_sheet委案方源文件表，d_sheet上传模板表，rows_s委案方源文件表共多少行，excel_sheet_slist_1是s_sheet部分列名
    # 获取债务人在列表中的位置，即在第几列
    pattern_ObligorName1=re.compile('.*姓名.*?')
    pattern_ObligorName2 = re.compile('.*借款人.*?')
    flagObligorName=False
    for ObligorName_index,ObligorName in enumerate(excel_sheet_slist_1):
        if re.search(pattern_ObligorName1,ObligorName):
            flagObligorName = True
            print("债务人姓名所在列为："+str(ObligorName_index))
            # 复制源表姓名列内容
            s_sheet.Range(s_sheet.Cells(2, ObligorName_index + 1),
                                s_sheet.Cells(rows_s, ObligorName_index + 1)).Copy()
            # 粘贴模板表债务人姓名列
            d_sheet.Paste(d_sheet.Cells(2,2))
            return  ObligorName_index
        elif re.search(pattern_ObligorName2,ObligorName):
            flagObligorName = True
            print("债务人姓名所在列为：" + str(ObligorName_index))
            # 复制源表姓名列内容
            s_sheet.Range(s_sheet.Cells(2, ObligorName_index + 1),
                          s_sheet.Cells(rows_s, ObligorName_index + 1)).Copy()
            # 粘贴模板表债务人姓名列
            d_sheet.Paste(d_sheet.Cells(2, 2))
            return ObligorName_index
    if flagObligorName==False:
        print("未找到借款人的相关列内容")
def copy_ObligorID(s_sheet,d_sheet,rows_s,excel_sheet_slist_1):
    #s_sheet委案方源文件表，d_sheet上传模板表，rows_s委案方源文件表共多少行，excel_sheet_slist_1是s_sheet部分列名
    # 获取序列号在列表中的位置，即在第几列
    pattern_ObligorID1=re.compile('.*身份证号.*?')
    flagObligorID=False
    for ObligorID_index,ObligorID in enumerate(excel_sheet_slist_1):
        if re.search(pattern_ObligorID1,ObligorID):
            flagObligorID = True
            print('ObligorID所在列为：'+str(ObligorID_index))
            # 复制源表序列内容
            s_sheet.Range(s_sheet.Cells(2, ObligorID_index + 1),
                                s_sheet.Cells(rows_s, ObligorID_index + 1)).Copy()
            # 粘贴模板表业务流水号列
            d_sheet.Paste(d_sheet.Cells(2,3))
            return ObligorID_index
    if flagObligorID==False:
        print("未找到身份证号码的相关列内容")
def copy_PhoneNumber(s_sheet,d_sheet,rows_s,excel_sheet_slist_1):
    #s_sheet委案方源文件表，d_sheet上传模板表，rows_s委案方源文件表共多少行，excel_sheet_slist_1是s_sheet部分列名
    #用正则表达式编译成re对象
    pattern1 = re.compile('.*手机号*?')
    pattern2= re.compile('.*联系电话*?')
    flagmatch = False
    #采用枚举的方式，获取手机号在列表中的位置
    for index,value in enumerate(excel_sheet_slist_1) :
        # 获取手机号在列表中的位置，即在第几列
        if re.search(pattern1, value):
            flagmatch = True
            # 复制源表序列内容
            s_sheet.Range(s_sheet.Cells(2, index + 1),
                          s_sheet.Cells(rows_s,index + 1)).Copy()
            # 粘贴模板表手机号列
            d_sheet.Paste(d_sheet.Cells(2, 4))
            return index
        elif re.search(pattern2, value):
            flagmatch = True
            s_sheet.Range(s_sheet.Cells(2, index + 1),
                          s_sheet.Cells(rows_s, index + 1)).Copy()
            # 粘贴模板表手机号列
            d_sheet.Paste(d_sheet.Cells(2, 4))
            return index
    if flagmatch == False:
        print("用户手机号没有匹配项")
def copy_RepaySum(s_sheet,d_sheet,rows_s,excel_sheet_slist):
    #s_sheet委案方源文件表，d_sheet上传模板表，rows_s委案方源文件表共多少行，excel_sheet_slist_1是s_sheet部分列名
    #用正则表达式编译成re对象
    pattern_RepaySum1 = re.compile('.*委案金额*?')
    pattern_RepaySum2= re.compile('.*应还金额*?')
    flagmatch = False
    #采用枚举的方式，获取委案金额在列表中的位置
    for RepaySum_index,RepaySum in enumerate(excel_sheet_slist) :
        # 获取委案金额在列表中的位置，即在第几列
        if re.search(pattern_RepaySum1,RepaySum):
            flagmatch = True
            print('委案金额所在列为：' + str(RepaySum_index))
            # 复制源表序列内容
            s_sheet.Range(s_sheet.Cells(2, RepaySum_index + 1),
                          s_sheet.Cells(rows_s,RepaySum_index + 1)).Copy()
            # 粘贴模板表委案金额列
            d_sheet.Paste(d_sheet.Cells(2, 5))
            return RepaySum_index
        elif re.search(pattern_RepaySum2,RepaySum):
            flagmatch = True
            print('委案金额所在列为：' + str(RepaySum_index))
            s_sheet.Range(s_sheet.Cells(2, RepaySum_index + 1),
                          s_sheet.Cells(rows_s, RepaySum_index  + 1)).Copy()
            # 粘贴模板表委案金额列
            d_sheet.Range("E2").PasteSpecial(Paste=win32com.client.constants.xlPasteValues)
            #d_sheet.Range("E2").PasteSpecial(Paste=-4163)
            return RepaySum_index
    if flagmatch == False:
        print("用户委案金额没有匹配项")
def copy_RepayDate(s_sheet,d_sheet,rows_s,excel_sheet_slist):
    #s_sheet委案方源文件表，d_sheet上传模板表，rows_s委案方源文件表共多少行，excel_sheet_slist_1是s_sheet部分列名
    #用正则表达式编译成re对象
    pattern_RepayDate1 = re.compile('.*逾期.*[时间|日期].*?')
    flagmatch = False
    #采用枚举的方式，获取逾期起始时间在列表中的位置
    for RepayDate_index,RepayDate in enumerate(excel_sheet_slist) :
        # 获取逾期起始时间在列表中的位置，即在第几列
        if re.search(pattern_RepayDate1,RepayDate):
            flagmatch = True
            # 复制源表序列内容
            s_sheet.Range(s_sheet.Cells(2, RepayDate_index + 1),
                          s_sheet.Cells(rows_s,RepayDate_index + 1)).Copy()
            # 粘贴模板表逾期起始时间列
            d_sheet.Paste(d_sheet.Cells(2, 6))
            return RepayDate_index
    if flagmatch == False:
        print("用户逾期起始时间没有匹配项")
def copy_RepayDateNumNum(s_sheet,d_sheet,rows_s,excel_sheet_slist):
    #s_sheet委案方源文件表，d_sheet上传模板表，rows_s委案方源文件表共多少行，excel_sheet_slist_1是s_sheet部分列名
    #用正则表达式编译成re对象
    pattern_RepayDateNum1 = re.compile('.*逾期天数.*?')
    flagmatch = False
    #采用枚举的方式，获取逾期天数在列表中的位置
    for RepayDateNum_index,RepayDateNum in enumerate(excel_sheet_slist) :
        # 获取逾期天数在列表中的位置，即在第几列
        if re.search(pattern_RepayDateNum1,RepayDateNum):
            flagmatch = True
            # 复制源表序列内容
            s_sheet.Range(s_sheet.Cells(2, RepayDateNum_index + 1),
                          s_sheet.Cells(rows_s,RepayDateNum_index + 1)).Copy()
            # 粘贴模板表逾期天数列
            d_sheet.Paste(d_sheet.Cells(2, 7))
            return RepayDateNum_index
    if flagmatch == False:
        print("用户逾期天数没有匹配项")
def copy_RepayDeadLineNum(s_sheet,d_sheet,rows_s,excel_sheet_slist):
    #s_sheet委案方源文件表，d_sheet上传模板表，rows_s委案方源文件表共多少行，excel_sheet_slist_1是s_sheet部分列名
    #用正则表达式编译成re对象
    pattern_RepayDeadLine1 = re.compile('.*委案截止[时间|日期].*?')
    flagmatch = False
    #采用枚举的方式，获取委案截止时间在列表中的位置
    for RepayDeadLine_index,RepayDeadLine in enumerate(excel_sheet_slist) :
        # 获取委案截止时间在列表中的位置，即在第几列
        if re.search(pattern_RepayDeadLine1,RepayDeadLine):
            flagmatch = True
            print('委案截止[时间|日期]所在列为：' + str(RepayDeadLine_index))
            # 复制源表序列内容
            s_sheet.Range(s_sheet.Cells(2, RepayDeadLine_index + 1),
                          s_sheet.Cells(rows_s,RepayDeadLine_index + 1)).Copy()
            # 粘贴模板表委案截止时间列
            d_sheet.Paste(d_sheet.Cells(2, 8))
            return RepayDeadLine_index
    if flagmatch == False:
        print("用户委案截止时间没有匹配项")
def test():
    test_list=['用户手1机号','手1机1号码','手1机联1系电话','联系电话']
    pattern1 = re.compile('.*手机号*?')
    pattern2 = re.compile('.*联系电话*?')
    flagmatch=False
    for index,value in enumerate(test_list) :
        if re.search(pattern1,value):
            print('索引index='+str(index)+"--值value="+value)
            print(re.search(pattern1,value).span())
            flagmatch = True
            return (index,value )
        elif re.search(pattern2,value):
            print('索引index=' + str(index) + "--值value=" + value)
            print(re.search(pattern2, value).span())
            flagmatch = True
            return index
    if flagmatch ==False:
        print("没有匹配项")

if __name__=='__main__':
    print("程序运行开始。。。")
    #excel_test()
    #excel_open()
    #excel_open1()
    #open_file()
    excel_new()
    # a=test()
    # print(a)
    print("运行结束。。。")
