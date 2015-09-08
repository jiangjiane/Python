seq1="spam"
seq2="scam"
res=[]
for x in seq1:
    if x in seq2:
        res.append(x)
print(res)
print("\n")

print(list(range(5)),list(range(2,5)),list(range(0,10,2)))
print(list(range(-5,5)))
print(list(range(5,-5,-1)))
print("\n")

for i in range(3):
    print(i,"Python")
print("\n")

x='spam'
for item in x:print(item,end=' ')
print("\n")

i=0
while i<len(x):
    print(x[i],end=' ')
    i+=1
print("\n")
        
