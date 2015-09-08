f=open('/home/jianjiang/Python/pythonpy/for_iter.py')
lines=f.readlines()
print(lines)
print('\n')

lines=[line.rstrip() for line in lines]
print(lines)
print('\n')

print([line.upper() for line in open('/home/jianjiang/Python/pythonpy/for_iter.py')])
print('\n')
print([line.rstrip().upper() for line in open('/home/jianjiang/Python/pythonpy/for_iter.py')])
print('\n')
print([line.split() for line in open('/home/jianjiang/Python/pythonpy/for_iter.py')])
print('\n')
print([line.replace(',','!') for line in open('/home/jianjiang/Python/pythonpy/for_iter.py')])
print('\n')
print([('D' in line,line[0]) for line in open('/home/jianjiang/Python/pythonpy/for_iter.py')])
print('\n')

#用if限定提取特殊句子如下为提取‘p'开头句子 
print([line.rstrip() for line in open('/home/jianjiang/Python/pythonpy/for_iter.py') if line[0]=='p'])
print('\n')
#将上句改写为for循环句式
res=[]
for line in open('/home/jianjiang/Python/pythonpy/for_iter.py'):
    if line[0]=='p':
        res.append(line.rstrip())
print(res)
print('\n')
