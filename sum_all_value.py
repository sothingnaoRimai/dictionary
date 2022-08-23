


a={'a':5,'b':10,'c':20,'d':5,'i':9}
s=0
b=[]
for i in a:
    s=s+a[i]
    b.append(a[i])
# print(s)
# print(b)
j=0
sum=0
while j<len(b):
    sum=sum+b[j]
    j=j+1
print(sum)