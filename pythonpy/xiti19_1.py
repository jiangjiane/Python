#递归函数
print('递归函数 ')
def mysum(L):
    if not L:
        return 0
    else:
        return L[0]+mysum(L[1:])

print(mysum([1,2,3,4,5]))
print('\n')

print('执行过程 ')
def mysum(L):
    print(L)
    if not L:
        return 0
    else:
        return L[0]+mysum(L[1:])

print(mysum([1,2,3,4,5]))
print('\n')

print('编码替代 ')
def mysum(L):
    return 0 if not L else L[0]+mysum(L[1:])
print(mysum([1]))
print(mysum([1,2,3,4,5]))
def mysum(L):
    return L[0] if len(L)==1 else L[0]+mysum(L[1:])
print(mysum(('s','p','a','m')))
def mysum(L):
    first,*rest=L
    return first if not rest else first +mysum(rest)
print(mysum(['spam','ham','eggs']))
print('\n')

print('相互调用 ')
def mysum(L):
    if not L:return 0
    return nonempty(L)
def nonempty(L):
    return L[0]+mysum(L[1:])
print(mysum([1.1,2.2,3.3,4.4]))
