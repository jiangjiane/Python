#第四部分习题
#xiti5 字典复制
def copyDict(old):
    new={}
    for key in old.keys():
        new[key]=old[key]
    return new
d={1:1,2:2}
e=copyDict(d)
d[2]='?'
print('d=',d)
print('e=',e)
