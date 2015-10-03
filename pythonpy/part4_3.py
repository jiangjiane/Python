#第四部分习题
#xiti3
def adder1(*args):
    print('adder1',end=' ')
    if type(args[0])==type(0): #手动测试类型，看是否为整数
        sum=0   #若为整数，sum初始值为0
    else:
        sum=args[0][:0] #若不是整数，第一个参数的空分片为初始值
    for arg in args:
        sum+=arg
    return sum

def adder2(*args):
    print('adder2',end=' ')
    sum=args[0]
    for next in args[1:]:
        sum+=next
    return sum

for func in (adder1,adder2):
    print(func(2,3,4))
    print(func('spam','eggs','toast'))
    print(func(['a','b'],['c','d'],['e','f']))
    
