def intersect(seq1,seq2):
    res=[]
    for x in seq1:
        if x in seq2:
            res.append(x)
    
    
    print([x for x in s1 if x in s2])
    return res
