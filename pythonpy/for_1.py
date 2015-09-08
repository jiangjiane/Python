D={'a':1,'b':2,'c':3}
for key in D:
    print(key,'=>',D[key])
print("\n")

list(D.items())
print("\n")

for (key,value) in D.items():
    print(key,'=>',value)
print("\n")

for ((a,b),c) in [((1,2),3),((4,5),6)]:print(a,b,c)
print("\n")

for ((a,b),c) in [([1,2],3),['XY',6]]:print(a,b,c)
print("\n")

a,*b,c=(1,2,3,4)
print(a,b,c)
print("\n")

for (a,*b,c) in [(1,2,3,4),(5,6,7,8)]:
    print(a,b,c)
print("\n")

for all in [(1,2,3,4),(5,6,7,8)]:
    a,b,c=all[0],all[1:3],all[3]
    print(a,b,c)
print("\n")

items=["aaa",111,(4,5),2.01]
tests=[(4,5),3.14]
for key in tests:
    for item in items:
        print(key,"was found")
        break         #内循环找到之后就进入下一次外循环
    else:
        print(key,"not found!")
print("\n")

for key in tests:
    if key in items:
        print(key,"was found")
    else:
        print(key,"not found!")
print("\n")
