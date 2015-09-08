print([x+y for x in 'abc' for y in 'lmn'])
print('\n')

res=[]
for x in 'abc':
    for y in 'lmn':
        res.append(x+y)
print(res)
print('\n')

x=[1,2,3]
y=[4,5,6]
z=[7,8,9]
xyz=zip(x,y,z)
print(list(xyz))
u=zip(*xyz)
print(list(u))
