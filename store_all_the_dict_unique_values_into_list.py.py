a=[{"first":"1"},{"second": "2"},{"third": "1"},{"four": "5"},{"five":"5"},{"six":"9"},{"seven":"7"}]
a1=[]
for i in a:
    for j in i.values():
        if j not in a1:
            a1.append(j)
print(a1)