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
    print('Wen Chuan')
    yield 5
    print('Fighting!')
c=h()
c.__next__()
