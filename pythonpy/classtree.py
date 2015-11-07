#! /usr/bin/python3 
# -*- coding: utf8 -*-

#用属性来显示类树
def classtree(cls,indent):
    print('.'*indent+cls.__name__)  # 打印类名
    for supercls in cls.__bases__:  # 遍历所有的超类
        classtree(supercls,indent+3)# 向上搜索

def instancetree(inst):
    print('Tree of %s' % inst)  #显示实例
    classtree(inst.__class__,3)

def selftest():
    class A:        pass
    class B(A):     pass
    class C(A):     pass
    class D(B,C):   pass
    class E:        pass
    class F(D,E):   pass
    instancetree(B())
    instancetree(F())

if __name__=='__main__':selftest()
