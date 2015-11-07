#! /usr/bin/python3 
# -*- coding: utf8 -*-

class Squares:
    def __init__(self,start,stop):
        self.value=start-1    # 这样可以显示出stop值
        self.stop=stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.value==self.stop:
            raise StopIteration
        self.value+=1         # 补回上文中减去的1 
        return self.value ** 2

for i in Squares(1,5):
    print(i,end=' ')
X=Squares(1,5)
I=iter(X)
next(I)
next(I)
next(I)
next(I)
next(I)
next(I)
