#第四部分习题
#part4_9
#values=[2,4,9,16,25]
import math
res=[]
for x in [2,4,9,16,25]:  #values      
    res.append(math.sqrt(x))
print('for_sqrt实现',res)

print('map_sqrt实现',list(map(math.sqrt,[2,4,9,16,25])))

print('列表解析_map实现',[math.sqrt(x) for x in [2,4,9,16,25]])
