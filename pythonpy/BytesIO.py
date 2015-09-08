#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import BytesIO

#write to BytesIO
f=BytesIO()
f.write(b'hello')
f.write(b' ')
f.write(b'world!')
print(f.getvalue())

# read from BytesIO
data='北京师范大学,\n脑与认知科学研究院,\n认知神经科学与学习国家重点实验室.'.encode('utf-8')
f=BytesIO(data)
print(f.read())
