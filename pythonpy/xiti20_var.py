#打印全局变量，并在之后设置一个有着相同变量名的本地变量
x=99
def selector():
    import __main__   #导入上层模块，并使用模块的属性标记来获得其全局变量
    print(__main__.x)
    x=88
    print(x)
    
selector()
