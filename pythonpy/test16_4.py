print('嵌套作用域举例 1')
x=99

def f1():
    x=88
    def f2():
        print(x)
    f2()

f1()
print('\n')

print('嵌套作用域举例 2')
def f1():
    x=88
    def f2():
        print(x)
    return f2

action=f1()
action()
print('\n')
