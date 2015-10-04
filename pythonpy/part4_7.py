#第四部分习题
#part4_7 参数匹配
def f1(a,b):print('f1',a,b)
def f2(a,*b):print('f2',a,b)
def f3(a,**b):print('f3',a,b)
def f4(a,*b,**c):print('f4',a,b,c)
def f5(a,b=2,c=3):print('f5',a,b,c)
def f6(a,b=2,*c):print('f6',a,b,c)

f1(1,2)
f1(b=2,a=1)
f2(1,2,3)
f3(1,x=2,y=3)
f4(1,2,3,x=2,y=3)
f5(1)
f5(1,4)
f6(1)
f6(1,3,6)
