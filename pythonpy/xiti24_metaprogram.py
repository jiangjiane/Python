#! /usr/bin/python3 
# -*- coding: utf8 -*-
#提取模块属性
seplen=60
sepchr='-'
def listing(module,verbose=True):
    sepline=sepchr*seplen
    if verbose:
        print(sepline)
        print('name:',module.__name__,'file:',module.__file__)
        print(sepline)

    count=0
    for attr in module.__dict__:        #scan namespace keys
        print('%02d)%s'%(count,attr),end=' ')
        if attr.startswith('__'):
            print('<built-in name>')    #skip__file__,etc
        else:
            print(getattr(module,attr)) #same as .__dict__[attr]
        count +=1

    if verbose:
        print(sepline)
        print(module.__name__,'has %d names'%count)
        print(sepline)

if __name__=='__main__':
    import xiti24_metaprogram
    listing(xiti24_metaprogram)   #self-test code
