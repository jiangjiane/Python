#生成器函数vs生成器表达式
print('生成器表达式 ')
G=(c*4 for c in 'SPAM')
print(list(G),'\n')

def timesfour(s):
    for c in s:
        yield c*4
G=timesfour('spam')
print(list(G),'\n')

G=(c*4 for c in 'SPAM')
I=iter(G)
print(next(I))
