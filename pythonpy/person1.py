#! /usr/bin/python3 
# -*- coding: utf8 -*-

class Person:
    def __init__(self,name,job=None,pay=0):
        self.name=name
        self.job=job
        self.pay=pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self,percent):
        self.pay=int(self.pay*(1+percent))
    def __str__(self):
        return '[Person:%s,%s]'%(self.name,self.pay)

class Manager:       #类的组合嵌套
    def __init__(self,name,pay):
        self.person=Person(name,'mgr',pay)
    """
    def giveRaise(self,percent,bonus=.10):
        self.pay=int(self.pay*(1+percent+bonus))
    """
    def giveRaise(self,percent,bonus=.10):
        self.person.giveRaise(percent+bonus)
    def __getattr__(self,attr):
        return getattr(self.person,attr)
    def __str__(self):
        return str(self.person)

if __name__=='__main__':
    bob=Person('Bon Smith')
    sue=Person('Sue Jones',job='dev',pay=100000)
    print(bob)#print(bob.name,bob.pay)
    print(sue)#print(sue.name,sue.pay)
    print(bob.lastName(),sue.lastName()) #print(bob.name.split()[-1])
    sue.giveRaise(.10)                   #sue.pay*=1.10
    print(sue)#print(sue.pay)
    tom=Manager('Tom Jones',50000)
    tom.giveRaise(.10)
    print(tom.lastName())
    print(tom)
    print('--All three--')
    for object in (bob,sue,tom):
        object.giveRaise(.10)
        print(object)
