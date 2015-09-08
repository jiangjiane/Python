#-*- coding:utf-8 -*-

class Screen(object):
    def __init__(self):
        self.__width=1024
        self.__height=768
        self.resolution=1024*768

@property
def width(self):
    return self.__width

@width.setter
def width(self,value):
    self.__width=value

@property
def height(self):
    return self.__height

@height.setter
def height(self,value):
    sellf.__height=value

@property
def resolution(self):
    return self.__resolution


#test
s=Screen()
s.width=1024
s.height=768
print(s.resolution)
assert s.resolution==786432,'1024*768=%d?'%s.resolution
