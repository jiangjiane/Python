#使用类的状态
class tester:
    def __init__(self,start):
        self.state=start
    def nested(self,label):
        print(label,self.state)
        self.state+=1

F=tester(0)
F.nested('spam')
F.nested('ham')
G=tester(42)
G.nested('toast')
G.nested('bacon')
F.nested('eggs')
print(F.state)
print('\n')

class tester:
    def __init__(self,start):
        self.state=start
    def __call__(self,label):
        print(label,self.state)
        self.state+=1

H=tester(99)
H('juice')
H('pancakes')
print('\n')

#使用函数属性的状态
def tester(start):
    def nested(label):
        print(label,nested.state)
        nested.state+=1
    nested.state=start
    return nested

F=tester(0)
F('spam')
F('ham')
print(F.state)
G=tester(42)
G('eggs')
F('ham')
