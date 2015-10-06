#! /usr/bin/python3 
# -*- coding: utf8 -*-
class FirstClass:
    def setdata(self,value):
        self.data=value
    def display(self):
        print(self.data)

x=FirstClass()
y=FirstClass()
x.setdata("King Arthur")
y.setdata(3.14159)
x.display()
y.display()
x.data="New value"
x.display()
