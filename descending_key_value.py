nem={'bijender':45,'deepak':60,'param':20,'anjili':300,'roshini':50}
p=sorted(nem.values())
# print(p)
a={}
for i in reversed(p):
    for j in reversed (nem.keys()):
        if nem[j]==i:
            a[j]=i
print(a)
