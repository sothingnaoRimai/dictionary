

d = {'second':58,'third':56,'gratest':100,'fourth':40,'fifth':20}
a=[]
max=0
nd=0
rd=0
# max_key=None
for i in d:
    for v in d:
        if d[v]>max:
            max=d[v]
            max_key=i
            g=max
        elif d[v] >nd and d[v]<max:
            nd=d[v]
            c=nd
        elif d[v] >rd and d[v]<nd:
            rd=d[v]
            k=rd
a.append(g)
a.append(c)
a.append(k)
print(a)