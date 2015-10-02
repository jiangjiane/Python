from xiti20_mytimer2 import timer,best

def power(x,y):return X**y
timer(power,2,32)
timer(power,2,32,_reps=1000000)
timer(power,2,100000)[0]

best(power,2,32)
best(power,2,100000,_reps=500)[0]
best(power,2,100000)[0]
