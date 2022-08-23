# # Ascending
l={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50,"koney":9000}
for x in l:
    for k in l:
        if l[k]<l[x]:
            l[k],l[x]=l[x],l[k]
        if l[x]<l[k]:

            l[x],l[k]=l[k],l[x]
print(l)