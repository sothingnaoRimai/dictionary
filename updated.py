d1={1:10, 2:20}
d2={2:30,9:40}
d3={1:50,6:60}
for i in d1:
    if i in d3:
        d3[i]=d1[i]+d3[i]
    elif i in d2:
        d2[i]=d1[i]+d2[i]
d1.update(d2)
d1.update(d3)
print(d1)