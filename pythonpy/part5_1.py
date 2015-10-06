#! /usr/bin/python3 
# -*- coding: utf8 -*-
#第五部分习题 xiti1_1
def countLines(name):
    file=open(name)
    return len(file.readlines())

def countChars(name):
    return len(open(name).read())

def test(name):
    return countLines(name),countChars(name)
