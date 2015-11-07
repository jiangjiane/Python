#! /usr/bin/python3 
# -*- coding: utf8 -*-

#例1
class MixedNames:
    data='spam'
    def __init__(self,value):
        self.data=value
    def display(self):
        print(self.data,MixedNames.data)

print('-----例1-----')
x=MixedNames(1)
y=MixedNames(2)
x.display()
y.display()

#例2
class NextClass:
    def printer(self,text):
        self.message=text
        print(self.message)

print('-----例2-----')    
x=NextClass()
x.printer('instance call')
print(x.message)

#例3
class Super:
    def method(slef):
        print('in Super.method')
class Sub(Super):
    def method(self):
        print('starting Sub.method')
        Super.method(self)
        print('ending Sub.method')

print('-----例3-----')
x=Super()
x.method()
x=Sub()
x.method()
