#! /usr/bin/python3 
# -*- coding: utf8 -*-

class Super:
    def delegate(self):
        self.action()
    def action(self):
        assert False,'action must be defined!'
class Sub(Super):
    def action(self):
        print('spam')

x=Sub()
x.delegate()
