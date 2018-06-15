
from functools import reduce
data = "This is a beauty"
data1=["aa",'','This','beauty']
# result = []
# for i in data:
#     if i.strip():
#         result.append(i)
#
# print(result)
# print(list(map(ord,result)))
a=list(filter(lambda x:x and x.strip(),data1))
print(a)
b=list(map(lambda x:x+"c"+str(1),a))
print(b)
c=list(reduce(lambda x,y:x+y,a,"start"))
print(c)
print(list(data))
print(range(2))
for i in range(2):
    print(i)

e = map(reduce(lambda x, y: x * y, range(1, 6)), range(1, 6))
print(e)

jiechenglist = []


for i in map(lambda x:x+1,range(6)):
    d = reduce(lambda x, y: x * y, map(lambda x:x+1,range(i)))
    jiechenglist.append(d)
print(str(jiechenglist))
f=reduce(lambda x, y: x + y,jiechenglist)
print(f)