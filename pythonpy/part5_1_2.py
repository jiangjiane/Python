#! /usr/bin/python3 
# -*- coding: utf8 -*-
#第五部分习题 xiti1_3 运用seek()
def countLines(file):
    file.seek(0)
    return len(file.readlines())

def countChars(file):
    file.seek(0)
    return len(file.read())

def test(name):
    file=open(name)
    return countLines(file),countChars(file)

if __name__=='__main__':
    print(test('part5_1_2.py'))

"""
if __name__=='__main__':
    print(test(input('Enter file name:'))
or
if __name__=='__main__':
    import sys
    print(test(sys.argv[1]))
"""
