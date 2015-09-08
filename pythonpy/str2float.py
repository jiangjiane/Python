#_*_ coding:utf-8 _*_

from functools import reduce
def str2float(s):
    return reduce(lambda x,y:x+0.001*y,map(int,s.split('.')))
