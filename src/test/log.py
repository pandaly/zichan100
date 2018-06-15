import  logging
# logging.debug('debug message')
# logging.warning('warning message')
# logging.info('info messgage')
# logging.error('error messgage')
# logging.exception('exception message')
# print(dir(logging))
# def foo(ip,port):
#     print("%s+++%d" %(ip,port))
# foo('192.168.1.20',90)
# foo(port=23,ip='192.168.3.65')
# def log1(arg1,arg2,*tuple,**dict):
#     print('arg1='+arg1,'arg2='+arg2,'*tuple='+tuple.__str__())
#     for i,item in enumerate(tuple):
#         print('%d----%s' %(i,item))
#     for key in dict:
#         print(key)
#log1('123')
mytuple=('aa','bb',('d','e'))
# mytuple1=('aa','bb',('d','e'))
mydict={'key1':1,'key2':12312,'key3':'jejjeje'}
# mydict1={'key4':1,'key5':12312,'key6':'jejjeje'}
# log1(str(123),'qweqw',*mytuple,*mytuple1,**mydict,**mydict1)

list1 =['a','b','c','d']
# print(abs(-12))
# f=abs
# print(f)
# print(f(-5))
#
# def f(x):
#     return x+x
# map(f,list1)
# print(list(map(f,list1)))
# print(map(f,list1))

# def closepack(*mytuple,**mydict):
#     print('闭包函数测试。。。。')
#     def log2(arg1, arg2, *tuple, **dict):
#         print('arg1=' + arg1, 'arg2=' + arg2, '*tuple=' + tuple.__str__())
#         for i, item in enumerate(tuple):
#             print('%d----%s' % (i, item))
#         for key in dict:
#             print(key)
#     return  log2
# result1=closepack(*mytuple,**mydict)
# print(result1)
# result1(*mytuple,**mydict)
def dec(fun):
    def wrapper(*mytuple,**mydict):
        print('装饰器进行中。。')
        return fun(*mytuple,**mydict)
    return wrapper
@dec
def log3(arg1, arg2, *tuple, **dict):
    print('arg1=' + arg1, 'arg2=' + arg2, '*tuple=' + tuple.__str__())
    for i, item in enumerate(tuple):
        print('%d----%s' % (i, item))
    for key in dict:
        print(key)
log3(*mytuple,**mydict)
