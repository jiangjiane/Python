#第三部分习题
#第三题
D={'a':1,'b':2,'c':3,'d':4,'e':5}
print('origin D: ',D,'\n')

Ks=list(D.keys())
Ks.sort()
print('sort D: ')
for k in Ks:print(k,D[k])
print('\n')

print('sorted D: ')
ks=D.keys()
for k in sorted(ks):print(k,D[k])
print('\n')

for k in sorted(D):print(k,D[k])

