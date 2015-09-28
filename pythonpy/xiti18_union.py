def intersect(*args):
    res=[]
    for x in args[0]:
        for other in args[1:]:
            if x not in other:break
            else:
                res.append(x)
    return res

def union(*args):
    res=[]
    for seq in args:
        for x in seq:
            if not x in res:
                res.append(x)
    return res

S1,S2,S3="SPAM","SCAM","SLAM"
print(intersect(S1,S2),union(S1,S2))
print(intersect([1,2,3],(1,4)))
print(intersect(S1,S2,S3))
print(union(S1,S2,S3))
