#yield用法
print('yield用法 ')
def gensquares(N):
    for i in range(N):
        yield i**2
for i in gensquares(5):
    print(i,end=' : ')
print('\n')

print('例1 ')
def addlist(alist):
    for i in alist:
        yield i+1
alist=[1,2,3,4]
for x in addlist(alist):
    print(x)
print('\n')

print('例2 ')
def h():
    print('Wen Chuan\n')
    yield 5
    print('Fighting!')
c=h()
c.__next__()

print('send(msg)与next()用法 ')
def h():
    print('Wen Chuan',end=' ')
    m=yield 5 #Fighting!
    print(m)
    d=yield 12
    print('We are together!')
c=h()
c.__next__() #相当于c.send(None)
c.send('Fighting!')#(yield 5)表达式被赋予了'Fighting!'
