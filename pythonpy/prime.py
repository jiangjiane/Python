y=int(input('Please enter a number:'))
x=y//2   # 运算符//的左右都得是整数
while x>1:
    if y % x ==0:
        print(y,'has factor',x)
        break
    x-=1
else:
    print(y,'is prime')
