#! /usr/bin/python3 
# -*- coding: utf8 -*-
"""
xiti24_reloadall.py:transitively reload nested modules
自动重载模块及该模块导入的每个模块
"""
import types
from imp import reload

def status(module):
    print('reloading ' + module.__name__)

def transitive_reload(module,visited):
    if not module in visited:
        status(module)
        status(module)
        visited[module]=None
        for attrobj in module.__dict__.values():
            if type(attrobj)==types.ModuleType:
                transitive_reload(attrobj,visited)

def reload_all(*args):
    visited={}
    for arg in args:
        if type(arg)==types.ModuleType:
            transitive_reload(arg,visited)

if __name__=='__main__':
    import xiti24_reloadall
    reload_all(xiti24_reloadall)
