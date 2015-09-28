#参数实例
def f(a,b,c):print(a,b,c)
print('位置参数f(1,2,3): ')
f(1,2,3)
print('关键字参数f(c=3,a=1,b=2): ')
f(c=3,a=1,b=2)
print('\n')

#默认参数
print('默认参数 ')
def f(a,b=2,c=3):print(a,b,c)
f(1),f(a=1),f(1,4),f(1,4,5),f(1,c=6)
print('\n')

#收集参数
print('收集参数 ')
def f(a,*pargs,**kargs):print(a,pargs,kargs)
f(1,2,3,x=1,y=2)
print('\n')

#解包参数
print('解包参数1 ')
def func(a,b,c,d):print(a,b,c,d)
args=(1,2)
args+=(3,4)
func(*args)
print('\n')
args={'a':1,'b':2,'c':3}
args['d']=4
func(**args)
print('\n')
print('解包参数2 ')
func(*(1,2),**{'d':4,'c':4})
func(1,*(2,3),**{'d':4})
func(1,c=3,*(2,),**{'d':4})
func(1,*(2,3),d=4)
func(1,*(2,),c=3,**{'d':4})
print('\n')

def tracer(func,*pargs,**kargs):
    print('calling:',func.__name__)
    rerurn func(*pargs,**kargs)
def func(a,b,c,d):
    return a+b+c+d
print(tracer(func,1,2,c=3,d=4))
