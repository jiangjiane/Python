S='spam'
offset=0
for item in S:
    print(item,'appears at offset',offset)
    offset+=1
print("\n")

for (offset,item) in enumerate(S):
    print(item,'appears at offset',offset)
print("\n")
