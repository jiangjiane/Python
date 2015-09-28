print('列表解析与map ')
print('输出spam的ASCII码 ')
res=[]
for x in 'spam':
    res.append(ord(x))
print(res,'\n')

print(list(map(ord,'spam')),'\n')
print([ord(x) for x in 'spam'],'\n')
print('0~10中x**2值 ')
print([x**2 for x in range(10)],'\n')
print(list(map((lambda x:x**2),range(10))),'\n')

#选出0~4中的偶数
print('选出0~4中的偶数 ')
print([x for x in range(5) if x%2==0],'\n')
print(list(filter((lambda x:x%2==0),range(5))),'\n')

#两个等效过程
print('两个等效过程 ')
print([x**2 for x in range(10) if x%2==0],'\n')
print(list(map((lambda x:x**2),filter((lambda x:x%2==0),range(10)))),'\n')
