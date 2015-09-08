#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Myobject(object):
    def __init__(self):
        self.x=9

    def power(self):
        return self.x*self.x

obj=Myobject()

print('hasattr(obj,\'x\')=',hasattr(obj,'x'))#是否有属性'x'
print('hasattr(obj,\'y\')=',hasattr(obj,'y'))#是否有属性'y'
setattr(obj,'y',19)# 设置属性'y'
print('hasattr(obj,\'y\')=',hasattr(obj,'y'))#是否有属性'y'
print('getattr(obj,\'y\')=',getattr(obj,'y'))#获取属性'y'
print('obj.y=',obj.y)#获取属性'y'

print('getattr(obj,\'z\')=',getattr(obj,'z',404))#获取属性'z'，若不存在，则返回值404

f=getattr(obj,'power')#获取属性‘power’
print(f)
print(f())
