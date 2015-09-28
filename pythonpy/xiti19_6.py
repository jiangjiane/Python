#在序列中映射函数 map、filter和reduce
print('map ')
counters=[1,2,3,4]
updated=[]
for x in counters:
    updated.append(x+10)

print(updated)
print('\n')

def inc(x):return x+10
print(list(map(inc,counters)),'\n')
#print('\n')
print(list(map((lambda x:x+3),counters)),'\n')

print('mymap ')
def mymap(func,seq):
    res=[]
    for x in seq:res.append(func(x))
    return res
print(mymap(inc,[1,2,3]),'\n')

print('filter ')
print(list(filter((lambda x:x>0),range(-5,5))),'\n')
#等效替代
res=[]
for x in range(-5,5):
    if x>0:
        res.append(x)
print(res,'\n')

print('reduce ')
from functools import reduce
print(reduce((lambda x,y:x+y),[1,2,3,4]))
print(reduce((lambda x,y:x*y),[1,2,3,4]),'\n')

#reduce for等效
print('for等效 ')
L=[1,2,3,4]
#res=L[0]
sum=0
for x in L:#[1:]:
    sum+=x
print(sum,'\n')

print('myreduce ')
def myreduce(function,sequence):
    tally=sequence[0]
    for next in sequence[1:]:
        tally=function(tally,next)
    return tally
print(myreduce((lambda x,y:x+y),[1,2,3,4,5]),'\n')
print(myreduce((lambda x,y:x*y),[1,2,3,4,5]),'\n')
