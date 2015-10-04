#第四部分习题
#xiti6 字典合并
def addDict(d1,d2):
    new={}
    for key in d1.keys():
        new[key]=d1[key]
    for key in d2.keys():
        new[key]=d2[key]
    return new

x={1:1}
y={1:1,2:2}
z=addDict(x,y)
print(z)
