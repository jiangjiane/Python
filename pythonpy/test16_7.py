#nonlocal应用
def tester(start):
    state=start
    def nested(label):
        print(label,state)
    return nested

F=tester(0)
F('spam')
F('ham')
print('\n')

#默认情况下，不允许修改嵌套的def作用域中的名称
def tester(start):
    state=start
    def nested(label):
        print(label,state)
        state+=1
    return nested

F=tester(0)
F('spam')
print('\n')

#默认情况下，不允许修改嵌套的def作用域中的名称，现使用nonlocal进行修改
def tester(start):
    state=start
    def nested(label):
        nonlocal state
        print(label,state)
        state+=1
    return nested

F=tester(0)
F('spam')
F('ham')
F('eggs')
print('\n')

G=tester(42)
G('spam')
G('eggs')
G('bacon')
print('\n')

