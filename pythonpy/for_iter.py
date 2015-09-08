D={'a':1,'b':2,'c':3}
for key in D.keys():
    print(key,D[key])
print('\n')

I=iter(D)
print(next(I))
print(next(I))
print(next(I))
print('\n')

f=open('/home/jianjiang/Python/pythonpy/do_iter.py')
print(next(f))
print(next(f))
print(next(f))

