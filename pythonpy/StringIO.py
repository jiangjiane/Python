#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import StringIO

# write to StringIO
f=StringIO()
f.write('hello')
f.write(' ')
f.write('world')
print(f.getvalue())

# read from StringIO
f=StringIO('北京师范大学,\n脑与认知科学研究院,\n认知神经科学与学习国家重点实验室.')# '...室.\n '
while True:
    s=f.readline()
    if s=='':# s==' '
        break
    print(s.strip())
