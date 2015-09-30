#map(func,seqs...)
print('自己的map函数,无自动填充型 ')
print('for and list实现')
def mymap1(func,*seqs):
    res=[]
    for args in zip(*seqs):
        res.append(func(*args))
    return res
print(mymap1(abs,[-2,-1,0,1,2]))
print(mymap1(pow,[1,2,3],[2,3,4,5]),'\n')

print('列表解析实现 ')
def mymap2(func,*seqs):
    return (func(*args) for args in zip(*seqs))
print(list(mymap2(abs,[-2,-1,0,1,2])))
print(list(mymap2(pow,[1,2,3],[2,3,4,5])),'\n')

print('迭代器运用实现 ')
def mymap3(func,*seqs):
    #res=[]
    for args in zip(*seqs):
        yield func(*args)
print(list(mymap3(abs,[-2,-1,0,1,2])))
print(list(mymap3(pow,[1,2,3],[2,3,4,5])),'\n')
