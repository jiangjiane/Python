#第三部分习题
#第四题
L=[1,2,4,8,16,32,64]
X=5

found=False
i=0
while not found and i<len(L):
    if 2**X==L[i]:
        found=True
        print('at index',i)
    else:
        i=i+1
        print(X,'not found')


i=0
while 2**X==L[i] and i<len(L):
    print('at index',i)
    i=i+1
else:
    print(X,'not found')
