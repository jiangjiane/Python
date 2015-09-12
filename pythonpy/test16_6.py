def func():
    x=4
    action=(lambda n:x**n)
    return action

x=func()
print(x(2))
print(x(3))
print('\n')

def func():
    x=4
    action=(lambda n,x=x:x**n)
    return action

x=func()
print(x(2))
print(x(3))
print('\n')

#变量在嵌套的函数被调用时才进行查找，所以结果是同样的值
def makeActions():
    acts=[]
    for i in range(5):
        acts.append(lambda x:i**x)
    return acts

acts=makeActions()
print(acts[0](2))
print(acts[2](2))
print(acts[4](2))
print(acts[1](3))
print('\n')

#使用默认参数把当前的值传递给嵌套作用域的变量
def makeActions():
    acts=[]
    for i in range(5):
        acts.append(lambda x,i=i:i**x)
    return acts

acts=makeActions()
print(acts[0](2))
print(acts[2](2))
print(acts[4](2))
print(acts[4](3))
print('\n')

#任意嵌套
def f1():
    x=99
    def f2():
        def f3():
            print(x)
        f3()
    f2()

f1()
