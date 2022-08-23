a={'a':[1,2,3],'b':[5,6,7]}
b={}
for j in a:
    i=-1
    c=a[j]
    l=[]
    while i>=-len(c):
        l.append(c[i])
        i-=1
    b[j]=l
print(b)