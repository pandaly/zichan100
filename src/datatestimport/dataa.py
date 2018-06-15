#coding:utf-8
import pymysql
from openpyxl.workbook import Workbook
import pandas as pd

db=pymysql.Connect(host='zc100testo.mysql.rds.aliyuncs.com',port=3306,user='dbowner',passwd='!!!abc123',db='assetsv2_test_import',charset='utf8')#连接数据库
cur=db.cursor()#创建游标
sql="""SELECT s.CaseId,i.DebtTotal,i.ObligorIdentityCard,s.OwnerName,s.AgentName,ro.RepaySum
from biz_case_status s LEFT JOIN biz_case_info i ON s.CaseId=i.CaseId
LEFT JOIN biz_case_repay_owner ro ON s.CaseId=ro.CaseId limit 1000"""

dataframe=pd.read_sql(sql,db)
dataframe.to_sql('data',db,if_exists='append')