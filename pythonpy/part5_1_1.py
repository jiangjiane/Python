#! /usr/bin/python3 
# -*- coding: utf8 -*-
#第五部分习题 xiti1_2
def countLines(name):
    tot=0
    for line in open(name):
        tot+=1
    return tot

def countChars(name):
    tot=0
    for line in open(name):
        tot+=len(line)
    return tot

def test(name):
    return countLines(name),countChars(name)
