#! /usr/bin/python3 
# -*- coding: utf8 -*-

#命名空间例程
X=11
def f():
    print(X)
def g():
    X=22
    print(X)
class C:
    X=33
    def m(self):
        X=44
        self.X=55

if __name__=='__main__':
    print(X) # 11
    f() # 11
    g() # 22
    print(X) # 11 模块名未变
    obj=C()
    print(obj.X) # 33 类属性被实例继承

    obj.m()
    print(obj.X) # 55 实例
    print(C.X) # 33 类

    # print(C.m.X) False 仅仅在方法里可见
    # print(g.X)   False 仅仅在函数里可见 只有当函数调用或方法执行时才存在于内存中
