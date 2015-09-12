#工厂函数
print('工厂函数举例：')
def maker(N):
    def action(X):
        return X**N
    return action

def f1():
    x=88
    def f2(x=x):
        print(x)
    f2()

f1()

def f1():
    x=88
    f2(x)
def f2(x):
    print(x)

f1()
