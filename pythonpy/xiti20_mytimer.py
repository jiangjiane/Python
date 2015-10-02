#对模块计时
import time
reps=1000
repslist=range(reps)

def timer(func,*args,**kargs):
    start=time.clock()
    for i in repslist:
        ret=func(*args,**kargs)
    elapsed=time.clock()-start
    return (elapsed,ret)
