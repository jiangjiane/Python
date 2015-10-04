#第四部分习题
#part4_10
import sys,xiti20_mytimer1
reps=10000
repslist=range(reps)

from math import sqrt
def mathMod():
    for i in repslist:
        res=sqrt(i)
    return res

def powCall():
    for i in repslist:
        res=pow(i,.5)
    return res

def powExpr():
    for i in repslist:
        res=i**.5
    return res

print(sys.version)
for tester in (xiti20_mytimer1.timer,xiti20_mytimer1.best):
    print('<%s>' % tester.__name__)
    for test in (mathMod,powCall,powExpr):
        elapsed,result=tester(test)
        print('-'*35)
        print('%s:%.5f=>%s'%(test.__name__,elapsed,result))
