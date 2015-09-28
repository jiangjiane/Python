#习题1
print('习题1 ')
def func(a,b=4,c=5):
    print(a,b,c)

func(1,2)
print('\n')

#习题2
print('习题2 ')
def func(a,b,c=5):
    print(a,b,c)

func(1,c=3,b=2)
print('\n')

#习题3
print('习题3 ')
def func(a,*pargs):
    print(a,pargs)

func(1,2,3)
print('\n')

#习题4
print('习题4 ')
def func(a,**kargs):
    print(a,kargs)

func(a=1,c=3,b=2)
print('\n')

#习题5
print('习题5 ')
def func(a,b,c=3,d=4):
    print(a,b,c,d)

func(1,*(5,6))
print('\n')
