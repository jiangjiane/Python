#列表解析和矩阵
print('列表解析和矩阵 ')
M=[[1,2,3],
   [4,5,6],
   [7,8,9]]
N=[[2,2,2],
   [3,3,3],
   [4,4,4]]
print('取行\n',M[1])  #取行
print(' ',M[1][2],'\n')
print('取列\n',[row[1] for row in M],'\n')  #取列
print('等效取列\n',[M[row][1] for row in (0,1,2)],'\n')#等效取行,其中(0,1,2)==[0,1,2]
print('取主轴元素\n',[M[i][i] for i in range(3)],'\n')#or range(len(M))
print('M.*N\n',[M[row][col]*N[row][col] for row in range(len(M)) for col in range(3)],'\n')
print('M.*N\n',[[M[row][col]*N[row][col] for col in range(len(M))] for row in range(3)],'\n')

#上两式等效for表达
res=[]
for row in range(3):
    for col in range(3):
        res.append(M[row][col]*N[row][col])
print('上两式等效for表达结果\n',res,'\n')
res=[]
for row in range(3):
    tmp=[]
    for col in range(3):
        tmp.append(M[row][col]*N[row][col])
    res.append(tmp)
print(res,'\n')
