#! /usr/bin/python3 
# -*- coding: utf8 -*-

import person
bob=person.Person(...)

from person import Person
bob=Person(...)

from person import Person,Manager
bob=Person('Bob Smith')
sue=Person('Sue Jones',job='dev',pay=100000)
tom=Manager('Tom Jones',50000)

import shelve
db=shelve.open('persondb')
for object in (bob,sue,tom):
    db[object.name]=object
db.close()

