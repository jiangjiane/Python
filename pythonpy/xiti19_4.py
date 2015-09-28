#lambda函数
print('lambda用法1 ')
def knights():
    title='Sir'
    action=(lambda x:title + ' ' +x)
    return action

act=knights()
print(act('robin'))
print('\n')

print('lambda用法2 ')
L=[lambda x:x**2,
   lambda x:x**3,
   lambda x:x**4]
for f in L:
    print(f(2))
print(L[0](3))
print('\n')

print('2的等效def写法 ')
def f1(x):return x**2
def f2(x):return x**3
def f3(x):return x**4
L=[f1,f2,f3]
for f in L:
    print(f(2))
print(L[0](3))
