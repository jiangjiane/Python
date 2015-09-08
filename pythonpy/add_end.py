#def add_end(L=[]):
    #定义默认参数时其必须指向不变对象
    #应修改为add_end(L=None)
#   L.append('END')
#   return L

def add_end(L=None):
    if L is None:
        L=[]
    L.append('END')
    return L
