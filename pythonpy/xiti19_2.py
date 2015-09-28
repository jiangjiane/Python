#循环语句VS递归
print('循环语句VS递归while ')
L=[1,2,3,4,5]
sum=0
while L:
    sum+=L[0]
    L=L[1:]
print('sum=',sum)

print('循环语句VS递归for ')
L=[1,2,3,4,5]
sum=0
for x in L:sum+=x
print('sum=',sum)
