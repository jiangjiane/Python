#map(func,seqs...)
print('自己的map函数,有自动填充型 ')
print('myzip and mymapPad ')
def myzip(*seqs):
    seqs=[list(S) for S in seqs]
    res=[]
    while all(seqs):
        res.append(tuple(S.pop(0) for S in seqs))
    return res

def mymapPad(*seqs,pad=None):
    seqs=[list(S) for S in seqs]
    res=[]
    while any(seqs):
        res.append(tuple((S.pop(0) if S else pad) for S in seqs))
    return res

S1,S2='abc','xyz123'
print(myzip(S1,S2))
print(mymapPad(S1,S2))
print(mymapPad(S1,S2,pad=99),'\n')

print('myzip_yield and mymapPad_yield ')
def myzip(*seqs):
    seqs=[list(S) for S in seqs]
    while all(seqs):
        yield tuple(S.pop(0) for S in seqs)
def mymapPad(*seqs,pad=None):
    seqs=[list(S) for S in seqs]
    while any(seqs):
        yield tuple((S.pop(0) if S else pad) for S in seqs)

S1,S2='abc','xyz123'
print(list(myzip(S1,S2)))
print(list(mymapPad(S1,S2)))
print(list(mymapPad(S1,S2,pad=99)),'\n')

print('myzip_len and mymapPad_len ')
def myzip(*seqs):
    minlen=min(len(S) for S in seqs)
    return [tuple(S[i] for S in seqs) for i in range(minlen)]
def mymapPad(*seqs,pad=None):
    maxlen=max(len(S) for S in seqs)
    index=range(maxlen)
    return [tuple((S[i] if len(S)>i else pad) for S in seqs) for i in index]

S1,S2='abc','xyz123'
print(myzip(S1,S2))
print(mymapPad(S1,S2))
print(mymapPad(S1,S2,pad=99),'\n')

