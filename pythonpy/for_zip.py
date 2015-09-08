L1=[1,2,3,4]
L2=[5,6,7,8]
print(list(zip(L1,L2)))
print("\n")

for (x,y) in zip(L1,L2):
    print(x,y,'--',x+y)
print("\n")

keys=['spam','eggs','toast']
vals=[1,3,5]
print(list(zip(keys,vals)))
print("\n")

D2={}
for (k,v) in zip(keys,vals):D2[k]=v
print(D2)
print("\n")

D3=dict(zip(keys,vals))
print(D3)
print("\n")
