print(set(open('/home/jianjiang/Python/pythonpy/enroll.py')))
print('\n')

print({line for line in open('/home/jianjiang/Python/pythonpy/enroll.py')})
print('\n')

print({ix:line for ix,line in enumerate(open('/home/jianjiang/Python/pythonpy/enroll.py'))})
print('\n')

print({line for line in open('/home/jianjiang/Python/pythonpy/enroll.py') if line[0]=='p'})
print('\n')

print({ix:line for ix,line in enumerate(open('/home/jianjiang/Python/pythonpy/enroll.py')) if line[0]=='p'})
print('\n')

x=(1,2)
y=(3,4)
print(list(zip(x,y)))
A,B=zip(*zip(x,y))
print(A),print(B)
print('\n')
