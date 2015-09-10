#第三部分习题
#第一题
S='spam'
for x in S:
    print('ASCII of %s is %d'%(x,ord(x)))
print('\n')

sum=0
for y in S:
    sum+=ord(y)
print('sum of ASCIIs:')
print('sum=',sum)
print('\n')

L=[]
for z in S:
    L.append(ord(z))
print(L)
print('\n')

S='spam'
print(list(map(ord,S)))

