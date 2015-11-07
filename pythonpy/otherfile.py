#! /usr/bin/python3 
# -*- coding: utf8 -*-

#文件manynames.py的补充文件
import manynames
X=66
print(X)
print(manynames.X)

manynames.f()
manynames.g()

print(manynames.C.X)
I=manynames.C()
print(I.X)
I.m()
print(I.X)
