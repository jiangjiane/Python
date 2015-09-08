E=enumerate('spam')
I=iter(E)
print(next(I))
print(next(I))
print(list(enumerate('spam')))
print('\n')

L=[1,2,3,4,5]
for i in range(len(L)):
    L[i]+=10
print(L)
print('\n')

L=[x+10 for x in L]
print(L)
print('\n')

res=[]
for x in L:
    res.append(x+10)
print(res)
print('\n')
