
nem={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50,"koney":9000}
p=sorted(nem.values())
# print(p)
a={}
for i in p:
    for j in nem.keys():
        if nem[j]==i:
            a[j]=i

print(a)