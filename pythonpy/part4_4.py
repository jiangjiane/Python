#第四部分习题
#xiti4
def adder(good=1,bad=2,ugly=3):
    return good+bad+ugly

print(adder())
print(adder(5))
print(adder(5,6))
print(adder(5,6,7))
print(adder(ugly=7,good=6,bad=5),'\n')

def adder1(*args):
    tot=args[0]
    for arg in args[1:]:
        tot+=arg
    return tot

def adder2(**args):
    argskeys=list(args.keys()) #按关键字遍历
    tot=args[argskeys[0]]
    for key in argskeys[1:]:
        tot+=args[key]
    return tot

def adder3(**args):
    args=list(args.values()) #按值遍历
    tot=args[0]
    for arg in args[1:]:
        tot+=arg
    return tot

def adder4(**args):
    return adder1(*args.values()) #利用adder1按值遍历

print(adder1(1,2,3),adder1('aa','bb','cc'))
print(adder2(a=1,b=2,c=3),adder2(a='aa',b='bb',c='cc'))
print(adder3(a=1,b=2,c=3),adder3(a='aa',b='bb',c='cc'))
print(adder4(a=1,b=2,c=3),adder4(a='aa',b='bb',c='cc'))
